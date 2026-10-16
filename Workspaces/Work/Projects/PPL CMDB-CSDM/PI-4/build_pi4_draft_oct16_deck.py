"""Build "PI4 - Draft - Oct 16.pptx" from the 2026-10-16 deck.

Applies the ADO pull of 2026-10-16 (second query of the day):

  1642332 Service Mapping Batch 3 (D5) : 4.6 -> 4.4   (ends Jan 19, 2027 -> Dec 22, 2026)
  1653575 Tripwire                     : 4.6 -> 4.4   (ends Jan 19, 2027 -> Dec 22, 2026)

Both pulled forward a sprint and a half. D5 is contracted against the Feb 2, 2027
gate, so its margin improves 14 -> 42 days.

Also closes open item 3 on slide 5. The 2026-10-16 deck flagged that ADO 1639206
(SolarWinds) still showed a Nov 24, 2026 target when Nov 10 was correct. This ADO
pull shows Nov 10, so ADO has been corrected and the item is dropped.

Feature count stays 14 and the program board stays 14 lanes, so the row pitch is
unchanged at 0.286in; only lane ORDER and the two moved bars change.

The 2026-10-16 deck and every earlier deck are left untouched.

    python build_pi4_draft_oct16_deck.py
    python validate_pi4_objectives_features_deck.py

Requires python-pptx.
"""
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from pptx import Presentation
from pptx.util import Inches

SRC = Path(r"C:\Users\manuel.b.vazquez\Documents\PI4-Objectives-Features-2026-10-16.pptx")
DST = Path(r"C:\Users\manuel.b.vazquez\Documents\PI4 - Draft - Oct 16.pptx")

shutil.copyfile(SRC, DST)
prs = Presentation(DST)
S = list(prs.slides)

log = []


def note(msg):
    log.append(msg)


# ---------------------------------------------------------------- helpers
def shapes_by_name(slide):
    return {sh.name: sh for sh in slide.shapes}


def find_tb(slide, needle):
    for sh in slide.shapes:
        if sh.has_text_frame and needle in sh.text_frame.text:
            return sh
    raise KeyError(f"textbox containing {needle!r} not found")


def set_cell(cell, text):
    runs = [r for p in cell.text_frame.paragraphs for r in p.runs]
    assert runs, f"no runs in cell (wanted to write {text!r})"
    runs[0].text = text
    for r in runs[1:]:
        r.text = ""


def set_sprint_cell(cell, features):
    """One paragraph per feature, each with exactly three runs."""
    import copy as _copy
    tf = cell.text_frame
    txBody = tf._txBody
    template = _copy.deepcopy(tf.paragraphs[0]._p)
    while len(tf.paragraphs) > len(features):
        txBody.remove(tf.paragraphs[-1]._p)
    while len(tf.paragraphs) < len(features):
        txBody.append(_copy.deepcopy(template))
    for p, (ado, name, tail) in zip(tf.paragraphs, features):
        runs = p.runs
        assert len(runs) == 3, f"expected 3 runs, got {len(runs)}"
        runs[0].text = f"{ado}  —  "
        runs[1].text = name
        runs[2].text = tail


# ================================================================ SLIDE 3
s3 = S[2]
t3 = next(sh.table for sh in s3.shapes if sh.has_table)
for ri, ado in ((5, "1653575"), (10, "1642332")):
    assert t3.cell(ri, 0).text.strip() == ado, f"S3 row {ri} is not {ado}"
    set_cell(t3.cell(ri, 2), "4.4")
    set_cell(t3.cell(ri, 3), "Dec 22, 2026")
note("S3  1642332 (D5) and 1653575 (Tripwire): 4.6 -> 4.4, end Jan 19 -> Dec 22, 2026")

# ================================================================ SLIDE 4
s4 = S[3]
t4 = next(sh.table for sh in s4.shapes if sh.has_table)

F_MAPS3 = ("1642332", "Service Mapping — 15 Priority Apps (Batch 3 of 3)",
           "   ·  4.4  ·  ends Dec 22, 2026  ·  D5 gate Feb 2, 2027")
F_TRIPWIRE = ("1653575", "Network Inventory Integration — Tripwire",
              "   ·  4.4  ·  ends Dec 22, 2026  ·  deliverable TBC — gate Feb 2, 2027")
F_SDECOM = ("1640819", "Server Decommission Lifecycle Process Flow",
            "   ·  4.4–4.6  ·  ends Jan 19, 2027  ·  D11 gate Feb 2, 2027")
F_CATITEM = ("1640844", "Catalog Item — Service Map Update Requests",
             "   ·  4.6  ·  ends Jan 19, 2027  ·  D12 gate Feb 2, 2027")

for ri, count, feats in ((4, "3", [F_MAPS3, F_TRIPWIRE, F_SDECOM]),
                         (6, "1", [F_CATITEM])):
    set_cell(t4.cell(ri, 2), count)
    set_sprint_cell(t4.cell(ri, 3), feats)
note("S4  sprint load 4.1=3  4.2=4  4.3=3  4.4=3  4.5=0  4.6=1  4.7 IP=0  (14 PI-4 features)")

foot4 = find_tb(s4, "All four network gear integrations")
runs4 = [r for p in foot4.text_frame.paragraphs for r in p.runs]
runs4[0].text = (
    "All four network gear integrations now sit in PI-4 — SolarWinds in 4.1, ending Nov 10, 2026. "
    "Service Mapping Batch 3 (D5) and Tripwire have both pulled forward from 4.6 to 4.4, ending "
    "Dec 22, 2026. Adoption Campaign (D7) and Server Decommission Lifecycle (D11) are the only work "
    "carrying through the holiday sprint, and no PI-4 feature extends into 4.7 IP."
)
for r in runs4[1:]:
    r.text = ""
note("S4  footnote: records the D5 + Tripwire pull-forward")

# ================================================================ SLIDE 5
s5 = S[4]
t5 = next(sh.table for sh in s5.shapes if sh.has_table)
assert t5.cell(5, 4).text.strip() == "1642332", "S5 row 5 is not D5 / 1642332"
set_cell(t5.cell(5, 5), "Dec 22, 2026")
set_cell(t5.cell(5, 6), "✓ 42 days")
note("S5  D5 (1642332): work ends Jan 19 -> Dec 22, 2026; margin 14 -> 42 days")

open_items = find_tb(s5, "Open items")
oi_runs = [r for p in open_items.text_frame.paragraphs for r in p.runs]
oi_runs[1].text = (
    "1.  Direction received Oct 14: evaluate all four network gear sources for relevance and performance, "
    "with the decision to proceed taken individually for each. The new SOW is expected to match; numbering "
    "below is from an earlier draft and is still to be verified.    2.  SolarWinds (D1) and Cisco Catalyst "
    "(D2) are contracted with fixed gates, so their decision to proceed is effectively made by the contract "
    "— only Qualys (1639239) and Tripwire (1653575) carry a genuine go/no-go, and neither has a deliverable "
    "number."
)
for r in oi_runs[2:]:
    r.text = ""
note("S5  open item 3 dropped — ADO now shows SolarWinds target Nov 10, 2026, so deck and ADO agree")

# ================================================================ SLIDE 6
s6 = S[5]
TEAL, MAROON, GOLD, NAVY_HEX = "0B6E7F", "6D2E46", "9C6F15", "1E2761"

# label, name, ado, colour, bar left/width, gate x, lead left/width
# ordered by starting sprint, then by work-end date
ROWS = [
    ("D1",  "SolarWinds",                      "1639206", NAVY_HEX,  4.75, 1.15,  9.94,  5.90, 4.11),
    ("D3",  "15 Maps (1 of 3)",                "1646517", TEAL,      4.75, 1.15,  7.39,  5.90, 1.56),
    ("D8",  "CMDB Correctness",                "1639335", MAROON,    4.75, 2.30,  9.94,  7.05, 2.96),
    ("D4",  "15 Maps (2 of 3)",                "1642237", TEAL,      5.90, 1.15,  9.94,  7.05, 2.96),
    ("D9",  "Non-Discoverable CI Interface",   "1640795", MAROON,    5.90, 1.15,  9.94,  7.05, 2.96),
    ("D2",  "Cisco Catalyst",                  "1639225", NAVY_HEX,  5.90, 1.15, 12.65,  7.05, 5.67),
    ("D7",  "Adoption Campaign",               "1639308", GOLD,      5.90, 5.75, 12.40, 11.65, 0.82),
    ("D6",  "Stakeholder Notifications",       "1642240", TEAL,      7.05, 1.15,  9.94,  8.20, 1.81),
    ("TBC", "Qualys",                          "1639239", NAVY_HEX,  7.05, 1.15, 12.65,  8.20, 4.52),
    ("D10", "Server Build Lifecycle",          "1640805", MAROON,    7.05, 2.30, 12.65,  9.35, 3.37),
    ("D5",  "15 Maps (3 of 3)",                "1642332", TEAL,      8.20, 1.15, 12.65,  9.35, 3.37),
    ("TBC", "Tripwire",                        "1653575", NAVY_HEX,  8.20, 1.15, 12.65,  9.35, 3.37),
    ("D11", "Server Decommission Lifecycle",   "1640819", MAROON,    8.20, 3.45, 12.65, 11.65, 1.07),
    ("D12", "Service Map Update Catalog Item", "1640844", MAROON,   10.50, 1.15, 12.65, 11.65, 1.07),
]

by_name = shapes_by_name(s6)
labels = {}
for sh in s6.shapes:
    if sh.has_text_frame:
        txt = sh.text_frame.text
        for *_, ado, _c, _bl, _bw, _gx, _ll, _lw in ROWS:
            if ado in txt and "  " in txt:
                labels[ado] = sh

BAR_Y0, STEP = 2.27, 0.286  # unchanged from the Oct 16 deck — still 14 lanes
for i, (dcode, name, ado, hexcol, bl, bw, gx, ll, lw) in enumerate(ROWS):
    by = BAR_Y0 + i * STEP

    lbl = labels[ado]
    lbl.top = Inches(by - 0.07)
    runs = [r for p in lbl.text_frame.paragraphs for r in p.runs]
    runs[0].text = f"{dcode}  "
    runs[1].text = name
    runs[2].text = f"   {ado}"

    bar = by_name[f"bar-{ado}"]
    bar.left, bar.top, bar.width = Inches(bl), Inches(by), Inches(bw)

    gate = by_name[f"gate-{ado}"]
    gate.left, gate.top = Inches(gx), Inches(by + 0.03)

    lead = by_name[f"lead-{ado}"]
    lead.left, lead.top, lead.width = Inches(ll), Inches(by + 0.10), Inches(lw)

note("S6  D5 and Tripwire moved to the 4.4 column; 14 lanes re-ordered by start sprint then end date")

prs.save(DST)
print(f"WROTE {DST}\n")
for line in log:
    print(" •", line)
