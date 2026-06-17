---
level: project
workspace: Research
project: notebooklm-pdf-load
status: active
created: 2026-06-08
updated: 2026-06-08
tags: [research]
---

## Goal

Split large PDF files into smaller PDFs suitable for NotebookLM source ingestion. Output files must comply with NotebookLM limits (250 pages, 75 MB per file), be split at TOC chapter/section boundaries, and the combined output must not exceed the original file size.

Done looks like: `python split_pdf.py <file.pdf>` produces a folder of named chapter PDFs that can be dragged directly into NotebookLM, all valid, all within limits.

## Current State

`src/split_pdf.py` implemented and ready to test. Splits by TOC → subsections → 250-page chunks as fallback. Validates all output files. Reports anti-bloat ratio.

## Key Decisions

- **pymupdf** for TOC parsing (best TOC extraction support)
- **pikepdf** for page extraction, **Ghostscript** for post-split optimization (font subsetting + stream recompression — the primary bloat source is shared embedded fonts duplicated across output files; GS resolves this by subsetting each output to only the glyphs it uses)
- Ghostscript is optional — script warns and continues without it; size check runs after GS, not before
- Output folder named after source file, created in same directory
- Output files named `{index:02d} - {chapter title}.pdf`
- 2% tolerance on anti-bloat check to account for unavoidable per-file metadata overhead
- Chapter intro pages (before first subsection) are preserved as a separate `intro` file
- NotebookLM upload is manual drag-and-drop (no API — NotebookLM has no public API)
- No Google Drive integration in current scope

## Active Context

- Script: `src/split_pdf.py`
- Dependencies: `src/requirements.txt` (pymupdf, pikepdf)
- Install: `pip install -r requirements.txt`
- Run: `python split_pdf.py <input.pdf> [output_dir]`

## Open Questions

- Does bloat warning trigger on real-world test PDFs with heavy shared fonts/images?
- Should front matter (pages before first TOC entry) be captured as a separate file?

## Sources

_No sources ingested yet._
