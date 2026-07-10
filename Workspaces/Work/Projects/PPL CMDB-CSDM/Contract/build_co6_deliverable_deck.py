"""
CO6 Deliverables - TEAM OVERVIEW deck (short, FYI).

Audience: the full CMDB / CSDM delivery team (onshore + offshore).
Purpose: heads-up on what's coming in Change Order #6 and how it maps to the
work we're already doing. Informational only.

Deliberately EXCLUDES contract-commercial details (fees, holdback, signature
exposure) - those are leadership material, not for a mixed delivery audience.
Keeps the DRAFT / UNSIGNED caveat because that is delivery-relevant status.

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
TITLE     = "CO6 Deliverables - Team Overview"
SUBTITLE  = "Change Order #6  ·  what's coming for CMDB / CSDM"
AUTHOR    = "Manuel Vazquez  -  Scrum Master, CMDB-CSDM"
FOOTLABEL = "PPL CMDB-CSDM  |  CO6 Deliverables (DRAFT)  |  Team FYI  -  Jul 10, 2026"

DRAFT_BANNER = ("DRAFT / UNSIGNED (3/27 working draft).  Scope, numbering and dates are "
                "TENTATIVE until the contract is executed - nothing here changes our current commitments yet.")

# Overview: (#, deliverable, type, due, PI)   type: "NEW" | "CONT"
OVERVIEW = [
    ("1",  "Network Gear Discovery",           "NEW",  "Aug 31 -> Oct 30",       "PI-3"),
    ("2",  "Service Mapping",                   "NEW",  "Aug 31 -> Oct 30",       "PI-3"),
    ("3a", "Qualys Integration",                "CONT", "Oct 27",                 "PI-3"),
    ("3b", "CMDB Governance",                   "CONT", "Jul 31",                 "PI-2"),
    ("4",  "CI Coverage - Computers",           "CONT", "Jul 31 -> Sep 30",       "PI-2/3"),
    ("5",  "CI Coverage - Servers",             "CONT", "Jul 31 -> Oct 30",       "PI-2/3"),
    ("6",  "Legacy Platform Rationalization",   "NEW",  "Aug 31 -> Oct 30",       "PI-3"),
    ("7",  "ITSM Product Management",           "NEW",  "Monthly Jul 31-Oct 30",  "PI-2/3"),
    ("8",  "ATF Strategy",                      "NEW",  "Oct 31",                 "PI-3"),
    ("9",  "Platform Support",                  "NEW",  "Monthly Aug 31-Oct 30",  "PI-3"),
]
OVERVIEW_FOOT = ("6 net-new  ·  3 continue current CO5 work (Governance, CI Coverage, Qualys).  "
                 "Draft numbers two items '3' (Qualys + CMDB Governance) - shown here as 3a / 3b.")

# Net-new: (deliverable, what it adds, due, where it stands today)
NEW_ROWS = [
    ("Network Gear Discovery",
     "Discover & populate network devices in CMDB (excl. OT); 90% coverage, business-owner validated",
     "Aug 31 -> Oct 30",
     "Scaffolding from PI-2 Obj 1 (feat 1356646; stories 1402572/574/575) - no acceptance met yet"),
    ("Service Mapping",
     "End-to-end maps for 10 priority business apps down to infra CIs; consumable in ServiceNow",
     "Aug 31 -> Oct 30",
     "Wave features 1355866/68/71 + per-app stories (WATT, Oceana, SolarWinds PoC 1431652); 10-app target is new"),
    ("Legacy Platform Rationalization",
     "Analysis + migration plan: iTeam -> DISCO / Cherwell -> AIM (Cherwell/AIM 'if applicable')",
     "Aug 31 -> Oct 30",
     "Only iTeam import 1452028 today - no analysis/plan stories yet"),
    ("ITSM Product Management",
     "New ITSM Product Owner role + ITSM workstream (outside CMDB)",
     "Monthly Jul 31 -> Oct 30",
     "No stories; owner TBD"),
    ("ATF Strategy",
     "Plan for Automated Test Framework rollout across in-prod ServiceNow capabilities",
     "Oct 31",
     "Greenfield - no stories"),
    ("Platform Support",
     "Dedicated BAU / DevOps team; ~40 hrs of stories per week per member",
     "Monthly Aug 31 -> Oct 30",
     "No stories; team size TBD"),
]
NEW_FOOT = ("Net-new is not free:  ITSM PM and Platform Support are ongoing-capacity commitments "
            "(~40 hrs/wk per person), not finite deliverables - they need people, not just backlog.  "
            "#1 and #2 have story scaffolding from PI-2 objectives but no contractual acceptance met yet.")

# Continuing: (workstream, what changes in CO6, new date, current stories)
CONT_ROWS = [
    ("CMDB Governance\n(was CO5 D1)",
     "Data dictionary now includes Databases; Data Cert pilot expands from Business-App-only to ALL CI classes + KB; ESS-02; SOX BA review",
     "Jul 31\n(+1 mo)",
     "Data Cert 1247179 / 1402727 / 1402958 ; ESS-02 spike 1420244 ; SOX 1438967 / 1455827"),
    ("CI Coverage - Computers\n(was CO5 D2.1)",
     "SCCM/Discovery precedence + bulk life-cycle; 90% of devices managed",
     "Jul 31 ->\nSep 30",
     "SCCM Computer 1348712/16/17/15 ; Computer Class 1354794"),
    ("CI Coverage - Servers\n(was CO5 D2.2/2.3)",
     "SCCM/Discovery precedence; enhanced DB Discovery (MS-SQL / Oracle); 90% of non-NERC-CIP servers",
     "Jul 31 ->\nOct 30",
     "SCCM Server 1356826 (1403759/60/62/63) ; creds 1444864"),
    ("Qualys Integration\n(was CO5 D3)",
     "Escalates from 'evaluate one integration' to a full one-way Qualys -> ServiceNow feed, deployed to PROD",
     "Oct 27",
     "Stream C 1428703 / 1428704 (currently blocked) ; spike 1234585"),
]
CONT_FOOT = ("The hard 90% coverage targets get real PI-3 runway (Sep 30 / Oct 30) instead of a single 6/30 cliff.  "
             "Foundation work (Governance, precedence) is dated Jul 31 - it lands in PI-2 Iter 2.5/2.6, so it needs "
             "to be substantially done by early PI-2 end, not 'sometime in July.'")

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
     "ITSM Product Management & Platform Support - monthly acceptance",
     "PI-2 tail -> PI-3"),
]

# What this means for us (FYI close)
TAKEAWAYS = [
    ("Draft only - nothing committed yet.",
     "CO6 is unsigned (3/27 draft). Treat scope and dates as tentative; our current commitments don't change until it's executed."),
    ("Most of it is work we're already doing.",
     "Governance, CI Coverage (Computers/Servers), Service Mapping and Network Gear are the same threads you're on now - CO6 just formalizes them with dates."),
    ("Four things are brand new for PI-3 planning.",
     "Legacy Platform Rationalization, ITSM Product Management, ATF Strategy and Platform Support - we'll story-out and staff these at PI-3 planning."),
    ("Two are standing commitments, not projects.",
     "ITSM PM and Platform Support (BAU) are ongoing capacity (~40 hrs/wk per person) - they need people assigned, not just a backlog."),
    ("The hard coverage targets get real runway.",
     "90% coverage moves to Sep 30 / Oct 30 in PI-3 - no single 6/30 cliff."),
    ("Questions?",
     "Source is the 3/27 draft. Jordan Yung is the CO6 SME; Joe Dames owns governance scope. Flag anything unclear to Manny."),
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
SLATE  = RGBColor(0x5B, 0x6B, 0x7B)   # "Continues" type marker
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
textbox(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.1),
        [(TITLE, 42, WHITE, True, False)])
textbox(s, Inches(0.82), Inches(2.8), Inches(11.7), Inches(0.6),
        [(SUBTITLE, 20, RGBColor(0xC9, 0xD6, 0xE6), False, False)])
# tentative flag on the title
rect(s, Inches(0.82), Inches(3.6), Inches(5.6), Inches(0.5), RGBColor(0x7A, 0x4F, 0x10), line=AMBER)
textbox(s, Inches(0.95), Inches(3.62), Inches(5.4), Inches(0.46),
        [("DRAFT / UNSIGNED  -  tentative until executed", 12, RGBColor(0xFF, 0xE6, 0xC2), True, False)],
        MSO_ANCHOR.MIDDLE)
textbox(s, Inches(0.82), Inches(4.75), Inches(11.7), Inches(1.5), [
    ("9 deliverables  ·  6 net-new  ·  3 continue current CO5 work", 16, WHITE, True, False),
    ("Proposed term: Jul 1 - Oct 30, 2026  (spans the tail of PI-2 + all of PI-3)", 14, RGBColor(0xC9, 0xD6, 0xE6), False, False),
    (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
])

# ---- Slide 2: Overview - all 9 -------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "CO6 Deliverables - All 9 at a Glance",
       "6 net-new  ·  3 continue current CO5 work  ·  staged monthly acceptance")
# draft banner
rect(s, Inches(0.55), Inches(1.22), Inches(12.2), Inches(0.5), RGBColor(0xFB, 0xEE, 0xDB), line=AMBER)
textbox(s, Inches(0.72), Inches(1.24), Inches(11.9), Inches(0.46),
        [(DRAFT_BANNER, 10.5, RGBColor(0x7A, 0x4F, 0x10), True, False)], MSO_ANCHOR.MIDDLE)
rows = len(OVERVIEW) + 1
tshape = s.shapes.add_table(rows, 5, Inches(0.55), Inches(1.9), Inches(12.2), Inches(4.5))
t = tshape.table
for j, wdt in enumerate([Inches(0.7), Inches(4.3), Inches(1.9), Inches(3.4), Inches(1.9)]):
    t.columns[j].width = wdt
for j, h in enumerate(["#", "Deliverable", "Type", "Due (draft)", "PI"]):
    cell(t, 0, j, h, 11.5, WHITE, True, PP_ALIGN.LEFT if j == 1 else PP_ALIGN.CENTER, DARK)
for i, (num, name, typ, due, pi) in enumerate(OVERVIEW, start=1):
    fill = LIGHT if i % 2 else WHITE
    tfill = ACCENT if typ == "NEW" else SLATE
    tword = "New" if typ == "NEW" else "Continues"
    cell(t, i, 0, num, 11, MUTED, True, PP_ALIGN.CENTER, fill)
    cell(t, i, 1, name, 11.5, DARK, True, PP_ALIGN.LEFT, fill)
    cell(t, i, 2, tword, 10.5, WHITE, True, PP_ALIGN.CENTER, tfill)
    cell(t, i, 3, due, 11, TEXT, False, PP_ALIGN.CENTER, fill)
    cell(t, i, 4, pi, 11, TEXT, True, PP_ALIGN.CENTER, fill)
textbox(s, Inches(0.55), Inches(6.5), Inches(12.2), Inches(0.55),
        [(OVERVIEW_FOOT, 10.5, TEXT, False, False)])

# ---- Slide 3: The 6 net-new ----------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "The 6 Net-New Deliverables",
       "Brand-new scope with no CO5 antecedent - mostly planned & staffed at PI-3")
rows = len(NEW_ROWS) + 1
tshape = s.shapes.add_table(rows, 4, Inches(0.55), Inches(1.3), Inches(12.2), Inches(4.5))
t = tshape.table
for j, wdt in enumerate([Inches(2.7), Inches(4.9), Inches(1.9), Inches(2.7)]):
    t.columns[j].width = wdt
for j, h in enumerate(["Deliverable", "What it adds", "Due (draft)", "Where it stands today"]):
    cell(t, 0, j, h, 11, WHITE, True, PP_ALIGN.LEFT if j != 2 else PP_ALIGN.CENTER, DARK)
for i, (name, adds, due, stands) in enumerate(NEW_ROWS, start=1):
    fill = LIGHT if i % 2 else WHITE
    cell(t, i, 0, name, 10.5, DARK, True, PP_ALIGN.LEFT, fill)
    cell(t, i, 1, adds, 9.5, TEXT, False, PP_ALIGN.LEFT, fill)
    cell(t, i, 2, due, 9.5, ACCENT, True, PP_ALIGN.CENTER, fill)
    cell(t, i, 3, stands, 9, TEXT, False, PP_ALIGN.LEFT, fill)
rect(s, Inches(0.55), Inches(5.95), Inches(12.2), Inches(0.9), RGBColor(0xFB, 0xEE, 0xDB), line=AMBER)
textbox(s, Inches(0.72), Inches(6.0), Inches(11.9), Inches(0.82),
        [(NEW_FOOT, 10, RGBColor(0x5A, 0x4A, 0x2A), False, False)], MSO_ANCHOR.MIDDLE)

# ---- Slide 4: The 3 continuing workstreams -------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Continuing From CO5 - Re-Baselined & Escalated",
       "These continue work we're already doing, with new (later) dates")
rows = len(CONT_ROWS) + 1
tshape = s.shapes.add_table(rows, 4, Inches(0.55), Inches(1.3), Inches(12.2), Inches(4.2))
t = tshape.table
for j, wdt in enumerate([Inches(2.4), Inches(4.9), Inches(1.6), Inches(3.3)]):
    t.columns[j].width = wdt
for j, h in enumerate(["Workstream", "What changes in CO6", "New date", "Current stories"]):
    cell(t, 0, j, h, 11, WHITE, True, PP_ALIGN.LEFT if j != 2 else PP_ALIGN.CENTER, DARK)
for i, (name, chg, date, stories) in enumerate(CONT_ROWS, start=1):
    fill = LIGHT if i % 2 else WHITE
    cell(t, i, 0, name.split("\n"), 10, DARK, True, PP_ALIGN.LEFT, fill)
    cell(t, i, 1, chg, 9.5, TEXT, False, PP_ALIGN.LEFT, fill)
    cell(t, i, 2, date.split("\n"), 9.5, GREEN, True, PP_ALIGN.CENTER, fill)
    cell(t, i, 3, stories, 9, TEXT, False, PP_ALIGN.LEFT, fill)
rect(s, Inches(0.55), Inches(5.7), Inches(12.2), Inches(1.1), RGBColor(0xE6, 0xF3, 0xEC), line=GREEN)
textbox(s, Inches(0.72), Inches(5.78), Inches(11.9), Inches(0.98),
        [(CONT_FOOT, 10, RGBColor(0x1E, 0x5A, 0x38), False, False)], MSO_ANCHOR.MIDDLE)

# ---- Slide 5: Timeline ---------------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "CO6 Timeline - Where It Lands",
       "Spans the tail of PI-2 + all of PI-3  ·  staged monthly acceptance")

# --- compact Gantt ---
AXL, AXR = 2.0, 12.6
M0, M1 = 6, 11   # Jun .. Nov


def px(m):
    return Inches(AXL + (m - M0) / (M1 - M0) * (AXR - AXL))


GRID_TOP, GRID_H = 1.3, 1.55
for m, lbl in [(6, "Jun"), (7, "Jul"), (8, "Aug"), (9, "Sep"), (10, "Oct"), (11, "Nov")]:
    rect(s, px(m), Inches(GRID_TOP), Pt(1), Inches(GRID_H), RGBColor(0xDD, 0xE3, 0xEA))
    textbox(s, px(m) - Inches(0.3), Inches(GRID_TOP + GRID_H + 0.02), Inches(0.6), Inches(0.25),
            [(lbl, 9, MUTED, False, False)], align=PP_ALIGN.CENTER)
# row labels
textbox(s, Inches(0.55), Inches(GRID_TOP), Inches(1.4), Inches(GRID_H),
        [("Contract /", 9, MUTED, True, False), ("PI window", 9, MUTED, True, False)], MSO_ANCHOR.MIDDLE)
BARS = [
    ("CO5 (ends Jun 30)",     6.0,   6.967,  GREY,   WHITE),
    ("CO6   Jul 1 - Oct 30",  7.0,   10.935, ACCENT, WHITE),
    ("PI-2  (-> Aug 4)",      6.0,   8.097,  PI2C,   WHITE),
    ("PI-3  Aug 5 - Oct 27",  8.129, 10.839, PI3C,   WHITE),
]
bh, gap = 0.30, 0.075
yy = GRID_TOP + 0.06
for lbl, ms, me, col, tc in BARS:
    x1, x2 = px(ms), px(me)
    rect(s, x1, Inches(yy), x2 - x1, Inches(bh), col)
    textbox(s, x1 + Inches(0.08), Inches(yy), (x2 - x1) - Inches(0.12), Inches(bh),
            [(lbl, 9.5, tc, True, False)], MSO_ANCHOR.MIDDLE)
    yy += bh + gap

# --- milestone table ---
rows = len(MILESTONES) + 1
tshape = s.shapes.add_table(rows, 3, Inches(0.55), Inches(3.45), Inches(12.2), Inches(3.0))
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

# ---- Slide 6: What this means for us -------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "What This Means for Us",
       "FYI - nothing here is committed until CO6 is signed")
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
