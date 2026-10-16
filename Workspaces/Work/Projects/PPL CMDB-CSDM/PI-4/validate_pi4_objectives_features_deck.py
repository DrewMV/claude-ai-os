"""Validate "PI4 - Draft - Oct 16.pptx" against the ADO query screenshot.

ADO truth is transcribed below from the second screenshot Manuel supplied on
2026-10-16 (ID / Type / Title / Parent / Start Date / Target Date). Sprints are
derived from the PI-4 iteration calendar, not asserted, so the deck is checked
against ADO rather than against itself.

NO DEVIATIONS REMAIN. The previous run carried ADO_TARGET_OVERRIDES because ADO
showed 1639206 (SolarWinds) with a 2026-11-24 target when the PO had confirmed
2026-11-10. This ADO pull shows 2026-11-10, so ADO has been corrected, the
override is gone and the matching open item has been dropped from slide 5.

Covers: slide 3 sprints and work-end dates, slide 4 sprint membership and counts,
slide 5 margins recomputed as gate minus work end, slide 6 bar/gate/lead geometry
and lane spacing, plus a sweep for stale strings left over from the prior deck.

Next cycle: update ADO{} and GATES{} from the new ADO query, point DECK at the new
file, and refresh the STALE list with the strings the previous deck carried.
Exits non-zero on any failure.

    python validate_pi4_objectives_features_deck.py

Requires python-pptx.
"""
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from pptx import Presentation

DECK = Path(r"C:\Users\manuel.b.vazquez\Documents\PI4 - Draft - Oct 16.pptx")

SPRINTS = [
    ("4.1", date(2026, 10, 28), date(2026, 11, 10)),
    ("4.2", date(2026, 11, 11), date(2026, 11, 24)),
    ("4.3", date(2026, 11, 25), date(2026, 12, 8)),
    ("4.4", date(2026, 12, 9), date(2026, 12, 22)),
    ("4.5", date(2026, 12, 23), date(2027, 1, 5)),
    ("4.6", date(2027, 1, 6), date(2027, 1, 19)),
    ("4.7 IP", date(2027, 1, 20), date(2027, 2, 2)),
]

# ADO screenshot, 2026-10-15
ADO = {
    "1639308": ("CMDB Adoption Campaign — Content, Training & Communications",
                "Drive CMDB Adoption Across PPL User Groups", date(2026, 11, 11), date(2027, 1, 19)),
    "1639335": ("CMDB Correctness (Staleness, Orphans, Duplication)",
                "Implement CMDB Lifecycle Management Process Flows", date(2026, 10, 28), date(2026, 11, 24)),
    "1640795": ("Interface (ex. service catalog item) — Non-Discoverable CI Attribute Updates",
                "Implement CMDB Lifecycle Management Process Flows", date(2026, 11, 11), date(2026, 11, 24)),
    "1640805": ("Server Build Lifecycle Process Flow",
                "Implement CMDB Lifecycle Management Process Flows", date(2026, 11, 25), date(2026, 12, 22)),
    "1640819": ("Server Decommission Lifecycle Process Flow",
                "Implement CMDB Lifecycle Management Process Flows", date(2026, 12, 9), date(2027, 1, 19)),
    "1640844": ("Catalog Item — Service Map Update Requests",
                "Implement CMDB Lifecycle Management Process Flows", date(2027, 1, 6), date(2027, 1, 19)),
    "1639206": ("Network Inventory Integration — SolarWinds",
                "Automate Network Gear Inventory in the CMDB", date(2026, 10, 28), date(2026, 11, 10)),
    "1639225": ("Network Inventory Integration — Cisco Catalyst",
                "Automate Network Gear Inventory in the CMDB", date(2026, 11, 11), date(2026, 11, 24)),
    "1639239": ("Network Inventory Integration POC — Qualys",
                "Automate Network Gear Inventory in the CMDB", date(2026, 11, 25), date(2026, 12, 8)),
    "1642237": ("15 Priority Service Maps — Built & Validated (2 OF 3)",
                "Build & Validate Service Maps for Priority Business Apps", date(2026, 11, 11), date(2026, 11, 24)),
    "1642240": ("Service Mapping — Automated Stakeholder Notifications in ITSM",
                "Build & Validate Service Maps for Priority Business Apps", date(2026, 11, 25), date(2026, 12, 8)),
    "1642332": ("Service Mapping — 15 Priority Apps (Batch 3 of 3)",
                "Build & Validate Service Maps for Priority Business Apps", date(2026, 12, 9), date(2026, 12, 22)),
    "1646517": ("15 Priority Service Maps — Built & Validated (1 OF 3)",
                "Build & Validate Service Maps for Priority Business Apps", date(2026, 10, 28), date(2026, 11, 10)),
    "1653575": ("Network Inventory Integration — Tripwire",
                "Automate Network Gear Inventory in the CMDB", date(2026, 12, 9), date(2026, 12, 22)),
}
OBJECTIVES = {
    "1639022": "Automate Network Gear Inventory in the CMDB",
    "1639027": "Build & Validate Service Maps for Priority Business Apps",
    "1639072": "Drive CMDB Adoption Across PPL User Groups",
    "1639075": "Implement CMDB Lifecycle Management Process Flows",
}
# ADO now matches the PO-confirmed dates for every feature — no overrides needed.
# All 14 features are PI-4 lanes now — SolarWinds moved in from PI-3 on 2026-10-16.
PI3_DELIVERY = set()


def sprint_of(d):
    for name, s, e in SPRINTS:
        if s <= d <= e:
            return name
    return None


def span(start, target):
    a, b = sprint_of(start), sprint_of(target)
    return a if a == b else f"{a}–{b}"


def fmt(d):
    return f"{d.strftime('%b')} {d.day}, {d.year}"


prs = Presentation(DECK)
S = list(prs.slides)
text_of = lambda sl: "\n".join(
    sh.text_frame.text for sh in sl.shapes if sh.has_text_frame
) + "\n" + "\n".join(
    c.text for sh in sl.shapes if sh.has_table for r in sh.table.rows for c in r.cells
)
ALL = {i: text_of(sl) for i, sl in enumerate(S, 1)}

fails, passes, warns = [], [], []


def check(cond, msg):
    (passes if cond else fails).append(msg)


print("=" * 78)
print("DERIVED EXPECTATIONS FROM ADO (screenshot 2026-10-15)")
print("=" * 78)
for ado, (title, parent, s, t) in sorted(ADO.items(), key=lambda kv: (kv[1][3], kv[1][2])):
    print(f"  {ado}  {span(s,t):<9} ends {fmt(t):<13}  {title[:55]}")

# ---- 1. slide 3 table: sprints + work-ends per feature
print("\n" + "=" * 78)
print("SLIDE 3 — Objective View table")
print("=" * 78)
t3 = next(sh.table for sh in S[2].shapes if sh.has_table)
rows3 = {t3.cell(r, 0).text.strip(): [t3.cell(r, c).text.strip() for c in range(6)]
         for r in range(len(t3.rows))}
for ado, (title, parent, s, t) in ADO.items():
    if ado in PI3_DELIVERY:
        check(ado in rows3, f"S3 {ado} present (PI-3 context row)")
        continue
    if ado not in rows3:
        fails.append(f"S3 {ado} MISSING from table")
        continue
    row = rows3[ado]
    check(row[2] == span(s, t), f"S3 {ado} sprints = {row[2]!r} (expect {span(s,t)!r})")
    check(row[3] == fmt(t), f"S3 {ado} work ends = {row[3]!r} (expect {fmt(t)!r})")
    check(title in row[1], f"S3 {ado} title matches ADO")
check("TBD" not in [r[0] for r in rows3.values()], "S3 no TBD placeholder rows remain")

# ---- 2. slide 4 sprint view: counts + membership by STARTING sprint
print("\n" + "=" * 78)
print("SLIDE 4 — Sprint View table")
print("=" * 78)
t4 = next(sh.table for sh in S[3].shapes if sh.has_table)
expected = {n: [] for n, _, _ in SPRINTS}
for ado, (title, parent, s, t) in ADO.items():
    if ado in PI3_DELIVERY:
        continue
    expected[sprint_of(s)].append(ado)
for ri in range(1, 8):
    name = t4.cell(ri, 0).text.strip().replace("Sprint ", "")
    shown_count = t4.cell(ri, 2).text.strip()
    body = t4.cell(ri, 3).text
    exp = sorted(expected[name])
    got = sorted(a for a in ADO if a in body)
    check(shown_count == str(len(exp)), f"S4 {name} count = {shown_count} (expect {len(exp)})")
    check(got == exp, f"S4 {name} members = {got} (expect {exp})")
total = sum(len(v) for v in expected.values())
check(total == 14, f"S4 total PI-4 features = {total} (expect 14)")

# ---- 3. every feature's sprint/date string is internally consistent on slide 4
for ado, (title, parent, s, t) in ADO.items():
    if ado in PI3_DELIVERY:
        continue
    frag = f"·  {span(s,t)}  ·  ends {fmt(t)}"
    check(frag in ALL[4], f"S4 {ado} span/end string {frag!r}")

# ---- 4. slide 5 compliance: margins = gate - work end
print("\n" + "=" * 78)
print("SLIDE 5 — AP00288 Compliance Check")
print("=" * 78)
t5 = next(sh.table for sh in S[4].shapes if sh.has_table)
MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def parse(s):
    m, d, y = s.replace(",", "").split()
    return date(int(y), MONTHS[m], int(d))


for ri in range(1, len(t5.rows)):
    ado = t5.cell(ri, 4).text.strip()
    gate_s, end_s, margin = (t5.cell(ri, 3).text.strip(),
                             t5.cell(ri, 5).text.strip(),
                             t5.cell(ri, 6).text.strip())
    if ado in ADO and ado not in PI3_DELIVERY:
        check(end_s == fmt(ADO[ado][3]), f"S5 D{t5.cell(ri,0).text} {ado} work ends {end_s!r} (expect {fmt(ADO[ado][3])!r})")
        days = (parse(gate_s) - parse(end_s)).days
        check(margin == f"✓ {days} days", f"S5 D{t5.cell(ri,0).text} {ado} margin {margin!r} (expect '✓ {days} days')")

# ---- 5. slide 6 program board geometry
print("\n" + "=" * 78)
print("SLIDE 6 — Program Board geometry")
print("=" * 78)
from pptx.util import Emu
X0, COLW, ORIGIN = 4.75, 1.15, date(2026, 10, 28)
sh6 = {sh.name: sh for sh in S[5].shapes}
GATES = {"1639206": date(2026, 12, 31),
         "1646517": date(2026, 11, 30), "1639335": date(2026, 12, 31),
         "1642237": date(2026, 12, 31), "1640795": date(2026, 12, 31),
         "1639225": date(2027, 2, 2), "1639308": date(2027, 1, 30),
         "1642240": date(2026, 12, 31), "1639239": date(2027, 2, 2),
         "1640805": date(2027, 2, 2), "1640819": date(2027, 2, 2),
         "1642332": date(2027, 2, 2), "1640844": date(2027, 2, 2),
         "1653575": date(2027, 2, 2)}
for ado, (title, parent, s, t) in ADO.items():
    if ado in PI3_DELIVERY:
        continue
    bar, gate, lead = sh6.get(f"bar-{ado}"), sh6.get(f"gate-{ado}"), sh6.get(f"lead-{ado}")
    if not (bar and gate and lead):
        fails.append(f"S6 {ado} missing bar/gate/lead")
        continue
    i0 = [n for n, _, _ in SPRINTS].index(sprint_of(s))
    i1 = [n for n, _, _ in SPRINTS].index(sprint_of(t))
    exp_l, exp_w = X0 + i0 * COLW, (i1 - i0 + 1) * COLW
    gl, gw = Emu(bar.left).inches, Emu(bar.width).inches
    check(abs(gl - exp_l) < 0.01, f"S6 {ado} bar left {gl:.2f} (expect {exp_l:.2f})")
    check(abs(gw - exp_w) < 0.01, f"S6 {ado} bar width {gw:.2f} (expect {exp_w:.2f})")
    exp_gx = X0 + ((GATES[ado] - ORIGIN).days / 98.0) * (7 * COLW) - 0.07
    check(abs(Emu(gate.left).inches - exp_gx) < 0.02,
          f"S6 {ado} gate x {Emu(gate.left).inches:.2f} (expect {exp_gx:.2f})")
    bar_end, lead_end = gl + gw, Emu(lead.left).inches + Emu(lead.width).inches
    check(abs(Emu(lead.left).inches - bar_end) < 0.02, f"S6 {ado} lead starts at bar end")
    check(abs(lead_end - (exp_gx + 0.07)) < 0.03, f"S6 {ado} lead reaches gate centre")
    # vertical: bar inside the plot band, nothing past the legend
    by = Emu(bar.top).inches
    check(1.45 <= by and by + 0.20 <= 6.30, f"S6 {ado} bar y {by:.2f} inside plot band")

# rows must not overlap
tops = sorted(Emu(sh6[f"bar-{a}"].top).inches for a in ADO if a not in PI3_DELIVERY)
gaps = [round(b - a, 3) for a, b in zip(tops, tops[1:])]
check(all(g >= 0.25 for g in gaps), f"S6 row gaps uniform & >=0.25in: {set(gaps)}")
check(len(tops) == 14, f"S6 14 lanes drawn (got {len(tops)})")

# ---- 6. stale content sweep
print("\n" + "=" * 78)
print("STALE CONTENT SWEEP")
print("=" * 78)
STALE = ["Oct 14, 2026", "Oct 15, 2026",
         "Tripwire has no ADO work item", "ADO work item still to be created",
         "Tripwire is not yet scheduled",
         # SolarWinds moved from PI-3 into PI-4 / 4.1 on 2026-10-16. The slide 4
         # footnote still says "moved from PI-3" on purpose — it tells the reader
         # what changed — so match the old *claims*, not the bare string "PI-3".
         "delivers in PI-3", "PI-3 · 3.6", "1 in PI-3", "SolarWinds in PI-3",
         "13 ADO features", "ahead of PI-4",
         "ADO still has SolarWinds starting",
         "·  4.6–4.7  ·",                      # Qualys' old span, as a feature row
         "4.3–4.4  ·  ends Dec 22, 2026  ·  D2",  # Cisco's old span, as a feature row
         "Feb 2, 2027  ·  deliverable TBC",    # Qualys formerly ran to the contract end date
         "1639239  —  Network Inventory Integration POC — Qualys   ·  4.6",
         # superseded by the Oct 14 direction: implementation is decided per integration,
         # so the deck must not assert that all four sources get implemented
         "evaluated and implemented",
         "evaluate and implement all four",
         "two of the four integrations are uncontracted",
         # superseded by the 2026-10-16 pull-forward of D5 and Tripwire from 4.6 to 4.4
         # (D12 legitimately still reads "4.6 · ends Jan 19, 2027", so qualify by code)
         "·  4.6  ·  ends Jan 19, 2027  ·  D5 gate",
         "4.6  ·  ends Jan 19, 2027  ·  deliverable TBC",
         "Tripwire now has an ADO item (1653575) in 4.6",
         # resolved: ADO now shows the Nov 10 target, so the deck must not still ask for the fix
         "shows a target date of Nov 24, 2026"]
for s in STALE:
    hits = [i for i, txt in ALL.items() if s in txt]
    check(not hits, f"stale {s!r} absent (found on {hits})" if hits else f"stale {s!r} absent")
check("Oct 16, 2026" in ALL[1], "S1 carries Oct 16, 2026")
for i in range(2, 7):
    check("Oct 16, 2026" in ALL[i], f"S{i} footer carries Oct 16, 2026")
check("1639206" in ALL[3] and "1639206" in ALL[4] and "1639206" in ALL[6],
      "SolarWinds 1639206 appears on slides 3, 4 and 6 as a PI-4 feature")
check("1653575" in ALL[3] and "1653575" in ALL[4] and "1653575" in ALL[6],
      "Tripwire 1653575 appears on slides 3, 4 and 6")
for oid, name in OBJECTIVES.items():
    check(oid in ALL[2], f"objective {oid} on slide 2")
    check(name in ALL[3], f"objective {name!r} banner on slide 3")

# ---- report
print("\n" + "=" * 78)
for p in passes:
    print("  PASS  ", p)
print("=" * 78)
if fails:
    for f in fails:
        print("  FAIL  ", f)
print(f"\n{len(passes)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)
