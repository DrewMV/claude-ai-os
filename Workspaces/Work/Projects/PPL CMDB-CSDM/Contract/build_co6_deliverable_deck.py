"""
CO6 Deliverables - TEAM FOCUS deck (work-oriented, with per-deliverable detail).

Audience: the CMDB / CSDM Development + supporting roles.
Purpose: what we deliver and by when - plus a detail slide per deliverable
(what "done" looks like, scope in/out, current stories, watch-outs).

NO contract-commercial or contract-status framing: no fees, no holdback, no
CO5-vs-CO6 comparison, no re-baseline/escalation language, no draft-numbering.
One neutral 'planning view - dates firm up at PI-3 planning' line only.

Structure:
    1  Title
    2  Deliverables & Dates (at-a-glance index)
    3-10  Deliverable detail (8 core, one each)
    11  Supporting lanes (ITSM PM + Platform Support)
    12  Timeline
    13  Where to focus

Theme mirrors build_co5_deliverable_deck.py so the decks look like a set.
Single source of truth. Edit CONTENT, then run:
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

# Deliverables index (date-ordered). (name, due, pi, focus, is_support)
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

# Per-deliverable detail (8 core). Each: name, due, pi, summary, done[], in_scope[], out_scope[], stories[], watch[]
DETAILS = [
    dict(
        name="CMDB Governance", due="Jul 31", pi="PI-2",
        summary="Governance foundation: data dictionary, data certification, ESS-02, and SOX Business App review.",
        done=[
            "Class attributes / data dictionary defined for all in-scope CI classes, incl. Databases",
            "Data Certification live for ALL CI classes (not just Business Apps), with KB articles",
            "ESS-02 alignment with Cyber Security & Compliance addressed",
            "SOX Business Apps correctly identified with update-rights controls",
        ],
        in_scope=[
            "Servers, Computers, Business Apps, Databases data dictionary",
            "Data Cert: process, intake, pilot, KB articles",
            "ESS-02 policy / CMDB alignment; SOX BA identification + access governance",
        ],
        out_scope=["NERC / CIP compliance indicators (separate stream)"],
        stories=[
            "Data Cert: 1247179 pilot  ·  1402727 dashboard (PROD)  ·  1402958 planning  ·  1435307 pilot changes",
            "ESS-02: spike 1420244 (analysis)",
            "SOX: 1438967 (closed)  ·  1455827 ownership-change notify",
            "Databases data dictionary - no story yet",
        ],
        watch=[
            "Databases class has no data-dictionary story yet - needs creating",
            "KB / user-doc articles have no owner - confirm before sign-off",
            "SOX only - NERC / CIP explicitly excluded",
        ],
    ),
    dict(
        name="CI Coverage - Computers", due="Jul 31 -> Sep 30", pi="PI-2 / PI-3",
        summary="SCCM/Discovery precedence, bulk life-cycle, and 90% of computers managed.",
        done=[
            "SCCM/Discovery data precedence reconciled and applied",
            "Bulk Life Cycle Stage & Status updates applied",
            "90% of computer devices managed (coverage validated)",
        ],
        in_scope=[
            "Physical + virtual computers",
            "Precedence reconciliation; bulk life-cycle; coverage measurement",
        ],
        out_scope=["Life-cycle process definition (owned by Asset Management)"],
        stories=[
            "SCCM Computer: 1348712 / 16 / 17 (resolved)  ·  1348715 last-seen (validation)",
            "Computer Class 1354794  ·  1402790 retired lifecycle (closed)",
            "90% coverage measurement - no story yet",
        ],
        watch=[
            "90% coverage has no measurement story - stand it up",
            "Life-cycle process depends on the Asset Management team",
            "Only on-network devices discovered - hard to prove the physical-device total",
        ],
    ),
    dict(
        name="CI Coverage - Servers", due="Jul 31 -> Oct 30", pi="PI-2 / PI-3",
        summary="Server precedence, enhanced MS-SQL / Oracle discovery, and 90% of non-NERC-CIP servers.",
        done=[
            "SCCM/Discovery precedence reconciled and applied for servers",
            "Enhanced Discovery working for MS-SQL & Oracle databases",
            "90% of non-NERC-CIP servers discovered",
        ],
        in_scope=["Server precedence; MS-SQL / Oracle discovery; coverage measurement"],
        out_scope=[
            "SOX indicators (manually maintained - excluded from automation)",
            "NERC / CIP servers (excluded from the 90% target)",
        ],
        stories=[
            "SCCM Server 1356826 (1403759 / 60 / 62 / 63 - validation)",
            "Credentials 1444864 (validation; child tasks active)  ·  1459721 SNMP / MID",
            "90% coverage measurement - no story yet",
        ],
        watch=[
            "Credential distribution to target CIs - no scalable solution yet (gates servers + DBs)",
            "SCCM precedence has no full field-by-field map - rework risk",
            "90% coverage has no measurement story",
        ],
    ),
    dict(
        name="Network Gear Discovery", due="Aug 31 -> Oct 30", pi="PI-3",
        summary="Discover and populate network devices in the CMDB, to 90% coverage.",
        done=[
            "Credentials configured & validated (excluding OT)",
            "Discovery schedules active",
            "Mandatory attributes populated",
            "90% coverage, business-owner validated",
        ],
        in_scope=["Network gear: credentials / SNMP, schedules, attributes, coverage"],
        out_scope=["OT (operational technology) devices - explicitly excluded"],
        stories=[
            "1356646 Network Device Coverage (feature)",
            "1402572 / 574 / 575 discovery config + rerun  ·  1402555 / 1402559 spikes",
            "Creds 1444864 / 1459721  ·  stakeholder dependency 1383487",
        ],
        watch=[
            "OT boundary - confirm with stakeholders",
            "Stakeholder requirements (1383487) still open",
            "Shares credential work with servers / databases",
        ],
    ),
    dict(
        name="Service Mapping", due="Aug 31 -> Oct 30", pi="PI-3",
        summary="End-to-end maps for 10 priority business apps down to infrastructure CIs.",
        done=[
            "Service maps built for 10 priority business apps",
            "Maps validated by application owners",
            "Maps consumable in ServiceNow",
        ],
        in_scope=["The 10 priority apps; app -> infra mapping; owner validation"],
        out_scope=["Apps beyond the 10 priority set"],
        stories=[
            "Wave features 1355866 / 1355868 / 1355871",
            "Per-app: WATT  ·  Oceana  ·  SolarWinds PoC 1431652",
        ],
        watch=[
            "App-owner validation is the gating dependency - need named owners",
            "Choose the 10 apps deliberately - it's a fixed acceptance bar",
            "Infra / credential access can stall mapping",
        ],
    ),
    dict(
        name="Legacy Platform Rationalization", due="Aug 31 -> Oct 30", pi="PI-3",
        summary="Analysis and migration plan for legacy data sources into the CMDB.",
        done=[
            "Analysis complete for iTeam -> DISCO / Cherwell -> AIM",
            "Migration plan produced (Cherwell / AIM only if applicable at PI-3 planning)",
        ],
        in_scope=["iTeam import / migration; analysis of DISCO / Cherwell / AIM"],
        out_scope=["Cherwell / AIM execution unless confirmed applicable at PI-3 planning"],
        stories=[
            "iTeam import 1452028 (only current story)",
            "Analysis / migration-plan stories - not created yet",
        ],
        watch=[
            "Greenfield - scope the analysis / plan stories at PI-3 planning",
            "Ties to the ~450-server application-to-server gap",
            "Cherwell / AIM applicability decided at PI-3 planning",
        ],
    ),
    dict(
        name="Qualys Integration", due="Oct 27", pi="PI-3",
        summary="One-way Qualys -> ServiceNow vulnerability feed, deployed to PROD.",
        done=[
            "One-way Qualys -> ServiceNow integration configured & tested",
            "Deployed to PROD",
            "Vulnerability data ingests on schedule, no data loss",
        ],
        in_scope=["One-way Qualys -> SNOW feed: config, test, PROD deploy"],
        out_scope=["Two-way sync; other integrations (Tanium was the alternative)"],
        stories=[
            "1428703 install plugin  ·  1428704 configure - both blocked",
            "Data-scope spike 1234585  ·  1465952 plugin replacement (closed)",
        ],
        watch=[
            "Plugin blocker: replacement plugin pending approval (1465952 may have cleared it - confirm)",
            "Story states were not auto-flipped - verify with Stan",
            "Build cannot finish until the plugin is unblocked",
        ],
    ),
    dict(
        name="ATF Strategy", due="Oct 31", pi="PI-3",
        summary="A plan for rolling out the Automated Test Framework across in-prod ServiceNow capabilities.",
        done=["Rollout plan delivered: selection criteria, timeline, and approach"],
        in_scope=["Strategy / plan for ATF rollout (an analysis deliverable)"],
        out_scope=["Building / implementing ATF (this is the plan, not the rollout)"],
        stories=["None - greenfield"],
        watch=[
            "No stories yet - scope at PI-3 planning",
            "Deliverable is a plan, not an implementation",
            "Owner TBD",
        ],
    ),
]

# Supporting lanes: (name, sub, items[])
SUPPORT = [
    ("ITSM Product Management", "Monthly  ·  PI-2 / PI-3", [
        "ITSM Product Owner role: stakeholder management, backlog prioritization, agile ceremonies, governance",
        "Separate ITSM lane - outside core CMDB delivery",
        "No stories; owner TBD",
    ]),
    ("Platform Support", "Monthly  ·  PI-3", [
        "Dedicated BAU / DevOps team; ~40 hrs of stories per week per member; per-sprint time tracking",
        "Ongoing capacity, not a finite deliverable",
        "Team size TBD",
    ]),
]
SUPPORT_NOTE = "These are staffing / capacity decisions, not backlog - flagged so they stay on the radar."

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
AMBER_FILL = RGBColor(0xFB, 0xEE, 0xDB)
AMBER_HEAD = RGBColor(0x7A, 0x4F, 0x10)
AMBER_BODY = RGBColor(0x5A, 0x4A, 0x2A)

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


def bullet_lines(title, items, tsize=12, bsize=10, bcolor=TEXT, tcolor=DARK):
    lines = []
    if title:
        lines.append((title, tsize, tcolor, True, False))
    for it in items:
        lines.append(("•  " + it, bsize, bcolor, False, False))
    return lines


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

# ---- Slide 2: Deliverables & dates (index) -------------------------------
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


# ---- Slides 3-10: per-deliverable detail ---------------------------------
def detail_slide(spec):
    s = prs.slides.add_slide(BLANK)
    header(s, spec["name"], "Due " + spec["due"] + "   ·   " + spec["pi"])
    # summary strip
    rect(s, Inches(0.55), Inches(1.22), Inches(12.2), Inches(0.5), RGBColor(0xE9, 0xF0, 0xF8), line=ACCENT)
    textbox(s, Inches(0.72), Inches(1.24), Inches(11.9), Inches(0.46),
            [(spec["summary"], 11, DARK, False, False)], MSO_ANCHOR.MIDDLE)
    # left column: Done when
    textbox(s, Inches(0.55), Inches(1.92), Inches(6.0), Inches(2.5),
            bullet_lines("Done when (acceptance)", spec["done"], bsize=10))
    # right column: Scope (in / out)
    scope = [("Scope", 12, DARK, True, False), ("In scope", 10.5, GREEN, True, False)]
    scope += [("•  " + it, 9.5, TEXT, False, False) for it in spec["in_scope"]]
    scope.append(("Out of scope", 10.5, RED, True, False))
    scope += [("•  " + it, 9.5, TEXT, False, False) for it in spec["out_scope"]]
    textbox(s, Inches(6.75), Inches(1.92), Inches(6.0), Inches(2.5), scope)
    # stories band
    rect(s, Inches(0.55), Inches(4.5), Inches(12.2), Inches(1.35), LIGHT)
    textbox(s, Inches(0.72), Inches(4.55), Inches(11.9), Inches(1.27),
            bullet_lines("Current stories", spec["stories"], tsize=11.5, bsize=9.5))
    # watch-outs strip
    rect(s, Inches(0.55), Inches(5.92), Inches(12.2), Inches(0.98), AMBER_FILL, line=AMBER)
    textbox(s, Inches(0.72), Inches(5.96), Inches(11.9), Inches(0.9),
            bullet_lines("Watch-outs / dependencies", spec["watch"],
                         tsize=11, bsize=9.5, bcolor=AMBER_BODY, tcolor=AMBER_HEAD))
    return s


for spec in DETAILS:
    detail_slide(spec)

# ---- Slide 11: Supporting lanes ------------------------------------------
s = prs.slides.add_slide(BLANK)
header(s, "Supporting Lanes", "PO / BAU capacity - separate from core CMDB delivery")
for k, (name, sub, items) in enumerate(SUPPORT):
    x = 0.55 + k * 6.35
    rect(s, Inches(x), Inches(1.5), Inches(6.0), Inches(0.72), DARK)
    textbox(s, Inches(x + 0.18), Inches(1.55), Inches(5.6), Inches(0.34), [(name, 15, WHITE, True, False)])
    textbox(s, Inches(x + 0.18), Inches(1.88), Inches(5.6), Inches(0.28),
            [(sub, 11, RGBColor(0xC9, 0xD6, 0xE6), False, False)])
    rect(s, Inches(x), Inches(2.22), Inches(6.0), Inches(3.0), LIGHT)
    textbox(s, Inches(x + 0.18), Inches(2.35), Inches(5.6), Inches(2.8),
            bullet_lines("", items, bsize=11))
rect(s, Inches(0.55), Inches(5.5), Inches(12.2), Inches(0.7), AMBER_FILL, line=AMBER)
textbox(s, Inches(0.72), Inches(5.54), Inches(11.9), Inches(0.62),
        [(SUPPORT_NOTE, 11, AMBER_BODY, False, False)], MSO_ANCHOR.MIDDLE)

# ---- Slide 12: Timeline --------------------------------------------------
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

# ---- Slide 13: Where to focus --------------------------------------------
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
