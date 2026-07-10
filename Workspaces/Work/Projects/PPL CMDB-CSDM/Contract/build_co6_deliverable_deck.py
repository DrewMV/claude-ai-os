"""
CO6 Deliverables - TEAM FOCUS deck (short, work-oriented).

Audience: the CMDB / CSDM Development + supporting roles.
Purpose: what we deliver and by when - and what each thread needs to focus on.
Ordered by due date (soonest first) so it reads as a priority list.

NO contract-commercial or contract-status framing: no fees, no holdback, no
CO5-vs-CO6 comparison, no re-baseline/escalation language, no draft-numbering.
One neutral 'planning view - dates firm up at PI-3 planning' line only.

Theme mirrors build_co5_deliverable_deck.py so the decks look like a set.
Single source of truth for this deck. Edit CONTENT, then run:
    python build_co6_deliverable_deck.py
Output:  CO6-Deliverables-<EDITION>.pptx

Source: CO6-DRAFT-3.27-unsigned.docx  ·  ../co6-deliverable-tracking.md
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------------------------------------------------------------------------
# CONTENT
# ---------------------------------------------------------------------------
EDITION   = "2026-07-10"
TITLE     = "CO6 Deliverables - Team Focus"
SUBTITLE  = "Deliverables, dates & where to focus  ·  for Development + supporting roles"
AUTHOR    = "Manuel Vazquez  -  Scrum Master, CMDB-CSDM"
FOOTLABEL = "PPL CMDB-CSDM  |  CO6 Deliverables  |  Team Focus  -  Jul 10, 2026"
PLANNING_NOTE = "Planning view - dates & scope firm up at PI-3 planning."

# Deliverables (date-ordered). (name, due, pi, focus, is_support)
DELIVERABLES = [
    ("CMDB Governance", "Jul 31", "PI-2",
     "Data dictionary incl. Databases; Data Certification for ALL CI classes + KB articles; ESS-02; SOX BA review",
     False),
    ("CI Coverage - Computers", "Jul 31 -> Sep 30", "PI-2/3",
     "SCCM/Discovery precedence + bulk life-cycle; 90% of devices managed",
     False),
    ("CI Coverage - Servers", "Jul 31 -> Oct 30", "PI-2/3",
     "SCCM/Discovery precedence; enhanced DB Discovery (MS-SQL/Oracle); 90% of non-NERC-CIP servers",
     False),
    ("Network Gear Discovery", "Aug 31 -> Oct 30", "PI-3",
     "Credentials / SNMP (excl. OT); discovery schedules; mandatory attributes; 90% coverage, owner-validated",
     False),
    ("Service Mapping", "Aug 31 -> Oct 30", "PI-3",
     "End-to-end maps for 10 priority apps down to infra CIs; owner-validated; consumable in ServiceNow",
     False),
    ("Legacy Platform Rationalization", "Aug 31 -> Oct 30", "PI-3",
     "Analysis + migration plan: iTeam -> DISCO / Cherwell -> AIM",
     False),
    ("Qualys Integration", "Oct 27", "PI-3",
     "One-way Qualys -> ServiceNow feed; configured, tested, deployed to PROD",
     False),
    ("ATF Strategy", "Oct 31", "PI-3",
     "Plan for Automated Test Framework rollout across in-prod ServiceNow capabilities",
     False),
    ("ITSM Product Management", "Monthly", "PI-2/3",
     "Separate ITSM lane (Product Owner role) - outside core CMDB delivery",
     True),
    ("Platform Support", "Monthly", "PI-3",
     "Standing BAU / DevOps support - ongoing capacity, not a finite deliverable",
     True),
]
DELIVERABLES_FOOT = ("Ordered by due date.  Bottom two are standing PO / BAU lanes - separate from core CMDB delivery.  "
                     + PLANNING_NOTE)

# In-flight now: (focus area, what to do next, current stories)
INFLIGHT = [
    ("CMDB Governance",
     "Roll Data Certification out to all CI classes + KB; close data dictionary incl. Databases; ESS-02; SOX BA review",
     "Data Cert 1247179 / 1402727 / 1402958  ·  ESS-02 spike 1420244  ·  SOX 1438967 / 1455827"),
    ("CI Coverage - Computers",
     "Land SCCM/Discovery precedence + bulk life-cycle; stand up the 90% coverage measurement",
     "SCCM Computer 1348712 / 16 / 17 / 15  ·  Computer Class 1354794"),
    ("CI Coverage - Servers",
     "Land server precedence; enhanced DB Discovery (MS-SQL / Oracle); stand up 90% measurement",
     "SCCM Server 1356826 (1403759 / 60 / 62 / 63)  ·  creds 1444864"),
    ("Service Mapping",
     "Build maps for the 10 priority apps; get app-owner validation; make consumable in SNOW",
     "Wave 1355866 / 68 / 71  ·  per-app: WATT, Oceana, SolarWinds PoC 1431652"),
    ("Network Gear Discovery",
     "Fix creds / SNMP (excl. OT); activate discovery schedules; populate mandatory attributes",
     "1356646  ·  1402572 / 574 / 575  ·  creds 1444864 / 1459721  ·  dep 1383487"),
    ("Qualys Integration",
     "Clear the plugin blocker; configure + test the one-way feed; deploy to PROD",
     "1428703 / 1428704 (blocked)  ·  data-scope spike 1234585"),
]
INFLIGHT_FOOT = ("These are the threads already in motion - the same work you're on now.  "
                 "Legacy Platform Rationalization and ATF Strategy are greenfield (no stories yet) - scoped at PI-3 planning.")

# Timeline milestones: (when, what's due, lands in)
MILESTONES = [
    ("Jul 31",
     "CMDB Governance (data dictionary incl. Databases; Data Cert all CI classes; ESS-02; SOX)  ·  CI Coverage foundation (Computers & Servers precedence)",
     "PI-2 Iter 2.5 / 2.6 (IP)"),
    ("Aug 31",
     "Network Gear (creds & schedules)  ·  Service Mapping (initial maps)  ·  Legacy Platform (analysis) - staged",
     "PI-3"),
    ("Sep 30",
     "CI Coverage - Computers 90% managed  ·  Network Gear mandatory attributes",
     "PI-3"),
    ("Oct 27",
     "Qualys -> ServiceNow live in PROD",
     "PI-3"),
    ("Oct 30",
     "CI Coverage - Servers 90%  ·  Network Gear 90%  ·  Service Mapping (10 apps)  ·  Legacy Platform (migration plan)",
     "PI-3"),
    ("Oct 31",
     "ATF Strategy (rollout plan)",
     "PI-3"),
    ("Ongoing",
     "ITSM Product Management & Platform Support - monthly",
     "PI-2 tail -> PI-3"),
]

# Where to focus (close)
TAKEAWAYS = [
    ("Focus first: the Jul 31 items.",
     "CMDB Governance and CI Coverage foundation (Computers & Servers precedence) are due first and land in PI-2 - keep these moving now."),
    ("Biggest PI-3 build: Discovery + Mapping.",
     "Network Gear, Service Mapping and the 90% coverage targets (Sep 30 / Oct 30) are the bulk of the work - discovery, credentials, and app-owner validation."),
    ("Unblock Qualys early.",
     "One-way feed to PROD by Oct 27 - the plugin blocker needs clearing before the build can finish."),
    ("New to plan at PI-3 planning.",
     "Legacy Platform Rationalization and ATF Strategy are greenfield - no stories yet; we scope and staff these at planning."),
    ("Supporting lanes stand up separately.",
     "ITSM Product Management and Platform Support are PO / BAU capacity, not core CMDB dev - flagged so they're on the radar."),
    ("Questions?",
     "Jordan Yung is the CO6 SME; Joe Dames owns governance scope. Flag anything unclear to Manny."),
]

# ---------------------------------------------------------------------------
# THEME  (mirrors build_co5_deliverable_deck.py)
# ---------------------------------------------------------------------------
DARK   = RGBColor(0x1F, 0x3A, 0x5F)
ACCENT = RGBColor(0x2E, 0x6D, 0xB4)
LIGHT  = RGBColor(0xF4, 0xF6, 0xF9)
TEXT   = RGBColor(0x2D, 0x2D, 0x2D)
MUTED  = RGBColor(0x6B, 0x72, 0x80)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GREEN  = RGBColor(0x2E, 0x8B, 0x57)
AMBER  = RGBColor(0xE0, 0x8A, 0x00)
RED    = RGBColor(0xC0, 0x39, 0x2B)
GREY   = RGBColor(0x8A, 0x92, 0x9E)
PALE   = RGBColor(0xEC, 0xEE, 0xF1)   # supporting-lane rows
PI2C   = RGBColor(0x6E, 0x88, 0xAE)   # PI-2 timeline bar
PI3C   = GREEN                        # PI-3 timeline bar

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
    textbox(slide, Inches(0.55), Inches(0.18), Inches(12.2), Inches(0.55),
            [(title, 26, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
    if subtitle:
        textbox(slide, Inches(0.57), Inches(0.66), Inches(12.2), Inches(0.32),
                [(subtitle, 12, RGBColor(0xC9, 0xD6, 0xE6), False, False)], MSO_ANCHOR.MIDDLE)
    textbox(slide, Inches(0.55), Inches(7.08), Inches(10), Inches(0.32),
            [(FOOTLABEL, 9, MUTED, False, False)])


def cell(t, i, j, lines, size, color, bold=False, align=PP_ALIGN.LEFT, fill=None):
    c = t.cell(i, j)
    if fill is not None:
        c.fill.solid(); c.fill.fore_color.rgb = fill
    tf = c.text_frame; tf.word_wrap = True
    if isinstance(lines, str):
        lines = [lines]
    for k, ln in enumerate(lines):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = ln
        _set(r, size, color, bold)


# ---- Slide 1: Title -------------------------------------------------------
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, EMU_W, EMU_H, DARK)
rect(s, 0, Inches(4.55), EMU_W, Inches(0.08), ACCENT)
textbox(s, Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.1),
        [(TITLE, 42, WHITE, True, False)])
textbox(s, Inches(0.82), Inches(2.9), Inches(11.7), Inches(0.6),
        [(SUBTITLE, 20, RGBColor(0xC9, 0xD6, 0xE6), False, False)])
textbox(s, Inches(0.82), Inches(4.75), Inches(11.7), Inches(1.5), [
    ("What we deliver, by when, and where to focus", 16, WHITE, True, False),
    ("Delivery window: Jul 1 - Oct 30, 2026  (tail of PI-2 + all of PI-3)", 14, RGBColor(0xC9, 0xD6, 0xE6), False, False),
    (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
])
textbox(s, Inches(0.82), Inches(6.55), Inches(11.7), Inches(0.32),
        [(PLANNING_NOTE, 11, RGBColor(0x7F, 0x8C, 0xA6), False, True)])

# ---- Slide 2: Deliverables & dates ---------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Deliverables & Dates", "Ordered by due date - soonest first")
rows = len(DELIVERABLES) + 1
tshape = s.shapes.add_table(rows, 4, Inches(0.55), Inches(1.4), Inches(12.2), Inches(4.7))
t = tshape.table
for j, wdt in enumerate([Inches(3.0), Inches(2.0), Inches(0.9), Inches(6.3)]):
    t.columns[j].width = wdt
for j, h in enumerate(["Deliverable", "Due", "PI", "What we focus on"]):
    cell(t, 0, j, h, 11.5, WHITE, True, PP_ALIGN.LEFT if j in (0, 3) else PP_ALIGN.CENTER, DARK)
for i, (name, due, pi, focus, sup) in enumerate(DELIVERABLES, start=1):
    fill = PALE if sup else (LIGHT if i % 2 else WHITE)
    cell(t, i, 0, name, 10.5, MUTED if sup else DARK, True, PP_ALIGN.LEFT, fill)
    cell(t, i, 1, due, 10, ACCENT if not sup else MUTED, True, PP_ALIGN.CENTER, fill)
    cell(t, i, 2, pi, 10, TEXT, True, PP_ALIGN.CENTER, fill)
    cell(t, i, 3, focus, 9.5, TEXT if not sup else MUTED, False, PP_ALIGN.LEFT, fill)
textbox(s, Inches(0.55), Inches(6.25), Inches(12.2), Inches(0.6),
        [(DELIVERABLES_FOOT, 10, TEXT, False, False)])

# ---- Slide 3: In-flight now ----------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "In-Flight Now - Current Work & Stories",
       "The threads already in motion - what to do next, and the ADO items")
rows = len(INFLIGHT) + 1
tshape = s.shapes.add_table(rows, 3, Inches(0.55), Inches(1.4), Inches(12.2), Inches(4.3))
t = tshape.table
for j, wdt in enumerate([Inches(3.0), Inches(5.5), Inches(3.7)]):
    t.columns[j].width = wdt
for j, h in enumerate(["Focus area", "What to do next", "Current stories"]):
    cell(t, 0, j, h, 11.5, WHITE, True, PP_ALIGN.LEFT, DARK)
for i, (area, todo, stories) in enumerate(INFLIGHT, start=1):
    fill = LIGHT if i % 2 else WHITE
    cell(t, i, 0, area, 10.5, DARK, True, PP_ALIGN.LEFT, fill)
    cell(t, i, 1, todo, 9.5, TEXT, False, PP_ALIGN.LEFT, fill)
    cell(t, i, 2, stories, 9, TEXT, False, PP_ALIGN.LEFT, fill)
rect(s, Inches(0.55), Inches(5.9), Inches(12.2), Inches(0.85), RGBColor(0xE9, 0xF0, 0xF8), line=ACCENT)
textbox(s, Inches(0.72), Inches(5.96), Inches(11.9), Inches(0.76),
        [(INFLIGHT_FOOT, 10, DARK, False, False)], MSO_ANCHOR.MIDDLE)

# ---- Slide 4: Timeline ---------------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Timeline - Where It Lands",
       "Tail of PI-2 + all of PI-3  ·  staged monthly acceptance")

AXL, AXR = 2.0, 12.6
M0, M1 = 6, 11   # Jun .. Nov


def px(m):
    return Inches(AXL + (m - M0) / (M1 - M0) * (AXR - AXL))


GRID_TOP, GRID_H = 1.3, 1.35
for m, lbl in [(6, "Jun"), (7, "Jul"), (8, "Aug"), (9, "Sep"), (10, "Oct"), (11, "Nov")]:
    rect(s, px(m), Inches(GRID_TOP), Pt(1), Inches(GRID_H), RGBColor(0xDD, 0xE3, 0xEA))
    textbox(s, px(m) - Inches(0.3), Inches(GRID_TOP + GRID_H + 0.02), Inches(0.6), Inches(0.25),
            [(lbl, 9, MUTED, False, False)], align=PP_ALIGN.CENTER)
textbox(s, Inches(0.55), Inches(GRID_TOP), Inches(1.4), Inches(GRID_H),
        [("Windows", 9, MUTED, True, False)], MSO_ANCHOR.MIDDLE)
BARS = [
    ("Delivery window   Jul 1 - Oct 30", 7.0,   10.935, ACCENT, WHITE),
    ("PI-2  (-> Aug 4)",                 6.0,   8.097,  PI2C,   WHITE),
    ("PI-3  Aug 5 - Oct 27",             8.129, 10.839, PI3C,   WHITE),
]
bh, gap = 0.32, 0.085
yy = GRID_TOP + 0.06
for lbl, ms, me, col, tc in BARS:
    x1, x2 = px(ms), px(me)
    rect(s, x1, Inches(yy), x2 - x1, Inches(bh), col)
    textbox(s, x1 + Inches(0.08), Inches(yy), (x2 - x1) - Inches(0.12), Inches(bh),
            [(lbl, 9.5, tc, True, False)], MSO_ANCHOR.MIDDLE)
    yy += bh + gap

rows = len(MILESTONES) + 1
tshape = s.shapes.add_table(rows, 3, Inches(0.55), Inches(3.35), Inches(12.2), Inches(3.1))
t = tshape.table
for j, wdt in enumerate([Inches(1.5), Inches(7.9), Inches(2.8)]):
    t.columns[j].width = wdt
for j, h in enumerate(["When", "What's due", "Lands in"]):
    cell(t, 0, j, h, 11, WHITE, True, PP_ALIGN.LEFT if j == 1 else PP_ALIGN.CENTER, DARK)
for i, (when, what, lands) in enumerate(MILESTONES, start=1):
    fill = LIGHT if i % 2 else WHITE
    cell(t, i, 0, when, 10.5, DARK, True, PP_ALIGN.CENTER, fill)
    cell(t, i, 1, what, 9, TEXT, False, PP_ALIGN.LEFT, fill)
    cell(t, i, 2, lands, 9.5, ACCENT, True, PP_ALIGN.CENTER, fill)

# ---- Slide 5: Where to focus ---------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Where to Focus", "Priorities for Development + supporting roles")
yy = 1.4
for head, body in TAKEAWAYS:
    rect(s, Inches(0.55), Inches(yy + 0.04), Inches(0.12), Inches(0.62), ACCENT)
    textbox(s, Inches(0.82), Inches(yy), Inches(11.9), Inches(0.32),
            [(head, 13.5, DARK, True, False)])
    textbox(s, Inches(0.82), Inches(yy + 0.34), Inches(11.9), Inches(0.5),
            [(body, 11, TEXT, False, False)])
    yy += 0.92


def save_safe(path):
    try:
        prs.save(path); print("Saved", path)
    except PermissionError:
        base, ext = os.path.splitext(path)
        alt = base + "-new" + ext
        prs.save(alt); print("Target locked - saved to", alt)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CO6-Deliverables-" + EDITION + ".pptx")
save_safe(out)
print("Slides:", len(prs.slides._sldIdLst))
