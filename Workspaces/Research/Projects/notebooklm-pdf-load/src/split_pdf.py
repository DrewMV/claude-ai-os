#!/usr/bin/env python3
"""
split_pdf.py — Split a large PDF by TOC chapters for NotebookLM ingestion.

Usage:
    python split_pdf.py <input.pdf>
    python split_pdf.py <input.pdf> <output_dir>
    python split_pdf.py <input.pdf> --limit 10   (test with first 10 files)

Each output file stays within 250 pages and 75 MB (NotebookLM source limits).
Splitting order:
  1. TOC chapters/sections
  2. TOC subsections (if a chapter exceeds 250 pages)
  3. 250-page chunks (if no subsections exist or chapter is still too large)

Pipeline per file:
  1. pikepdf extracts the page range (fast random access — no full-file scan)
  2. GS optimizes the small extracted file (font subsetting + recompression)
  3. Temp file deleted immediately

Peak disk usage: original file + (workers × ~100 MB temp) + small output files.
Default workers: 4  (adjust with --workers N)
"""

import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import fitz    # pymupdf — TOC parsing + content validation
import pikepdf # page extraction + structural validation

MAX_PAGES = 250
MAX_BYTES = 75 * 1024 * 1024  # 75 MB
DEFAULT_WORKERS = 4


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def sanitize(title: str, max_len: int = 80) -> str:
    """Make a TOC title safe to use as a filename."""
    clean = re.sub(r'[<>:"/\\|?*\x00-\x1f]', ' ', title)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean[:max_len] or "untitled"


def find_ghostscript() -> str | None:
    for cmd in ("gs", "gswin64c", "gswin32c"):
        if shutil.which(cmd):
            return cmd
    return None


def extract_and_optimize(args: tuple) -> tuple[str, int, int, str]:
    """
    Two-stage pipeline for one output file:
      1. pikepdf extracts pages [start..end] into a temp file (fast random access)
      2. GS optimizes the temp file (font subsetting + recompression) → final output
      3. Temp file is deleted

    Args tuple: (input_path, start, end, out_path, gs_exe)
    Returns: (out_path, page_count, size_bytes, error_message)
    """
    input_path, start, end, out_path, gs_exe = args
    tmp_path = out_path + "._tmp.pdf"

    # Stage 1: pikepdf extraction (random access, no full-file scan)
    try:
        with pikepdf.open(input_path) as src:
            dst = pikepdf.Pdf.new()
            dst.pages.extend(src.pages[start: end + 1])
            dst.save(
                tmp_path,
                compress_streams=True,
                object_stream_mode=pikepdf.ObjectStreamMode.generate,
            )
    except Exception as e:
        return out_path, 0, 0, f"pikepdf error: {e}"

    # Stage 2: GS optimization (on the small temp file — completes in seconds)
    try:
        result = subprocess.run(
            [
                gs_exe,
                "-dBATCH", "-dNOPAUSE", "-dQUIET",
                "-sDEVICE=pdfwrite",
                "-dCompatibilityLevel=1.4",
                "-dPDFSETTINGS=/prepress",
                f"-sOutputFile={out_path}",
                tmp_path,
            ],
            capture_output=True,
            timeout=120,
        )
    except subprocess.TimeoutExpired:
        _cleanup(tmp_path)
        return out_path, 0, 0, "gs timed out (120s)"
    except Exception as e:
        _cleanup(tmp_path)
        return out_path, 0, 0, f"gs error: {e}"
    finally:
        _cleanup(tmp_path)

    if result.returncode != 0 or not os.path.isfile(out_path):
        err = result.stderr.decode(errors="replace").strip()
        return out_path, 0, 0, f"gs error: {err[:200]}"

    size = os.path.getsize(out_path)
    if size == 0:
        return out_path, 0, 0, "gs produced empty file"

    return out_path, end - start + 1, size, ""


def _cleanup(path: str) -> None:
    try:
        if os.path.isfile(path):
            os.remove(path)
    except Exception:
        pass


def validate(path: Path) -> tuple[Path, bool, str]:
    """
    Two-pass validation:
      1. pikepdf — PDF structure and object integrity
      2. pymupdf — content-stream parsing per page (catches corrupt font
         streams and broken xrefs that pikepdf tolerates)
    Returns (path, ok, error_message).
    """
    try:
        with pikepdf.open(str(path)) as p:
            if len(p.pages) == 0:
                return path, False, "no pages"
    except Exception as e:
        return path, False, f"structure error: {e}"

    try:
        doc = fitz.open(str(path))
        for i in range(len(doc)):
            doc[i].get_text()
        doc.close()
    except Exception as e:
        return path, False, f"content error: {e}"

    return path, True, ""


def parse_toc(input_path: str) -> tuple[list[tuple], int]:
    """
    Return (segments, total_pages) where each segment is
    (level, title, start_0idx, end_0idx).

    Each segment's end is the page before the next entry at the same or
    higher level — giving each chapter its full scope including subsections.
    """
    doc = fitz.open(input_path)
    total = doc.page_count
    raw = doc.get_toc()
    doc.close()

    if not raw:
        raise ValueError(
            "No table of contents found in this PDF.\n"
            "Cannot split by chapters without a TOC."
        )

    segments = []
    for i, (lvl, title, page) in enumerate(raw):
        start = page - 1  # 0-indexed

        chapter_end = total - 1
        for j in range(i + 1, len(raw)):
            if raw[j][0] <= lvl:
                chapter_end = raw[j][2] - 2
                break

        start = max(0, min(start, total - 1))
        chapter_end = max(start, min(chapter_end, total - 1))
        segments.append((lvl, title, start, chapter_end))

    return segments, total


# ---------------------------------------------------------------------------
# Planning phase — pure logic, no I/O
# ---------------------------------------------------------------------------

def plan_splits(segments: list[tuple], top_level: list[int], out_dir: Path) -> list[dict]:
    """
    Recursively determine all output files based on TOC structure and page limits.
    Uses hierarchical numbering so grouping is visible in filenames:
      - Chapter fits in one file:        37 - Chapter Title.pdf
      - Chapter split into subsections:  37-00 - Chapter Title.pdf  (intro)
                                         37-01 - Subsection A.pdf
                                         37-02 - Subsection B.pdf
      - Chapter chunked (no subsections):37-01 - Chapter Title.pdf
                                         37-02 - Chapter Title.pdf
    Returns a plan: list of {out_path, src_start, src_end, title, pages}.
    No files are written here.
    """
    top_counter = [0]
    plan = []

    def plan_segment(idx: int, my_num: str | None = None) -> None:
        lvl, title, start, end = segments[idx]
        page_count = end - start + 1

        children = [
            i for i, (l, _, s, _) in enumerate(segments)
            if l == lvl + 1 and segments[i][2] >= start and segments[i][2] <= end
        ]

        if my_num is None:
            top_counter[0] += 1
            my_num = f"{top_counter[0]:02d}"

        if page_count <= MAX_PAGES:
            out_path = out_dir / f"{my_num} - {sanitize(title)}.pdf"
            plan.append({
                "out_path": out_path, "src_start": start, "src_end": end,
                "title": title, "pages": page_count,
            })
            return

        if children:
            first_child_start = segments[children[0]][2]
            if first_child_start > start:
                out_path = out_dir / f"{my_num}-00 - {sanitize(title)}.pdf"
                plan.append({
                    "out_path": out_path, "src_start": start,
                    "src_end": first_child_start - 1,
                    "title": f"{title} (intro)", "pages": first_child_start - start,
                })
            sub = [0]
            for child_i in children:
                sub[0] += 1
                plan_segment(child_i, my_num=f"{my_num}-{sub[0]:02d}")
            return

        chunk_start = start
        part = 1
        while chunk_start <= end:
            chunk_end = min(chunk_start + MAX_PAGES - 1, end)
            out_path = out_dir / f"{my_num}-{part:02d} - {sanitize(title)}.pdf"
            plan.append({
                "out_path": out_path, "src_start": chunk_start, "src_end": chunk_end,
                "title": f"{title} (part {part})", "pages": chunk_end - chunk_start + 1,
            })
            chunk_start = chunk_end + 1
            part += 1

    for i in top_level:
        plan_segment(i)

    return plan


def run_extractions(plan_entries: list[dict], input_path: str, gs_exe: str, workers: int) -> list[tuple]:
    """Run extract_and_optimize in parallel. Returns list of (out_path, err) for failures."""
    args = [
        (input_path, p["src_start"], p["src_end"], str(p["out_path"]), gs_exe)
        for p in plan_entries
    ]
    path_to_entry = {str(p["out_path"]): p for p in plan_entries}
    errors = []

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(extract_and_optimize, a): a for a in args}
        for future in as_completed(futures):
            out_path, pages, size, err = future.result()
            entry = path_to_entry[out_path]
            if err:
                errors.append((out_path, err))
                print(f"  ERROR  {Path(out_path).name}  ({err})")
            else:
                entry["bytes"] = size
                entry["pages"] = pages
                print(f"  {Path(out_path).name}  ({pages}p, {size / 1e6:.1f} MB)")

    return errors


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def split_pdf(input_path: str, output_dir: str | None = None,
              limit: int | None = None, workers: int = DEFAULT_WORKERS) -> None:
    input_path = os.path.abspath(input_path)
    if not os.path.isfile(input_path):
        sys.exit(f"Error: file not found: {input_path}")

    gs_exe = find_ghostscript()
    if not gs_exe:
        sys.exit(
            "Error: Ghostscript not found on PATH.\n"
            "Install: winget install ArtifexSoftware.GhostScript"
        )

    original_size = os.path.getsize(input_path)
    stem = Path(input_path).stem
    out_dir = Path(output_dir) if output_dir else Path(input_path).parent / stem
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Source:      {input_path}")
    print(f"Size:        {original_size / 1e6:.1f} MB")
    print(f"Output dir:  {out_dir}")
    print(f"Ghostscript: {gs_exe}")
    print(f"Workers:     {workers}\n")

    try:
        segments, total_pages = parse_toc(input_path)
    except ValueError as e:
        sys.exit(f"Error: {e}")

    print(f"TOC entries: {len(segments)}")
    print(f"Total pages: {total_pages}\n")

    top_level = [i for i, (l, _, _, _) in enumerate(segments) if l == 1]
    if not top_level:
        top_level = list(range(len(segments)))

    # --- Phase 1: Plan ---
    plan = plan_splits(segments, top_level, out_dir)
    if limit:
        plan = plan[:limit]
        print(f"Planned {len(plan)} output files (limited to first {limit}).\n")
    else:
        print(f"Planned {len(plan)} output files.\n")

    # --- Phase 2: Extract + optimize ---
    print(f"Extracting and optimizing {len(plan)} files ({workers} workers)...")
    errors = run_extractions(plan, input_path, gs_exe, workers)

    if errors:
        print(f"\n{len(errors)} file(s) failed extraction — aborting.")
        sys.exit(1)

    # --- Phase 3: Re-chunk any files still over size limit after GS ---
    oversized = [p for p in plan if p.get("bytes", 0) > MAX_BYTES]
    if oversized:
        print(f"\n{len(oversized)} file(s) still exceed {MAX_BYTES / 1e6:.0f} MB — re-chunking...")
        new_entries = []
        for entry in oversized:
            plan.remove(entry)
            entry["out_path"].unlink(missing_ok=True)
            chunk_start = entry["src_start"]
            part = 1
            base = entry["out_path"].stem
            while chunk_start <= entry["src_end"]:
                chunk_end = min(chunk_start + MAX_PAGES - 1, entry["src_end"])
                new_entries.append({
                    "out_path": out_dir / f"{base} part {part}.pdf",
                    "src_start": chunk_start, "src_end": chunk_end,
                    "title": f"{entry['title']} (part {part})",
                    "pages": chunk_end - chunk_start + 1,
                })
                chunk_start = chunk_end + 1
                part += 1

        run_extractions(new_entries, input_path, gs_exe, workers)
        plan.extend(new_entries)

    # --- Phase 4: Validation (parallel) ---
    print(f"\nValidating {len(plan)} files...")
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(validate, p["out_path"]): p for p in plan}
        bad = []
        for future in as_completed(futures):
            path, ok, err = future.result()
            if ok:
                print(f"  OK  {path.name}")
            else:
                bad.append((path, err))
                print(f"  FAIL  {path.name}  ({err})")

    if bad:
        sys.exit(
            f"\nERROR: {len(bad)} corrupt file(s):\n"
            + "\n".join(f"  {p}  ({err})" for p, err in bad)
        )
    print(f"  All {len(plan)} files passed structure + content checks.\n")

    # --- Anti-bloat check ---
    combined = sum(p.get("bytes", 0) for p in plan)
    ratio = combined / original_size
    print(f"Size check:")
    print(f"  Original: {original_size / 1e6:.1f} MB")
    print(f"  Combined: {combined / 1e6:.1f} MB  ({ratio:.1%})")
    if ratio > 1.02:
        print(
            "  WARNING: combined output exceeds original despite GS optimization.\n"
            "  Likely cause: images or content duplicated across many small chapters."
        )
    else:
        print("  OK — within acceptable range.")

    print(f"\nDone. {len(plan)} files written to:\n  {out_dir}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Split a large PDF by TOC chapters.")
    parser.add_argument("input", help="Path to the source PDF")
    parser.add_argument("output_dir", nargs="?", help="Output directory (default: next to input)")
    parser.add_argument("--limit", type=int, help="Only process the first N planned files (for testing)")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS,
                        help=f"Parallel workers (default: {DEFAULT_WORKERS}). "
                             f"Higher = faster but more temp disk usage (~100 MB per worker).")
    args = parser.parse_args()
    split_pdf(args.input, args.output_dir, args.limit, args.workers)
