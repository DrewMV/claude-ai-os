"""
CMDB-CSDM Weekly Leadership Status Deck generator.

Single source of truth for the weekly status report. Edit the CONTENT
section below, then run:  python build_status_deck.py
Outputs (named by EDITION date):
  - <EDITION>.pptx   PowerPoint for customer leadership
  - <EDITION>.md     Marp markdown mirror for Obsidian

Weekly update workflow:
  1. Copy last week's values, bump EDITION / WEEK_LABEL / ITERATION.
  2. Move resolved items out of RISKS; refresh THIS_WEEK with the new deltas
     (this is what powers the "week over week" view).
  3. Re-run the script.
"""
import os
import json
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---------------------------------------------------------------------------
# CONTENT  (edit this block each week)
# ---------------------------------------------------------------------------
EDITION      = "2026-06-12"
WEEK_LABEL   = "Week of June 11, 2026  (updated June 12, 12:00pm EST)"
PI           = "PI-2"
PI_WINDOW    = "May 13 - Aug 4, 2026"
ITERATION    = "Iteration 2.3  (Jun 10 - 23)"
AUTHOR       = "Manuel Vazquez  -  Scrum Master, CMDB-CSDM"
EDITION_NOTE = "Updated 6/12 12:00pm EST - first week-over-week deltas vs the 6/11 baseline."

OVERALL_STATUS = ("ON TRACK - WITH WATCH ITEMS",
                  "Delivery is progressing across all 6 objectives. Two items resolved since the 6/11 "
                  "baseline (NowAssist resourcing, SCCM approval gate). New watch item: Qualys integration "
                  "blocked pending a vendor plugin approval. DNS dependency and code-freeze windows remain.")

# Operational priority (0 = most urgent), Objective, ADO Obj, Business Value, RAG, one-line status,
# then DERIVED story counts (provisional, not ADO-validated): scope, moving, stuck
OBJECTIVES = [
    ("P0", "Governed VMware-to-Azure Migration (Airlift)",        "1420079", 10, "GREEN", "On track - 3 airlift stories in validation; CI auto-populate active", 4, 4, 0),
    ("P1", "Automate Discovery Coverage for Network Gear",        "1366657", 10, "AMBER", "Improving - SCCM gate cleared; precedence stories in validation; ~6 not yet ID'd", 6, 6, 0),
    ("P1", "Establish CI Data Certification Program",             "1420082",  8, "GREEN", "On track - dashboard signed off (PROD Jun 23); pilot changes in validation", 2, 2, 0),
    ("P2", "Expand Service Mapping Foundation",                   "1366660",  9, "AMBER", "On track - discovery scaling; DNS dependency still open",  6, 6, 0),
    ("P2", "Regulatory & Security Integrations (Qualys/NERC/CCB)", "1366662",  8, "AMBER", "Watch - Qualys plugin BLOCKED on vendor approval; CCB Jun 16 / Audit Jun 18", 3, 1, 2),
    ("P3", "Embed NowAssist AI Across CMDB & ITSM",               "1408764",  7, "GREEN", "Unblocked - 4 stories reassigned to Kiran; 1 active, 3 ready + baseline spike", 5, 5, 0),
]
# Provisional portfolio totals (derived from team notes; replace once ADO-validated)
OBJ_SCOPE  = sum(o[6] for o in OBJECTIVES)
OBJ_MOVING = sum(o[7] for o in OBJECTIVES)
OBJ_STUCK  = sum(o[8] for o in OBJECTIVES)
STORY_CAVEAT = ("Story counts derived from team notes - PROVISIONAL, not ADO-validated. "
                "'Completed' tracking begins at first PROD deploy (Jun 23).")

# ---------------------------------------------------------------------------
# WEEK-OVER-WEEK HISTORY  (#1: persist a snapshot each run, diff vs prior)
# ---------------------------------------------------------------------------
HISTORY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "status_history.json")
RAG_RANK = {"RED": 1, "AMBER": 2, "GREEN": 3}
RAGWORD  = {"GREEN": "On track", "AMBER": "Watch", "RED": "Blocked"}


def load_history():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def current_snapshot():
    return {
        "week_label": WEEK_LABEL,
        "iteration": ITERATION,
        "portfolio": {"scope": OBJ_SCOPE, "moving": OBJ_MOVING, "stuck": OBJ_STUCK},
        "objectives": {o[1]: {"pri": o[0], "rag": o[4], "scope": o[6],
                              "moving": o[7], "stuck": o[8]} for o in OBJECTIVES},
    }


HISTORY = load_history()
CURR = current_snapshot()
_prior_keys = sorted(k for k in HISTORY if k < EDITION)
PRIOR_EDITION = _prior_keys[-1] if _prior_keys else None
PRIOR = HISTORY.get(PRIOR_EDITION)


def wow_rows():
    """Per-objective status transitions vs the prior snapshot.
    Empty list on a baseline edition (no prior snapshot exists yet)."""
    if not PRIOR:
        return []
    prev = PRIOR.get("objectives", {})
    out = []
    for o in OBJECTIVES:
        name, rag, scope, moving, stuck = o[1], o[4], o[6], o[7], o[8]
        p = prev.get(name)
        if not p:
            out.append({"name": name, "last": None, "this": rag,
                        "d_moving": None, "d_stuck": None, "trend": "NEW"})
            continue
        if RAG_RANK[rag] > RAG_RANK[p["rag"]]:
            trend = "UP"
        elif RAG_RANK[rag] < RAG_RANK[p["rag"]]:
            trend = "DOWN"
        else:
            trend = "SAME"
        out.append({"name": name, "last": p["rag"], "this": rag,
                    "d_moving": moving - p["moving"], "d_stuck": stuck - p["stuck"],
                    "trend": trend})
    return out


def wow_transitions():
    """(newly_blocked, newly_unblocked) objective-name lists vs prior snapshot."""
    blocked, unblocked = [], []
    if PRIOR:
        prev = PRIOR.get("objectives", {})
        for o in OBJECTIVES:
            name, rag = o[1], o[4]
            p = prev.get(name)
            if not p:
                continue
            if p["rag"] != "RED" and rag == "RED":
                blocked.append(name)
            elif p["rag"] == "RED" and rag != "RED":
                unblocked.append(name)
    return blocked, unblocked

# PI over PI
PI_PROGRESS = [
    ("PI-2", "May 13 - Aug 4, 2026", "ACTIVE", "Iteration 2.3 of 6", "6 objectives in flight; foundation laid + first PROD deployment"),
    ("PI-3", "Aug 5 - Oct 27, 2026", "PLANNING", "Planning Jul 22 - Aug 4", "NowAssist 5-phase rollout, Qualys Phase 2, CI Cert extended scope"),
]
PI_NOTE = "Only PI-2 has live data today. PI-over-PI comparison populates once PI-3 begins (planning during the PI-2 IP iteration)."

# Iteration over Iteration: id, window, status, theme, outcomes[]
ITERATIONS = [
    ("2.1", "May 13 - 26",   "COMPLETED", "Foundation & refinement",
        ["Airlift + CI auto-population stories shaped",
         "OOTB-first & customization governance established",
         "Retro theme: credential blockers dominated the sprint"]),
    ("2.2", "May 27 - Jun 9", "COMPLETED", "SCCM precedence & unblocking",
        ["SCCM locked as authoritative for 6 hardware attributes",
         "Service Mapping credentials resolved (6/9)",
         "Airlift dev admin access resolved (6/9)",
         "NowAssist activation stories created & assigned"]),
    ("2.3", "Jun 10 - 23",   "ACTIVE", "Deploy & scale",
        ["Data Certification -> PROD (Jun 23)",
         "SCCM precedence stories advanced to validation; approval gate cleared",
         "Service Mapping subnet scans expanding",
         "Qualys read-only integration blocked on vendor plugin approval",
         "NowAssist activation reassigned to Kiran Dhobale - in progress"]),
]
VELOCITY_NOTE = ("Quantitative velocity (committed vs. accepted points) is not yet captured in sprint "
                 "ceremonies. Establishing this metric is an active process-improvement item.")

# Week over week
THIS_WEEK = [
    "NowAssist resourcing resolved - 4 OOB stories reassigned to Kiran Dhobale; prerequisites story now active, others ready.",
    "SCCM approval gate cleared - timestamp-alignment story unblocked; all SCCM precedence stories now in validation.",
    "Airlift migration stories advanced to validation.",
    "Data Certification pilot changes in validation; dashboard PROD deploy on track for Jun 23.",
]
WEEK_NOTE = "First edition = baseline. From next week this slide shows what moved vs. the prior report."

# Deep dives: header, [(item, status, detail)]
DEEP_DIVE_1 = ("Highest-Priority Objectives (P0 - P1)", [
    ("Airlift (P0)",            "GREEN", "Pre/During/Post-Migration stories in validation; CI auto-populate active. Dev access resolved 6/9."),
    ("Data Certification (P1)", "GREEN", "Dashboard signed off 6/10; PROD Jun 23, Todd validates Jun 24-25. Pilot changes in validation."),
    ("Discovery / SCCM (P1)",   "AMBER", "SCCM approval gate cleared - timestamp story unblocked; precedence stories in validation. ~6 stories still need ADO IDs."),
])
DEEP_DIVE_2 = ("Supporting Objectives (P2 - P3)", [
    ("Service Mapping (P2)",  "AMBER", "Discovery scaling - infrastructure previously invisible now found. DNS dependency still open."),
    ("Regulatory / Qualys (P2)", "AMBER", "Qualys read-only stories BLOCKED - vendor plugin replacement pending approval. CCB Jun 16, Audit Sync Jun 18. NERC-CIP early engagement."),
    ("NowAssist AI (P3)",     "GREEN", "Resourcing resolved - 4 OOB stories reassigned to Kiran Dhobale; 1 active, 3 ready + health-baseline spike. Feature 1436574 confirmed."),
])

# Milestones
MILESTONES = [
    ("Jun 15", "Data Certification UAT gate"),
    ("Jun 16", "CMDB CCB Meeting"),
    ("Jun 17", "Backlog Refinement 2.3"),
    ("Jun 18", "CMDB Audit Sync"),
    ("Jun 19", "PROD Change Request - Data Certification"),
    ("Jun 23", "Sprint 2.3 end + Data Certification PROD deployment"),
    ("Jun 24-25", "Todd validates Data Certification in PROD"),
]

# Risks & asks: risk, severity, detail, ask
RISKS = [
    ("Qualys vendor approval", "HIGH", "Qualys replaced its plugin version; previous uninstalled, new one requested. Stories 1428703/1428704 blocked.", "Support / expedite vendor approval to unblock the read-only integration."),
    ("Service Mapping DNS",  "HIGH", "Reverse-DNS issue limits full discovery coverage.", "Leadership support on the DNS / infra dependency."),
    ("Code-freeze windows",  "HIGH", "Dev freeze Jun 27 - Jul 18; Test freeze Jul 18 - Aug 15 compresses PI-2 completion.", "Awareness; sequence deployments around freezes."),
]

# What's next
NEXT = [
    "PI-3 Planning during the IP iteration (Jul 22 - Aug 4).",
    "NowAssist Phase 1+: Duplicate CI Elimination, NL CMDB Search.",
    "Qualys Phase 2: two-way integration for data completeness.",
    "CI Certification: extend program beyond Business Apps.",
    "Plan delivery around code freezes (Dev Jun 27-Jul 18, Test Jul 18-Aug 15).",
]

# ---------------------------------------------------------------------------
# THEME
# ---------------------------------------------------------------------------
DARK   = RGBColor(0x1F, 0x3A, 0x5F)   # navy
ACCENT = RGBColor(0x2E, 0x6D, 0xB4)   # blue
LIGHT  = RGBColor(0xF4, 0xF6, 0xF9)   # near-white panel
TEXT   = RGBColor(0x2D, 0x2D, 0x2D)
MUTED  = RGBColor(0x6B, 0x72, 0x80)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GREEN  = RGBColor(0x2E, 0x8B, 0x57)
AMBER  = RGBColor(0xE0, 0x8A, 0x00)
RED    = RGBColor(0xC0, 0x39, 0x2B)
RAG = {"GREEN": GREEN, "AMBER": AMBER, "RED": RED,
       "HIGH": RED, "MEDIUM": AMBER, "LOW": GREEN}
# week-over-week trend styling: (cell color, label)
TREND = {"UP": (GREEN, "▲ Improved"), "DOWN": (RED, "▼ Slipped"),
         "SAME": (MUTED, "→ No change"), "NEW": (ACCENT, "＋ New")}

EMU_W, EMU_H = Inches(13.333), Inches(7.5)
FONT = "Segoe UI"

prs = Presentation()
prs.slide_width = EMU_W
prs.slide_height = EMU_H
BLANK = prs.slide_layouts[6]


def _set(run, size, color, bold=False, italic=False):
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = FONT


def rect(slide, x, y, w, h, color, line=None):
    from pptx.enum.shapes import MSO_SHAPE
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(0.75)
    shp.shadow.inherit = False
    return shp


def textbox(slide, x, y, w, h, lines, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT):
    """lines: list of (text, size, color, bold, italic) or list of such for paragraphs."""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Pt(4)
    tf.margin_top = tf.margin_bottom = Pt(2)
    for i, spec in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        text, size, color, bold, italic = spec
        r = p.add_run(); r.text = text
        _set(r, size, color, bold, italic)
    return tb


def header(slide, title, subtitle=None):
    rect(slide, 0, 0, EMU_W, Inches(1.05), DARK)
    rect(slide, 0, Inches(1.05), EMU_W, Inches(0.06), ACCENT)
    textbox(slide, Inches(0.55), Inches(0.18), Inches(11.5), Inches(0.55),
            [(title, 26, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
    if subtitle:
        textbox(slide, Inches(0.57), Inches(0.66), Inches(11.5), Inches(0.32),
                [(subtitle, 12, RGBColor(0xC9, 0xD6, 0xE6), False, False)], MSO_ANCHOR.MIDDLE)
    # footer
    textbox(slide, Inches(0.55), Inches(7.05), Inches(8), Inches(0.35),
            [(f"PPL CMDB-CSDM  |  {PI}  |  {WEEK_LABEL}", 9, MUTED, False, False)])


def chip(slide, x, y, label, color, w=Inches(1.0)):
    c = rect(slide, x, y, w, Inches(0.30), color)
    tf = c.text_frame; tf.word_wrap = False
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = label
    _set(r, 10, WHITE, True)
    return c


def pending_box(slide, x, y, w, h, title, body):
    """Annotated placeholder for a metric that is intentionally not yet populated."""
    rect(slide, x, y, w, h, LIGHT)
    rect(slide, x, y, Inches(0.12), h, AMBER)
    chip(slide, x + Inches(0.28), y + Inches(0.16), "PENDING DATA", AMBER, Inches(1.7))
    textbox(slide, x + Inches(2.15), y + Inches(0.13), w - Inches(2.4), Inches(0.45),
            [(title, 12.5, DARK, True, False)], MSO_ANCHOR.MIDDLE)
    textbox(slide, x + Inches(0.28), y + Inches(0.62), w - Inches(0.55), h - Inches(0.72),
            [(body, 10.5, MUTED, False, True)])


# ---- Slide 1: Title -------------------------------------------------------
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, EMU_W, EMU_H, DARK)
rect(s, 0, Inches(4.55), EMU_W, Inches(0.08), ACCENT)
textbox(s, Inches(0.8), Inches(2.0), Inches(11.7), Inches(1.0),
        [("CMDB-CSDM Delivery Status", 44, WHITE, True, False)])
textbox(s, Inches(0.82), Inches(3.05), Inches(11.7), Inches(0.6),
        [("Weekly Leadership Report", 22, RGBColor(0xC9, 0xD6, 0xE6), False, False)])
textbox(s, Inches(0.82), Inches(4.75), Inches(11.7), Inches(1.4), [
    (f"{PI}  ·  {ITERATION}", 16, WHITE, True, False),
    (WEEK_LABEL, 14, RGBColor(0xC9, 0xD6, 0xE6), False, False),
    (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
])

# ---- Slide 2: How to read -------------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "How to Read This Report", EDITION_NOTE)
textbox(s, Inches(0.55), Inches(1.4), Inches(12), Inches(0.4),
        [("Three progress lenses, refreshed every week:", 15, TEXT, True, False)])
lenses = [("PI over PI", "Are we delivering more value each Program Increment?"),
          ("Iteration over Iteration", "Is each 2-week sprint building on the last?"),
          ("Week over Week", "What concretely moved since the last report?")]
y = Inches(2.0)
for name, desc in lenses:
    rect(s, Inches(0.55), y, Inches(0.12), Inches(0.55), ACCENT)
    textbox(s, Inches(0.8), y, Inches(11.5), Inches(0.6),
            [(name, 14, ACCENT, True, False), (desc, 12, TEXT, False, False)])
    y += Inches(0.75)
# RAG legend
textbox(s, Inches(0.55), Inches(4.6), Inches(6), Inches(0.4),
        [("Status legend:", 13, TEXT, True, False)])
chip(s, Inches(0.55), Inches(5.05), "GREEN", GREEN, Inches(1.1))
textbox(s, Inches(1.8), Inches(5.05), Inches(5), Inches(0.3), [("On track", 12, TEXT, False, False)])
chip(s, Inches(0.55), Inches(5.5), "AMBER", AMBER, Inches(1.1))
textbox(s, Inches(1.8), Inches(5.5), Inches(6), Inches(0.3), [("Progressing, with watch items", 12, TEXT, False, False)])
chip(s, Inches(0.55), Inches(5.95), "RED", RED, Inches(1.1))
textbox(s, Inches(1.8), Inches(5.95), Inches(6), Inches(0.3), [("Blocked / needs intervention", 12, TEXT, False, False)])

# ---- Slide 3: Executive Summary ------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Executive Summary", ITERATION)
chip(s, Inches(0.55), Inches(1.35), OVERALL_STATUS[0], GREEN, Inches(4.4))
textbox(s, Inches(0.55), Inches(1.85), Inches(12.2), Inches(0.8),
        [(OVERALL_STATUS[1], 13, TEXT, False, False)])
textbox(s, Inches(0.55), Inches(2.75), Inches(6), Inches(0.35),
        [("Wins this period", 15, GREEN, True, False)])
yy = Inches(3.15)
for w in THIS_WEEK:
    textbox(s, Inches(0.7), yy, Inches(6.0), Inches(0.7), [("+  " + w, 11.5, TEXT, False, False)])
    yy += Inches(0.78)
textbox(s, Inches(6.9), Inches(2.75), Inches(6), Inches(0.35),
        [("Needs leadership attention", 15, RED, True, False)])
yy = Inches(3.15)
for r in RISKS[:3]:
    textbox(s, Inches(7.05), yy, Inches(5.8), Inches(0.7),
            [("!  " + r[0] + " - " + r[3], 11.5, TEXT, False, False)])
    yy += Inches(0.78)

# ---- Slide 4: Objectives Scorecard ---------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "PI-2 Objectives Scorecard", "Status explains itself  ·  Stories = moving / in-scope (provisional)")
# Executive tiles: one card per objective in a 3 x 2 grid (Variation C).
# RAG comes from the explicit per-objective value (not derived from counts),
# so Service Mapping / Regulatory stay amber despite zero "stuck" stories.
tw, th = Inches(4.0), Inches(2.55)
gx, gy = Inches(0.55), Inches(1.30)
for i, (pri, name, obj, bv, rag, note, scope, moving, stuck) in enumerate(OBJECTIVES):
    cx = gx + (i % 3) * (tw + Inches(0.3))
    cy = gy + (i // 3) * (th + Inches(0.25))
    rect(s, cx, cy, tw, th, LIGHT)
    rect(s, cx, cy, tw, Inches(0.72), RAG[rag])
    textbox(s, cx + Inches(0.2), cy + Inches(0.04), tw - Inches(0.4), Inches(0.64),
            [(f"{pri}   {name}", 11.5, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
    textbox(s, cx + Inches(0.2), cy + Inches(0.82), tw - Inches(0.4), Inches(0.8),
            [(str(scope), 44, DARK, True, False)])
    textbox(s, cx + Inches(1.4), cy + Inches(1.12), tw - Inches(1.5), Inches(0.6),
            [("stories in scope", 11, MUTED, False, False),
             (f"{moving} moving  ·  {stuck} stuck", 11, TEXT, True, False)])
    textbox(s, cx + Inches(0.2), cy + Inches(1.85), tw - Inches(0.4), Inches(0.62),
            [(note, 10, TEXT, False, False)])
textbox(s, Inches(0.55), Inches(6.72), Inches(12.25), Inches(0.35),
        [(STORY_CAVEAT, 8.5, MUTED, False, True)])

# ---- Slide 5: PI over PI --------------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Progress: PI over PI", "Are we delivering more value each Program Increment?")
x = Inches(0.55)
for pi, window, status, sub, desc in PI_PROGRESS:
    col = GREEN if status == "ACTIVE" else MUTED
    card = rect(s, x, Inches(1.5), Inches(6.0), Inches(3.4), LIGHT)
    rect(s, x, Inches(1.5), Inches(6.0), Inches(0.7), DARK)
    textbox(s, x + Inches(0.25), Inches(1.6), Inches(5.5), Inches(0.5),
            [(pi + "   " + status, 18, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
    textbox(s, x + Inches(0.25), Inches(2.4), Inches(5.5), Inches(2.3), [
        (window, 13, ACCENT, True, False),
        (sub, 12, MUTED, False, True),
        ("", 6, TEXT, False, False),
        (desc, 13, TEXT, False, False),
    ])
    x += Inches(6.3)
# #4 placeholder: PI-over-PI comparison metric (pending until PI-3 has live data)
pending_box(s, Inches(0.55), Inches(5.05), Inches(12.2), Inches(0.95),
            "PI-over-PI comparison metric",
            "Comparison basis (objectives completed / business value delivered / stories accepted per PI) "
            "to be fixed before PI-3 begins. Only PI-2 has live data today - not yet ready for relevant data.")
textbox(s, Inches(0.55), Inches(6.15), Inches(12.2), Inches(0.7),
        [("Note: " + PI_NOTE, 11, MUTED, False, True)])

# ---- Slide 6: Iteration over Iteration ------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Progress: Iteration over Iteration", "Is each 2-week sprint building on the last?")
x = Inches(0.55)
cw = Inches(4.0)
for it, window, status, theme, outcomes in ITERATIONS:
    col = GREEN if status == "ACTIVE" else ACCENT
    rect(s, x, Inches(1.45), cw, Inches(0.78), col)
    textbox(s, x + Inches(0.2), Inches(1.5), cw - Inches(0.3), Inches(0.7),
            [("Sprint " + it, 16, WHITE, True, False),
             (window + "  ·  " + status, 10, RGBColor(0xE8, 0xEE, 0xF6), False, False)], MSO_ANCHOR.MIDDLE)
    rect(s, x, Inches(2.23), cw, Inches(3.45), LIGHT)
    textbox(s, x + Inches(0.2), Inches(2.33), cw - Inches(0.3), Inches(0.4),
            [(theme, 12, ACCENT, True, True)])
    yy = Inches(2.85)
    for o in outcomes:
        textbox(s, x + Inches(0.2), yy, cw - Inches(0.35), Inches(0.8),
                [("- " + o, 10.5, TEXT, False, False)])
        yy += Inches(0.62)
    x += cw + Inches(0.3)
# #3 placeholder: quantitative iteration velocity (pending consistent ceremony capture)
pending_box(s, Inches(0.55), Inches(5.8), Inches(12.2), Inches(1.0),
            "Iteration velocity - committed vs. accepted stories",
            "Per-sprint committed -> accepted counts will quantify whether each iteration builds on the last. "
            + VELOCITY_NOTE + " Not yet ready for relevant data.")

# ---- Slide 7: Week over Week (#2 data-driven delta; #5 delivery placeholder)
s = prs.slides.add_slide(BLANK)
header(s, "Progress: Week over Week", "What changed in status since the last report?")
_rows = wow_rows()
if _rows:
    # ---- delta mode: status transitions vs the prior snapshot ----
    n = len(_rows) + 1
    tbl_h = Inches(0.45) * n
    tshape = s.shapes.add_table(n, 5, Inches(0.55), Inches(1.4), Inches(12.2), tbl_h)
    t = tshape.table
    for j, wdt in enumerate([Inches(4.6), Inches(1.6), Inches(1.6), Inches(2.2), Inches(2.2)]):
        t.columns[j].width = wdt
    for j, htxt in enumerate(["Objective", "Last week", "This week", "Δ stories", "Trend"]):
        c = t.cell(0, j); c.fill.solid(); c.fill.fore_color.rgb = DARK
        p = c.text_frame.paragraphs[0]; r = p.add_run(); r.text = htxt
        _set(r, 11, WHITE, True)
        if j >= 1:
            p.alignment = PP_ALIGN.CENTER
    for i, row in enumerate(_rows, start=1):
        tcol, tlabel = TREND[row["trend"]]
        dtext = "new" if row["d_moving"] is None else f"{row['d_moving']:+d} mv / {row['d_stuck']:+d} stk"
        vals = [row["name"], RAGWORD.get(row["last"], "—"), RAGWORD[row["this"]], dtext, tlabel]
        for j, v in enumerate(vals):
            c = t.cell(i, j); c.fill.solid()
            c.fill.fore_color.rgb = LIGHT if i % 2 else WHITE
            p = c.text_frame.paragraphs[0]; r = p.add_run(); r.text = v
            if j == 1:
                _set(r, 10.5, RAG.get(row["last"], MUTED), True); p.alignment = PP_ALIGN.CENTER
            elif j == 2:
                _set(r, 10.5, RAG[row["this"]], True); p.alignment = PP_ALIGN.CENTER
            elif j == 3:
                _set(r, 10, TEXT, False); p.alignment = PP_ALIGN.CENTER
            elif j == 4:
                c.fill.fore_color.rgb = tcol; _set(r, 10.5, WHITE, True); p.alignment = PP_ALIGN.CENTER
            else:
                _set(r, 10.5, TEXT, False)
    blocked, unblocked = wow_transitions()
    yb = Inches(1.4) + tbl_h + Inches(0.2)
    textbox(s, Inches(0.55), yb, Inches(12.2), Inches(0.8), [
        ("Newly unblocked:  " + (", ".join(unblocked) if unblocked else "none"), 11, GREEN, True, False),
        ("Newly blocked:  " + (", ".join(blocked) if blocked else "none"), 11, RED, True, False),
    ])
    pending_box(s, Inches(0.55), yb + Inches(0.95), Inches(12.2), Inches(0.9),
                "Completed / delivered this period",
                "Delivery tracking (completed & accepted stories) begins at first PROD deploy (Jun 23). "
                "Current 'moving' counts reflect activity in flight, not completion. Not yet ready for relevant data.")
else:
    # ---- baseline mode: no prior snapshot to diff against yet ----
    textbox(s, Inches(0.55), Inches(1.4), Inches(12.2), Inches(0.45),
            [("Baseline snapshot captured - this edition is the reference point.", 16, ACCENT, True, False)])
    textbox(s, Inches(0.55), Inches(1.95), Inches(12.2), Inches(0.65),
            [(WEEK_NOTE + " Status changes (▲ improved / ▼ slipped), story movement, and newly "
              "blocked/unblocked objectives will be computed automatically from next edition.",
              12, MUTED, False, True)])
    textbox(s, Inches(0.55), Inches(2.8), Inches(12.2), Inches(0.35),
            [("This week's baseline status", 13, DARK, True, False)])
    yy = Inches(3.2)
    for o in OBJECTIVES:
        chip(s, Inches(0.55), yy, RAGWORD[o[4]], RAG[o[4]], Inches(1.15))
        textbox(s, Inches(1.85), yy - Inches(0.02), Inches(8.4), Inches(0.4),
                [(f"{o[0]}  {o[1]}", 12, TEXT, False, False)], MSO_ANCHOR.MIDDLE)
        textbox(s, Inches(10.35), yy - Inches(0.02), Inches(2.45), Inches(0.4),
                [(f"{o[7]}/{o[6]} moving", 11, MUTED, False, False)], MSO_ANCHOR.MIDDLE)
        yy += Inches(0.46)
    pending_box(s, Inches(0.55), Inches(5.95), Inches(12.2), Inches(0.85),
                "Completed / delivered this period",
                "Delivery tracking (completed & accepted stories) begins at first PROD deploy (Jun 23). "
                "Current 'moving' counts reflect activity in flight, not completion. Not yet ready for relevant data.")

# ---- Slides 8-9: Deep dives ----------------------------------------------
for title, items in (DEEP_DIVE_1, DEEP_DIVE_2):
    s = prs.slides.add_slide(BLANK)
    header(s, title, "Status and detail by objective")
    yy = Inches(1.6)
    for name, rag, detail in items:
        rect(s, Inches(0.55), yy, Inches(12.2), Inches(1.45), LIGHT)
        chip(s, Inches(0.75), yy + Inches(0.2), rag, RAG[rag], Inches(1.1))
        textbox(s, Inches(2.05), yy + Inches(0.15), Inches(10.4), Inches(0.4),
                [(name, 15, DARK, True, False)])
        textbox(s, Inches(2.05), yy + Inches(0.6), Inches(10.4), Inches(0.8),
                [(detail, 12, TEXT, False, False)])
        yy += Inches(1.65)

# ---- Slide 10: Milestones -------------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Key Milestones & Upcoming Dates", "Iteration 2.3 critical path")
yy = Inches(1.5)
for date, ev in MILESTONES:
    rect(s, Inches(0.55), yy, Inches(1.9), Inches(0.55), ACCENT)
    textbox(s, Inches(0.6), yy, Inches(1.8), Inches(0.55),
            [(date, 13, WHITE, True, False)], MSO_ANCHOR.MIDDLE, PP_ALIGN.CENTER)
    rect(s, Inches(2.55), yy, Inches(10.2), Inches(0.55), LIGHT)
    textbox(s, Inches(2.75), yy, Inches(9.9), Inches(0.55),
            [(ev, 13, TEXT, False, False)], MSO_ANCHOR.MIDDLE)
    yy += Inches(0.68)

# ---- Slide 11: Risks & Asks ----------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Risks & Leadership Asks", "Where we need help to stay on track")
rows = len(RISKS) + 1
tbl_shape = s.shapes.add_table(rows, 4, Inches(0.55), Inches(1.4), Inches(12.2), Inches(4.6))
tbl = tbl_shape.table
tbl.columns[0].width = Inches(2.6)
tbl.columns[1].width = Inches(1.1)
tbl.columns[2].width = Inches(4.4)
tbl.columns[3].width = Inches(4.1)
for j, h in enumerate(["Risk", "Severity", "Detail", "Ask of Leadership"]):
    cell = tbl.cell(0, j)
    cell.fill.solid(); cell.fill.fore_color.rgb = DARK
    p = cell.text_frame.paragraphs[0]; r = p.add_run(); r.text = h
    _set(r, 12, WHITE, True)
for i, (risk, sev, detail, ask) in enumerate(RISKS, start=1):
    vals = [risk, sev, detail, ask]
    for j, v in enumerate(vals):
        cell = tbl.cell(i, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = LIGHT if i % 2 else WHITE
        p = cell.text_frame.paragraphs[0]; r = p.add_run(); r.text = v
        if j == 1:
            cell.fill.fore_color.rgb = RAG[sev]
            _set(r, 11, WHITE, True); p.alignment = PP_ALIGN.CENTER
        elif j == 0:
            _set(r, 11, DARK, True)
        else:
            _set(r, 10.5, TEXT, False)

# ---- Slide 12: What's Next ------------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "What's Next", "Looking ahead to PI-3 and the IP iteration")
yy = Inches(1.7)
for n in NEXT:
    rect(s, Inches(0.55), yy + Inches(0.05), Inches(0.12), Inches(0.5), ACCENT)
    textbox(s, Inches(0.85), yy, Inches(11.8), Inches(0.7), [(n, 14, TEXT, False, False)])
    yy += Inches(0.85)

# ---- Slide 13: Appendix ---------------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Appendix", "Story-level detail")
textbox(s, Inches(0.55), Inches(1.8), Inches(12), Inches(3), [
    ("Full traceability is maintained in the team's working notes:", 14, TEXT, True, False),
    ("", 8, TEXT, False, False),
    ("- Objectives -> Features -> Stories:  PI-2/pi2-objectives-features-stories.md", 12, ACCENT, False, False),
    ("- Activity by Iteration (2.1 / 2.2 / 2.3):  PI-2/pi2-iteration-activity.md", 12, ACCENT, False, False),
    ("- Program Backlog Review notes:  PI-2/Program-Backlog-Review/", 12, ACCENT, False, False),
    ("", 8, TEXT, False, False),
    ("This deck is regenerated weekly from build_status_deck.py.", 11, MUTED, False, True),
])

def save_safe(save_fn, path):
    """Save via save_fn(path); if the target is locked (open in PowerPoint /
    Explorer preview), write to a '-new' file instead so the run never fails."""
    try:
        save_fn(path)
        print("Saved", path)
    except PermissionError:
        base, ext = os.path.splitext(path)
        alt = base + "-new" + ext
        save_fn(alt)
        print("Target locked - saved to", alt, "(close the original, then rename)")

out_pptx = os.path.join(os.path.dirname(os.path.abspath(__file__)), EDITION + ".pptx")
save_safe(prs.save, out_pptx)

# ---------------------------------------------------------------------------
# MARKDOWN (Marp) MIRROR
# ---------------------------------------------------------------------------
def md_lines():
    L = []
    L.append("---")
    L.append("marp: true")
    L.append("theme: default")
    L.append("paginate: true")
    L.append(f"title: CMDB-CSDM Delivery Status - {WEEK_LABEL}")
    L.append("---")
    L.append("")
    # title
    L.append("<!-- _class: lead -->")
    L.append("# CMDB-CSDM Delivery Status")
    L.append("### Weekly Leadership Report")
    L.append("")
    L.append(f"**{PI} · {ITERATION}**")
    L.append(f"{WEEK_LABEL}")
    L.append(f"_{AUTHOR}_")
    L.append("")
    L.append("---")
    # how to read
    L.append("## How to Read This Report")
    L.append(f"_{EDITION_NOTE}_")
    L.append("")
    L.append("Three progress lenses, refreshed every week:")
    L.append("")
    L.append("- **PI over PI** — are we delivering more value each Program Increment?")
    L.append("- **Iteration over Iteration** — is each 2-week sprint building on the last?")
    L.append("- **Week over Week** — what concretely moved since the last report?")
    L.append("")
    L.append("**Legend:** 🟢 On track  ·  🟡 Progressing, watch items  ·  🔴 Blocked / needs intervention")
    L.append("")
    L.append("---")
    # exec summary
    L.append("## Executive Summary")
    L.append(f"### 🟢 {OVERALL_STATUS[0]}")
    L.append(OVERALL_STATUS[1])
    L.append("")
    L.append("**Wins this period**")
    for w in THIS_WEEK:
        L.append(f"- ✅ {w}")
    L.append("")
    L.append("**Needs leadership attention**")
    for r in RISKS[:3]:
        L.append(f"- ⚠️ **{r[0]}** — {r[3]}")
    L.append("")
    L.append("---")
    # scorecard
    L.append("## PI-2 Objectives Scorecard")
    L.append("")
    L.append(f"**Story coverage (provisional):** {OBJ_SCOPE} in scope · {OBJ_MOVING} moving · {OBJ_STUCK} need attention")
    L.append("")
    L.append("| Pri | Objective | BV | Stories | Status | Summary |")
    L.append("|-----|-----------|----|---------|--------|---------|")
    dot = {"GREEN": "🟢 On track", "AMBER": "🟡 Watch", "RED": "🔴 Blocked"}
    for pri, name, obj, bv, rag, note, scope, moving, stuck in OBJECTIVES:
        L.append(f"| {pri} | {name} | {bv} | {moving}/{scope} | {dot[rag]} | {note} |")
    L.append("")
    L.append(f"> _{STORY_CAVEAT}_")
    L.append("")
    L.append("---")
    # PI over PI
    L.append("## Progress: PI over PI")
    L.append("")
    L.append("| PI | Window | Status | Focus |")
    L.append("|----|--------|--------|-------|")
    for pi, window, status, sub, desc in PI_PROGRESS:
        L.append(f"| **{pi}** | {window} | {status} ({sub}) | {desc} |")
    L.append("")
    L.append(f"> _{PI_NOTE}_")
    L.append("")
    L.append("> ⏳ _**Pending (#4):** PI-over-PI comparison metric (objectives completed / BV delivered / "
             "stories accepted per PI) to be fixed before PI-3 begins - not yet ready for relevant data._")
    L.append("")
    L.append("---")
    # iteration over iteration
    L.append("## Progress: Iteration over Iteration")
    for it, window, status, theme, outcomes in ITERATIONS:
        L.append("")
        L.append(f"**Sprint {it}** — {window} · _{status}_ · {theme}")
        for o in outcomes:
            L.append(f"  - {o}")
    L.append("")
    L.append(f"> ⏳ _**Pending (#3):** iteration velocity (committed vs. accepted stories per sprint) will "
             f"quantify whether each iteration builds on the last. {VELOCITY_NOTE} Not yet ready for relevant data._")
    L.append("")
    L.append("---")
    # week over week (#2 data-driven delta; #5 delivery placeholder)
    L.append("## Progress: Week over Week")
    _wr = wow_rows()
    if _wr:
        L.append("")
        L.append("| Objective | Last week | This week | Δ stories | Trend |")
        L.append("|-----------|-----------|-----------|-----------|-------|")
        _ar = {"UP": "▲ Improved", "DOWN": "▼ Slipped", "SAME": "→ No change", "NEW": "＋ New"}
        for row in _wr:
            d = "new" if row["d_moving"] is None else f"{row['d_moving']:+d} mv / {row['d_stuck']:+d} stk"
            L.append(f"| {row['name']} | {RAGWORD.get(row['last'], '—')} | {RAGWORD[row['this']]} | {d} | {_ar[row['trend']]} |")
        _bl, _ub = wow_transitions()
        L.append("")
        L.append(f"**Newly unblocked:** {', '.join(_ub) if _ub else 'none'}  ·  **Newly blocked:** {', '.join(_bl) if _bl else 'none'}")
    else:
        L.append("")
        L.append(f"**Baseline snapshot captured.** {WEEK_NOTE} Status changes, story movement, and newly "
                 "blocked/unblocked objectives will be computed automatically from next edition.")
        L.append("")
        L.append("Baseline status this week:")
        L.append("")
        for o in OBJECTIVES:
            L.append(f"- {dot[o[4]]} **{o[1]}** — {o[7]}/{o[6]} moving")
    L.append("")
    L.append("> ⏳ _**Pending (#5 delivery):** completed/accepted tracking begins at first PROD deploy "
             "(Jun 23); current counts reflect activity, not completion._")
    L.append("")
    L.append("---")
    # deep dives
    for title, items in (DEEP_DIVE_1, DEEP_DIVE_2):
        L.append(f"## {title}")
        L.append("")
        for name, rag, detail in items:
            L.append(f"- {dot[rag]} **{name}** — {detail}")
        L.append("")
        L.append("---")
    # milestones
    L.append("## Key Milestones & Upcoming Dates")
    L.append("")
    L.append("| Date | Event |")
    L.append("|------|-------|")
    for date, ev in MILESTONES:
        L.append(f"| **{date}** | {ev} |")
    L.append("")
    L.append("---")
    # risks
    L.append("## Risks & Leadership Asks")
    L.append("")
    L.append("| Risk | Severity | Detail | Ask of Leadership |")
    L.append("|------|----------|--------|-------------------|")
    sev_dot = {"HIGH": "🔴 HIGH", "MEDIUM": "🟡 MED", "LOW": "🟢 LOW"}
    for risk, sev, detail, ask in RISKS:
        L.append(f"| **{risk}** | {sev_dot[sev]} | {detail} | {ask} |")
    L.append("")
    L.append("---")
    # whats next
    L.append("## What's Next")
    L.append("")
    for n in NEXT:
        L.append(f"- {n}")
    L.append("")
    L.append("---")
    # appendix
    L.append("## Appendix — Story-Level Detail")
    L.append("")
    L.append("- Objectives → Features → Stories: `PI-2/pi2-objectives-features-stories.md`")
    L.append("- Activity by Iteration (2.1 / 2.2 / 2.3): `PI-2/pi2-iteration-activity.md`")
    L.append("- Program Backlog Review notes: `PI-2/Program-Backlog-Review/`")
    L.append("")
    L.append("_This deck is regenerated weekly from `build_status_deck.py`._")
    L.append("")
    return "\n".join(L)

out_md = os.path.join(os.path.dirname(os.path.abspath(__file__)), EDITION + ".md")
def _write_md(p):
    with open(p, "w", encoding="utf-8") as f:
        f.write(md_lines())
save_safe(_write_md, out_md)

# ---------------------------------------------------------------------------
# PERSIST THIS WEEK'S SNAPSHOT  (#1) - keyed by EDITION, so re-runs are idempotent
# ---------------------------------------------------------------------------
HISTORY[EDITION] = CURR
with open(HISTORY_PATH, "w", encoding="utf-8") as f:
    json.dump(HISTORY, f, indent=2, ensure_ascii=False)
print(f"History updated: {HISTORY_PATH} ({len(HISTORY)} edition(s))")
