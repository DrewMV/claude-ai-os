"""
PI-3 Work Scheduled deck — CMDB / CSDM team.

Slides:
  1. Title
  2. Program Board  (15 features across 6 sprints)
  3. Sprint Load Overview  (stacked column chart, points by workstream)
  4-9. Sprint 3.1 - 3.6 IP detail  (feature rows: ADO IDs, story detail, points)
  10. Certification Reconciliation — Computers & Servers (Sep 30 gate)
  11. Certification Reconciliation — Databases & Network Devices (Oct 30 gate)
  12. Open Items & Data Quality Flags

Source: pi3-cmdb-csdm-ado-tracking.md + per-feature story/dependency files,
reconciled against a full ADO board export (sorted by Work Item Type, with
Iteration Path) as of 2026-08-06. All IDs/points/sprints below are ADO-confirmed
unless flagged otherwise.

Run:  python build_pi3_work_scheduled_deck.py
Output: PI3-Work-Scheduled-2026-08-06.pptx
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION

# ─────────────────────────────────────────────────── CONTENT
EDITION   = "2026-08-06"
TITLE     = "PI-3 Work Scheduled  —  CMDB / CSDM"
SUBTITLE  = "5 Objectives · 15 Features · 213 Story Points · Aug 5 – Oct 27, 2026"
AUTHOR    = "Manuel Vazquez  —  Product Owner, CMDB-CSDM"
FOOTLABEL = ("PPL CMDB-CSDM  |  PI-3 Work Scheduled  |  "
             "ADO A-INFOPS\\FY26\\PI3  |  Aug 6, 2026")
DRAFT_NOTE = ("Reconciled against ADO board export (Iteration Path), Aug 6, 2026. "
              "Points marked TBD are not yet visible in ADO.")

# ─────────────────────────────────────────────────── THEME
DARK        = RGBColor(0x1F, 0x3A, 0x5F)
ACCENT      = RGBColor(0x2E, 0x6D, 0xB4)
LIGHT       = RGBColor(0xF4, 0xF6, 0xF9)
TEXT        = RGBColor(0x2D, 0x2D, 0x2D)
MUTED       = RGBColor(0x6B, 0x72, 0x80)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
RULE        = RGBColor(0xDD, 0xE3, 0xEA)

BLUE   = RGBColor(0x2E, 0x6D, 0xB4); BLUE_T   = RGBColor(0x1A, 0x52, 0x96)
TEAL   = RGBColor(0x2A, 0x9D, 0x8F); TEAL_T   = RGBColor(0x1F, 0x7A, 0x6E)
INDIGO = RGBColor(0x5B, 0x4B, 0x8A); INDIGO_T = RGBColor(0x4A, 0x3D, 0x73)
AMBER  = RGBColor(0xE0, 0x8A, 0x00); AMBER_T  = RGBColor(0xB5, 0x6E, 0x00)
CORAL  = RGBColor(0xC0, 0x52, 0x3A); CORAL_T  = RGBColor(0x8F, 0x3C, 0x2A)
RED    = RGBColor(0xC0, 0x39, 0x2B)

# workstream: (label, fill_vivid, text_on_white)
WS = {
    "NET":  ("Network Discovery",       BLUE,   BLUE_T),
    "SM":   ("Service Maps / BA Migr.", TEAL,   TEAL_T),
    "CERT": ("Data Certification",      INDIGO, INDIGO_T),
    "QLY":  ("Qualys Sync",             AMBER,  AMBER_T),
    "GOV":  ("PI-2 Carryover / Gov.",   CORAL,  CORAL_T),
}

EMU_W, EMU_H = Inches(13.333), Inches(7.5)
FONT = "Calibri"

# ─────────────────────────────────────────────────── PROGRAM BOARD DATA
FEATURES = [
    dict(id="1516993", ws="NET",  sprint="3.1", co6="Aug 31", short="Discovery Live — all device types"),
    dict(id="1517650", ws="SM",   sprint="3.1", co6="Aug 31", short="Silver-Tier Maps + ≥75% Inventory"),
    dict(id="1537867", ws="SM",   sprint="3.1", co6="n/a",    short="Migrate BA → Service Instances (DQ)"),
    dict(id="1517065", ws="QLY",  sprint="3.1", co6="Sep 30", short="Activate SN→Qualys Sync (PROD)"),
    dict(id="1554951", ws="GOV",  sprint="3.1", co6="n/a",    short="Database Class Clean-up (PI-2)"),
    dict(id="1557616", ws="GOV",  sprint="3.1", co6="n/a",    short="Air Lift CMDB Support (PI-2)"),
    dict(id="1553982", ws="GOV",  sprint="3.1", co6="n/a",    short="New BA Governance Model (PI-2)"),
    dict(id="1517029", ws="CERT", sprint="3.2", co6="Sep 30", short="Certify Computers"),
    dict(id="1517032", ws="CERT", sprint="3.2", co6="Sep 30", short="Certify Servers"),
    dict(id="1517005", ws="NET",  sprint="3.3", co6="Sep 30", short="Mandatory Attribute Population"),
    dict(id="1517655", ws="SM",   sprint="3.3", co6="Sep 30", short="Gold-Tier Maps + Silver Validation"),
    dict(id="1517037", ws="CERT", sprint="3.4", co6="Oct 30", short="Certify Databases"),
    dict(id="1517040", ws="CERT", sprint="3.4", co6="Oct 30", short="Certify Network Devices"),
    dict(id="1356646", ws="NET",  sprint="3.5", co6="Oct 30", short="Coverage Reconciliation ≥90%"),
    dict(id="1518000", ws="SM",   sprint="3.5", co6="Oct 30", short="Remaining Silver + Svc→App"),
]

SPRINTS_BOARD = [
    ("3.1",    "Aug 5–18"),
    ("3.2",    "Aug 19–Sep 1"),
    ("3.3",    "Sep 2–15"),
    ("3.4",    "Sep 16–29"),
    ("3.5",    "Sep 30–Oct 13"),
    ("3.6 IP", "Oct 14–27"),
]

# ─────────────────────────────────────────────────── SPRINT LOAD (points by workstream)
LOAD = {
    "3.1":    {"NET": 13, "CERT": 4,  "QLY": 1, "SM": 34, "GOV": 4},
    "3.2":    {"NET": 0,  "CERT": 9,  "QLY": 0, "SM": 38, "GOV": 0},
    "3.3":    {"NET": 5,  "CERT": 2,  "QLY": 0, "SM": 29, "GOV": 0},
    "3.4":    {"NET": 11, "CERT": 34, "QLY": 0, "SM": 8,  "GOV": 0},
    "3.5":    {"NET": 14, "CERT": 0,  "QLY": 0, "SM": 0,  "GOV": 0},
    "3.6 IP": {"NET": 5,  "CERT": 0,  "QLY": 0, "SM": 0,  "GOV": 0},
}

# ─────────────────────────────────────────────────── SPRINT DETAIL (feature rows)
# Each row: (ado_id, ws, feature_name, detail_text, points_label, note)
SPRINT_DATA = [
    {
        "code": "3.1", "dates": "Aug 5 – Aug 18",
        "gates": "No CO6 gate this sprint — delivery enablement  |  test code freeze Aug 5–15 (no PROD deploys)",
        "rows": [
            ("1516993", "NET", "Automated Credentialed Discovery Live — All Network Device Types",
             "ND-1 1526911 Configure credentials (5) · ND-2 1526947 Discovery defs/IP ranges (1) · "
             "ND-3 1526951 Credentialed discovery live, all 6 device types (2) · ND-6 1557701 Analysis of network ranges (2)",
             "10", None),
            ("1356646", "NET", "Network Inventory Coverage Reconciliation (≥90%) — prep",
             "1402555 Identify CI classes for group 1 (3, spike)", "3", None),
            ("1517029", "CERT", "Certify Computers",
             "CC-1 1535486 Document cert process flow (2, spike)", "2", None),
            ("1517032", "CERT", "Certify Servers",
             "SV-1 1535496 Document cert process flow (2, spike)", "2", None),
            ("1517065", "QLY", "Activate ServiceNow → Qualys Sync (PROD)",
             "1428703 Install x_qual5_itam_nwapp plugin, Dev/Test/Prod (1)", "1", None),
            ("1537867", "SM", "Migration of Business Apps to Application Services",
             "S01 1553645 Inventory / reference-map (8) · S07 1553653 Stakeholder comms & enablement (8)", "16", None),
            ("1517650", "SM", "Silver-Tier Service Maps + ≥75% Inventory",
             "3 spikes + 15 stories — data-source discovery batch (11 named apps + 4 placeholder)", "18", None),
            ("GOV", "GOV", "PI-2 Carryover / Governance stories",
             "1512084 Populate Assigned-to, Computer Class (2, ⚠ misplaced under DB feature) · "
             "1553978/1553980 Service Catalog + SOX-flag governance (1 each)", "4", None),
        ],
    },
    {
        "code": "3.2", "dates": "Aug 19 – Sep 1",
        "gates": "CO6 gate Aug 31 — Automated Credentialed Discovery Live  +  Silver Service Maps  +  ≥75% Inventory",
        "rows": [
            ("1517029", "CERT", "Certify Computers",
             "CC-2 1535488 Build cert policies to PROD (2) · CC-3 1535489 Stand up dashboard (1) · "
             "CC-5 1535491 Deliver training (3, ⚠ lands ahead of CC-4)", "6", "sequencing"),
            ("1517032", "CERT", "Certify Servers",
             "SV-2 1535499 Build cert policies to PROD (2) · SV-3 1535500 Stand up dashboard (1)", "3", None),
            ("1537867", "SM", "Migration of Business Apps to Application Services",
             "S02 1553646 Copy BA → Application Service, retire original (8) · "
             "S09 1553656 Recurrence-guardrail spike (1)", "9", None),
            ("1517650", "SM", "Silver-Tier Service Maps + ≥75% Inventory",
             "13 spikes + 16 stories — data-source discovery + build batch", "29", None),
        ],
    },
    {
        "code": "3.3", "dates": "Sep 2 – Sep 15",
        "gates": "No CO6 gate this sprint — builds toward Sep 30  |  test freeze lifted",
        "rows": [
            ("1517029", "CERT", "Certify Computers",
             "CC-4 1535490 Run cert cycle & monitor completeness (1)", "1", None),
            ("1517032", "CERT", "Certify Servers",
             "SV-4 1535502 Run cert cycle & monitor completeness (1)", "1", None),
            ("1517005", "NET", "Mandatory Attribute Population via Discovery — Network Devices",
             "1537633 Define mandatory candidates (2) · 1537635 Baseline population & gap analysis (3)", "5", None),
            ("1537867", "SM", "Migration of Business Apps to Application Services",
             "S04 1553648 Enable migrated services (3) · S10 1553649 Validate migration end state (5) · "
             "S05 1553651 Retarget platform config off retired class (8)", "16", None),
            ("1517650", "SM", "Silver-Tier Service Maps + ≥75% Inventory",
             "5 spikes + 8 stories — all placeholder-titled, not yet filled in with real app names", "13", "data quality"),
        ],
    },
    {
        "code": "3.4", "dates": "Sep 16 – Sep 29",
        "gates": "CO6 gate Sep 30 (prior sprint's work lands) — ⚠ heaviest sprint: 53 pts, driven by Databases + Network Devices landing together",
        "rows": [
            ("1517037", "CERT", "Certify Databases",
             "DB-1 1560066 Document process flow (3, spike) · DB-2 1560067 Build to PROD (3) · "
             "DB-3 1560068 Dashboard (2) · DB-4 1560069 Run cycle (2) · DB-5 1560071 Training (3)",
             "13", "clustering"),
            ("1517040", "CERT", "Certify Network Devices",
             "NW-1 1560087 Audit-baseline spike (5) · NW-2 1560089 Process flow (3) · "
             "NW-3 1560091 Build to PROD (3) · NW-4 1560093 Dashboard (2) · NW-5 1560094 Run cycle (2) · "
             "NW-6 1560096 Training (3)", "18", "clustering"),
            ("1517032", "CERT", "Certify Servers",
             "SV-5 1535504 Deliver training (3)", "3", None),
            ("1517005", "NET", "Mandatory Attribute Population via Discovery — Network Devices",
             "1537637 Populate non-discoverable attrs, CI owner (2) · 1537638 Validate no blanks (TBD) · "
             "1560305 …Support Group (2) · 1560306 …Technical Group Owner (2) · 1560308 …Environment (2)",
             "8 + TBD", None),
            ("1356646", "NET", "Network Inventory Coverage Reconciliation (≥90%) — prep",
             "1402559 Compare CI class sources (3, spike)", "3", None),
            ("1537867", "SM", "Migration of Business Apps to Application Services",
             "S06 1553652 Route operational CIs to App Service (3) · S08 1553654 Post-migration hypercare & close-out (5)",
             "8", None),
        ],
    },
    {
        "code": "3.5", "dates": "Sep 30 – Oct 13",
        "gates": "No new CO6 gate this sprint — builds toward Oct 30",
        "rows": [
            ("1356646", "NET", "Network Inventory Coverage Reconciliation (≥90%)",
             "CR-1 1559163 Define authoritative inventory / denominator (3) · CR-2 1559166 Gap analysis (3) · "
             "CR-3 1559175 Gap closure (5) · CR-4 1559183 Coverage dashboard (3)", "14", None),
        ],
    },
    {
        "code": "3.6 IP", "dates": "Oct 14 – Oct 27",
        "gates": "CO6 gate Oct 30 — Certify Databases  ·  Certify Network Devices  ·  Coverage ≥90%  |  sign-off / validation buffer, not new build",
        "rows": [
            ("1356646", "NET", "Network Inventory Coverage Reconciliation (≥90%) — final",
             "CR-5 1559193 Business-owner validation & sign-off on ≥90% coverage (5)", "5", None),
        ],
    },
]

# ─────────────────────────────────────────────────── CERTIFICATION DEEP-DIVE DATA
CERT_SEP30 = {
    "title": "Certification Reconciliation — Computers & Servers",
    "subtitle": "CO6 Obj 3  ·  Sep 30 gate  ·  all 10 stories created in ADO, IDs reconciled",
    "groups": [
        ("1517029", "Certify Computers", [
            ("CC-1", "1535486", "Document the Computer Data Certification process flow", "2", "3.1", "Ready DoR"),
            ("CC-2", "1535488", "Build Computer certification policies/rules to PROD", "2", "3.2", "Ready DoR"),
            ("CC-3", "1535489", "Stand up the Computer certification tracking dashboard", "1", "3.2", "Ready DoR"),
            ("CC-4", "1535490", "Run the Computer certification cycle and monitor completeness", "1", "3.3", "New"),
            ("CC-5", "1535491", "Deliver Computer certification training to CI owners", "3", "3.2", "Ready DoR"),
        ]),
        ("1517032", "Certify Servers", [
            ("SV-1", "1535496", "Document the Server Data Certification process flow", "2", "3.1", "Active"),
            ("SV-2", "1535499", "Build Server certification policies/rules to PROD", "2", "3.2", "Ready DoR"),
            ("SV-3", "1535500", "Stand up the Server certification tracking dashboard", "1", "3.2", "Ready DoR"),
            ("SV-4", "1535502", "Run the Server certification cycle and monitor completeness", "1", "3.3", "New"),
            ("SV-5", "1535504", "Deliver Server certification training to CI owners", "3", "3.4", "New"),
        ]),
    ],
}

CERT_OCT30 = {
    "title": "Certification Reconciliation — Databases & Network Devices",
    "subtitle": "CO6 Obj 3  ·  Oct 30 gate  ·  all 11 stories created in ADO, IDs reconciled — ⚠ all landed in Sprint 3.4",
    "groups": [
        ("1517037", "Certify Databases", [
            ("DB-1", "1560066", "Document the Database Data Certification process flow", "3", "3.4", "New (spike)"),
            ("DB-2", "1560067", "Build Database certification policies/rules to PROD", "3", "3.4", "New"),
            ("DB-3", "1560068", "Stand up the Database certification tracking dashboard", "2", "3.4", "New"),
            ("DB-4", "1560069", "Run the Database certification cycle and monitor completeness", "2", "3.4", "New"),
            ("DB-5", "1560071", "Deliver Database certification training to CI owners", "3", "3.4", "New"),
        ]),
        ("1517040", "Certify Network Devices", [
            ("NW-1", "1560087", "Network audit-dashboard scope + gap-remediation baseline", "5", "3.4", "New (spike)"),
            ("NW-2", "1560089", "Document the Network Device certification process flow", "3", "3.4", "New"),
            ("NW-3", "1560091", "Build Network Device certification policies/rules to PROD", "3", "3.4", "New"),
            ("NW-4", "1560093", "Stand up the Network Device certification tracking dashboard", "2", "3.4", "New"),
            ("NW-5", "1560094", "Run the Network Device certification cycle and monitor completeness", "2", "3.4", "New"),
            ("NW-6", "1560096", "Deliver Network Device certification training to owners", "3", "3.4", "New"),
        ]),
    ],
}

OPEN_ITEMS = [
    ("Sprint 3.4 clustering", "All 5 Databases stories and all 6 Network Devices stories landed in Iteration 3.4 "
     "in ADO, rather than phased across 3.4→3.6 IP as drafted — 31 of 53 points in that sprint from these "
     "two features alone. Same pattern as CC-5 landing ahead of CC-4."),
    ("Service Mapping placeholder titles", "17 of the 39 “Gather/Build/Validate/Publish” stories under "
     "Feature 1517650 are still titled [PLACEHOLDER] — bulk-created template rows not yet filled in with a "
     "real app / data-source name. Flag to Adam Griffis."),
    ("Possible duplicate stories", "1508982 / 1513944 (no parent, no sprint assigned) look like duplicates of "
     "1553978 / 1553980 (parented to Feature 1553982, Sprint 3.1, same titles). Not resolved — confirm in ADO."),
    ("1512084 still misplaced", "“Populate Assigned-to field in Computer Class” is parented to the Database "
     "Class Clean-up feature (1554951), not a Computer-class feature. Needs reparenting in ADO."),
    ("Unparented / no-sprint item", "1393089 “Requirement Gathering for Non-OT devices” (0 pts) has no "
     "parent feature and no sprint — ownership unclear."),
    ("Points not yet visible in ADO", "1537638 (Mandatory Attribute Population, Sprint 3.4), plus 4 PI-2 database "
     "clean-up stories and 2 Airlift stories — real load, but not counted in the 213-point total above."),
]

# ─────────────────────────────────────────────────── HELPERS

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


def rounded_rect(slide, x, y, w, h, color):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
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
        r = p.add_run()
        r.text = text
        _set(r, size, color, bold, italic)
    return tb


def slide_header(slide, title, subtitle=None):
    rect(slide, 0, 0, EMU_W, Inches(1.05), DARK)
    rect(slide, 0, Inches(1.05), EMU_W, Inches(0.06), ACCENT)
    textbox(slide, Inches(0.55), Inches(0.13), Inches(12.2), Inches(0.58),
            [(title, 22, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
    if subtitle:
        textbox(slide, Inches(0.57), Inches(0.65), Inches(12.2), Inches(0.32),
                [(subtitle, 10.5, RGBColor(0xC9, 0xD6, 0xE6), False, False)],
                MSO_ANCHOR.MIDDLE)
    textbox(slide, Inches(0.55), Inches(7.10), Inches(11.8), Inches(0.28),
            [(FOOTLABEL, 8.5, MUTED, False, False)])


def _tcell(t, i, j, lines, size, color, bold=False,
           align=PP_ALIGN.LEFT, fill=None, anchor=MSO_ANCHOR.MIDDLE, italic=False):
    c = t.cell(i, j)
    if fill is not None:
        c.fill.solid()
        c.fill.fore_color.rgb = fill
    c.vertical_anchor = anchor
    tf = c.text_frame
    tf.word_wrap = True
    if isinstance(lines, str):
        lines = [lines]
    for k, ln in enumerate(lines):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_before = Pt(0)
        p.space_after = Pt(1)
        r = p.add_run()
        r.text = ln
        _set(r, size, color, bold, italic)


# ─────────────────────────────────────────────────── SLIDE 1 — TITLE

def add_title(prs, blank):
    s = prs.slides.add_slide(blank)
    rect(s, 0, 0, EMU_W, EMU_H, DARK)
    rect(s, 0, Inches(4.45), EMU_W, Inches(0.08), ACCENT)
    textbox(s, Inches(0.85), Inches(1.6), Inches(11.6), Inches(1.2),
            [(TITLE, 38, WHITE, True, False)])
    textbox(s, Inches(0.87), Inches(2.75), Inches(11.6), Inches(0.65),
            [(SUBTITLE, 18, RGBColor(0xC9, 0xD6, 0xE6), False, False)])
    textbox(s, Inches(0.87), Inches(4.62), Inches(11.6), Inches(2.0), [
        ("All 4 certification classes fully reconciled in ADO — Computers, Servers, Databases, Network Devices", 15, WHITE, True, False),
        ("CMDB / CSDM team focus area  —  a subset of CO6", 13, RGBColor(0xC9, 0xD6, 0xE6), False, False),
        (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
    ])
    textbox(s, Inches(0.87), Inches(6.5), Inches(11.6), Inches(0.4),
            [(DRAFT_NOTE, 10.5, RGBColor(0x7F, 0x8C, 0xA6), False, True)])


# ─────────────────────────────────────────────────── SLIDE 2 — PROGRAM BOARD

def add_board(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_header(s, "PI-3 Program Board — 15 Features Across 6 Sprints",
                 "Color-coded by objective  ·  all features are parented to one of 5 PI-3 objectives")
    usable = 12.2
    gap = 0.10
    colw = (usable - 5 * gap) / 6.0
    top = 1.32
    hdr_h = 0.55
    chip_h = 0.58
    chip_gap = 0.06

    for ci, (code, dates) in enumerate(SPRINTS_BOARD):
        cx = 0.55 + ci * (colw + gap)
        is_ip = "IP" in code
        col_fill = MUTED if is_ip else DARK
        rect(s, Inches(cx), Inches(top), Inches(colw), Inches(hdr_h), col_fill)
        textbox(s, Inches(cx), Inches(top + 0.03), Inches(colw), Inches(hdr_h - 0.04),
                [("Sprint " + code, 11, WHITE, True, False),
                 (dates, 8, RGBColor(0xC9, 0xD6, 0xE6), False, False)],
                MSO_ANCHOR.MIDDLE, PP_ALIGN.CENTER)

        feats = [f for f in FEATURES if f["sprint"] == code]
        chip_top = top + hdr_h + 0.07
        if not feats:
            rect(s, Inches(cx), Inches(chip_top), Inches(colw), Inches(chip_h), LIGHT)
            textbox(s, Inches(cx), Inches(chip_top), Inches(colw), Inches(chip_h),
                    [("— sign-off buffer —", 8, MUTED, False, True)], MSO_ANCHOR.MIDDLE, PP_ALIGN.CENTER)
            continue
        for fi, f in enumerate(feats):
            cy = chip_top + fi * (chip_h + chip_gap)
            vivid = WS[f["ws"]][1]
            rounded_rect(s, Inches(cx), Inches(cy), Inches(colw), Inches(chip_h), vivid)
            textbox(s, Inches(cx + 0.06), Inches(cy + 0.03),
                    Inches(colw - 0.12), Inches(chip_h - 0.06),
                    [(f["short"], 7, WHITE, True, False),
                     ("ADO " + f["id"] + "  ·  CO6 " + f["co6"], 6.5, RGBColor(0xE0, 0xEC, 0xF8), False, False)],
                    MSO_ANCHOR.MIDDLE, PP_ALIGN.LEFT)

    # legend
    lx, ly = 0.55, 6.72
    textbox(s, Inches(lx), Inches(ly - 0.02), Inches(1.0), Inches(0.28),
            [("Objective:", 9, TEXT, True, False)], MSO_ANCHOR.MIDDLE)
    lx += 1.05
    for key in ["NET", "SM", "CERT", "QLY", "GOV"]:
        name, vivid, _ = WS[key]
        rect(s, Inches(lx), Inches(ly + 0.01), Inches(0.2), Inches(0.2), vivid)
        textbox(s, Inches(lx + 0.26), Inches(ly - 0.02), Inches(2.3), Inches(0.28),
                [(name, 8.5, TEXT, False, False)], MSO_ANCHOR.MIDDLE)
        lx += 2.3


# ─────────────────────────────────────────────────── SLIDE 3 — SPRINT LOAD CHART

def add_load_chart(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_header(s, "Sprint Load Overview — Story Points by Workstream",
                 "213 known points across 25 features/sprints · Sprint 3.4 is the heaviest at 53 points")

    cats = [code for code, _ in SPRINTS_BOARD]
    chart_data = CategoryChartData()
    chart_data.categories = cats
    ws_order = ["NET", "CERT", "SM", "QLY", "GOV"]
    hexmap = {"NET": BLUE, "CERT": INDIGO, "SM": TEAL, "QLY": AMBER, "GOV": CORAL}
    for key in ws_order:
        chart_data.add_series(WS[key][0], [LOAD[c][key] for c in cats])

    x, y, cx, cy = Inches(0.55), Inches(1.35), Inches(12.2), Inches(5.1)
    gframe = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_STACKED, x, y, cx, cy, chart_data)
    chart = gframe.chart
    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.legend.include_in_layout = False
    chart.legend.font.size = Pt(11)
    chart.legend.font.name = FONT

    for i, plot in enumerate(chart.plots):
        plot.has_data_labels = True
        dl = plot.data_labels
        dl.number_format = '0'
        dl.number_format_is_linked = False
        dl.font.size = Pt(9)
        dl.font.color.rgb = WHITE
        dl.font.bold = True

    for i, series in enumerate(chart.series):
        series.format.fill.solid()
        series.format.fill.fore_color.rgb = hexmap[ws_order[i]]

    cat_ax = chart.category_axis
    cat_ax.tick_labels.font.size = Pt(12)
    cat_ax.tick_labels.font.name = FONT
    cat_ax.format.line.color.rgb = RULE

    val_ax = chart.value_axis
    val_ax.has_major_gridlines = True
    val_ax.major_gridlines.format.line.color.rgb = RULE
    val_ax.tick_labels.font.size = Pt(10)
    val_ax.tick_labels.font.name = FONT
    val_ax.tick_labels.font.color.rgb = MUTED

    textbox(s, Inches(0.55), Inches(6.55), Inches(12.2), Inches(0.5),
            [("⚠ 45 additional points from PI-2 carryover stories with no point value yet visible in ADO are not shown "
              "(4 database clean-up stories, 2 Airlift stories, 1537638).", 9.5, MUTED, False, True)])


# ─────────────────────────────────────────────────── SLIDES 4-9 — SPRINT DETAIL

def add_sprint_detail(prs, blank, sd):
    s = prs.slides.add_slide(blank)
    code  = sd["code"]
    dates = sd["dates"]
    gates = sd["gates"]
    rows  = sd["rows"]

    n_rows = 1 + len(rows)
    slide_header(s, f"Sprint {code}  —  {dates}", gates)

    tbl_top  = Inches(1.30)
    tbl_left = Inches(0.55)
    tbl_w    = Inches(12.2)
    tbl_h    = Inches(5.68)

    # column widths: ADO ID | Feature | Story detail | Points
    COL_W = [Inches(1.55), Inches(2.85), Inches(6.9), Inches(0.9)]

    t = s.shapes.add_table(n_rows, 4, tbl_left, tbl_top, tbl_w, tbl_h).table
    for j, wdt in enumerate(COL_W):
        t.columns[j].width = wdt

    hdr_labels = ["ADO ID", "Feature", "Story / spike detail (id, ADO id, description, points)", "Total pts"]
    for j, lbl in enumerate(hdr_labels):
        algn = PP_ALIGN.LEFT if j in (1, 2) else PP_ALIGN.CENTER
        _tcell(t, 0, j, lbl, 9.5, WHITE, True, algn, DARK, MSO_ANCHOR.MIDDLE)

    for i, (fid, ws, fname, detail, pts, note) in enumerate(rows, start=1):
        fill = LIGHT if i % 2 == 0 else WHITE
        _, vivid, txt_on_white = WS[ws]
        id_disp = fid if fid != "GOV" else "—"
        _tcell(t, i, 0, id_disp, 9, txt_on_white, True, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
        if note:
            _tcell(t, i, 1, [fname, "⚠ " + note], 9, TEXT, False, PP_ALIGN.LEFT, fill, MSO_ANCHOR.MIDDLE)
            t.cell(i, 1).text_frame.paragraphs[1].runs[0].font.color.rgb = RED
            t.cell(i, 1).text_frame.paragraphs[1].runs[0].font.bold = True
            t.cell(i, 1).text_frame.paragraphs[1].runs[0].font.size = Pt(8)
        else:
            _tcell(t, i, 1, fname, 9, TEXT, False, PP_ALIGN.LEFT, fill, MSO_ANCHOR.MIDDLE)
        _tcell(t, i, 2, detail, 8.5, TEXT, False, PP_ALIGN.LEFT, fill, MSO_ANCHOR.MIDDLE)
        _tcell(t, i, 3, pts, 10, ACCENT, True, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)

    note_y = tbl_top + tbl_h + Inches(0.05)
    textbox(s, tbl_left, note_y, tbl_w, Inches(0.25),
            [(DRAFT_NOTE, 8.5, MUTED, False, True)])


# ─────────────────────────────────────────────────── SLIDES 10-11 — CERTIFICATION DEEP-DIVE

def add_cert_detail(prs, blank, spec):
    s = prs.slides.add_slide(blank)
    slide_header(s, spec["title"], spec["subtitle"])

    n_rows = 1
    for _, _, stories in spec["groups"]:
        n_rows += 1 + len(stories)

    tbl_top  = Inches(1.30)
    tbl_left = Inches(0.55)
    tbl_w    = Inches(12.2)
    tbl_h    = Inches(5.68)

    COL_W = [Inches(0.75), Inches(0.95), Inches(6.9), Inches(1.0), Inches(0.95), Inches(1.65)]
    t = s.shapes.add_table(n_rows, 6, tbl_left, tbl_top, tbl_w, tbl_h).table
    for j, wdt in enumerate(COL_W):
        t.columns[j].width = wdt

    hdr_labels = ["Local", "ADO ID", "Story", "Points", "Sprint", "State"]
    for j, lbl in enumerate(hdr_labels):
        algn = PP_ALIGN.LEFT if j == 2 else PP_ALIGN.CENTER
        _tcell(t, 0, j, lbl, 9.5, WHITE, True, algn, DARK, MSO_ANCHOR.MIDDLE)

    row = 1
    for feat_id, feat_name, stories in spec["groups"]:
        t.cell(row, 0).merge(t.cell(row, 5))
        _tcell(t, row, 0, f"ADO {feat_id}  ·  {feat_name}", 9.5, WHITE, True, PP_ALIGN.LEFT, INDIGO, MSO_ANCHOR.MIDDLE)
        row += 1
        for local, ado, desc, pts, sprint, state in stories:
            fill = LIGHT if row % 2 == 0 else WHITE
            _tcell(t, row, 0, local, 9, ACCENT, True, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 1, ado, 9, TEXT, False, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 2, desc, 9, TEXT, False, PP_ALIGN.LEFT, fill, MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 3, pts, 9, TEXT, False, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 4, sprint, 9, MUTED, False, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 5, state, 8.5, MUTED, False, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
            row += 1

    note_y = tbl_top + tbl_h + Inches(0.05)
    textbox(s, tbl_left, note_y, tbl_w, Inches(0.25),
            [(DRAFT_NOTE, 8.5, MUTED, False, True)])


# ─────────────────────────────────────────────────── SLIDE 12 — OPEN ITEMS

def add_open_items(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_header(s, "Open Items & Data Quality Flags",
                 "Surfaced while reconciling the Aug 6 ADO export — none of these block PI-3, all need an owner")

    top = 1.32
    card_h = 0.85
    gap = 0.10
    for i, (label, body) in enumerate(OPEN_ITEMS):
        cy = top + i * (card_h + gap)
        rounded_rect(s, Inches(0.55), Inches(cy), Inches(12.2), Inches(card_h), LIGHT)
        rect(s, Inches(0.55), Inches(cy), Inches(0.14), Inches(card_h), RED)
        textbox(s, Inches(0.85), Inches(cy + 0.06), Inches(3.1), Inches(card_h - 0.12),
                [(label, 12, TEXT, True, False)], MSO_ANCHOR.MIDDLE)
        textbox(s, Inches(4.05), Inches(cy + 0.06), Inches(8.5), Inches(card_h - 0.12),
                [(body, 10, TEXT, False, False)], MSO_ANCHOR.MIDDLE)


# ─────────────────────────────────────────────────── BUILD + SAVE

def build_deck():
    prs = Presentation()
    prs.slide_width  = EMU_W
    prs.slide_height = EMU_H
    blank = prs.slide_layouts[6]

    add_title(prs, blank)
    add_board(prs, blank)
    add_load_chart(prs, blank)
    for sd in SPRINT_DATA:
        add_sprint_detail(prs, blank, sd)
    add_cert_detail(prs, blank, CERT_SEP30)
    add_cert_detail(prs, blank, CERT_OCT30)
    add_open_items(prs, blank)

    return prs


def save_safe(prs, path):
    try:
        prs.save(path)
        print(f"Saved  {os.path.basename(path)}  ({len(prs.slides._sldIdLst)} slides)")
    except PermissionError:
        base, ext = os.path.splitext(path)
        alt = base + "-new" + ext
        prs.save(alt)
        print(f"Target locked — saved to  {os.path.basename(alt)}")


here = os.path.dirname(os.path.abspath(__file__))
out  = os.path.join(here, f"PI3-Work-Scheduled-{EDITION}.pptx")
save_safe(build_deck(), out)
