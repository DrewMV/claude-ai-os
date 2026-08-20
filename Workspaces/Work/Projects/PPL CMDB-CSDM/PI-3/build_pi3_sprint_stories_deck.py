"""
PI-3 Sprint & Story Plan deck — CMDB / CSDM team.

Slides:
  1. Title
  2. Program Board  (features across 6 sprints, same palette as features deck)
  3–8. Sprint 3.1 – 3.6 IP detail  (each sprint: features + stories executing that sprint)

Source: pi3-cmdb-csdm-ado-tracking.md + per-feature story/dependency files,
as of 2026-07-29. Stories are REFERENCE / DRAFT — ADO is authoritative.

Run:  python build_pi3_sprint_stories_deck.py
Output: PI3-Sprint-Stories-Plan-2026-07-29.pptx
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ─────────────────────────────────────────────────── CONTENT
EDITION   = "2026-07-29"
TITLE     = "PI-3 Sprint & Story Plan  —  CMDB / CSDM"
SUBTITLE  = "6 Sprints · Features & Stories · Aug 5 – Oct 27, 2026"
AUTHOR    = "Manuel Vazquez  —  Scrum Master, CMDB-CSDM"
FOOTLABEL = ("PPL CMDB-CSDM  |  PI-3 Sprint & Story Plan  |  "
             "ADO A-INFOPS\\FY26\\PI3  |  Jul 29, 2026")
DRAFT_NOTE = ("Stories: REFERENCE / DRAFT — ADO is authoritative. "
              "Story IDs filled in as items are created in ADO.")

# ─────────────────────────────────────────────────── THEME
DARK        = RGBColor(0x1F, 0x3A, 0x5F)
ACCENT      = RGBColor(0x2E, 0x6D, 0xB4)
LIGHT       = RGBColor(0xF4, 0xF6, 0xF9)
TEXT        = RGBColor(0x2D, 0x2D, 0x2D)
MUTED       = RGBColor(0x6B, 0x72, 0x80)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
GREEN       = RGBColor(0x2E, 0x8B, 0x57)
RED         = RGBColor(0xC0, 0x39, 0x2B)
AMBER_GATE  = RGBColor(0xE6, 0x7E, 0x00)
RULE        = RGBColor(0xDD, 0xE3, 0xEA)
ACCENT_TINT = RGBColor(0xE9, 0xF0, 0xF8)

BLUE   = RGBColor(0x2E, 0x6D, 0xB4); BLUE_T   = RGBColor(0x1A, 0x52, 0x96)
TEAL   = RGBColor(0x2A, 0x9D, 0x8F); TEAL_T   = RGBColor(0x1F, 0x7A, 0x6E)
INDIGO = RGBColor(0x5B, 0x4B, 0x8A); INDIGO_T = RGBColor(0x4A, 0x3D, 0x73)
AMBER  = RGBColor(0xE0, 0x8A, 0x00); AMBER_T  = RGBColor(0xB5, 0x6E, 0x00)

# workstream: (label, fill_vivid, text_on_white)
WS = {
    "NET":  ("Network Discovery",  BLUE,   BLUE_T),
    "SM":   ("Service Maps",       TEAL,   TEAL_T),
    "CERT": ("Data Certification", INDIGO, INDIGO_T),
    "QLY":  ("Qualys Sync",        AMBER,  AMBER_T),
}

# Story type tags  (fill, text)
STYPE = {
    "Story":   (RGBColor(0xE8, 0xF4, 0xEB), RGBColor(0x1B, 0x6B, 0x2E)),
    "Enabler": (RGBColor(0xE3, 0xF0, 0xFB), RGBColor(0x14, 0x5C, 0xAD)),
}

EMU_W, EMU_H = Inches(13.333), Inches(7.5)
FONT = "Segoe UI"

# ─────────────────────────────────────────────────── SPRINT DATA
# Each story tuple: (type, local_id, description, owner)
# Feature header: id, ws, name (shown in feature group row)
# gates: one-line CO6 note shown under the sprint header
SPRINT_DATA = [
    {
        "code": "3.1", "dates": "Aug 5 – Aug 18",
        "gates": "No CO6 gate — delivery enablement sprint  |  test code freeze Aug 5–15 (no PROD deploys)",
        "features": [
            {"id": "1516993", "ws": "NET",
             "name": "Automated Credentialed Discovery Live — All Network Device Types  ·  CO6 Aug 31",
             "stories": [
                 ("Enabler", "ND-1", "Configure SNMP/SSH credential records for all 6 device types (Routers, Switches, Firewalls, LBs, WAPs, Controllers)", "Stan Tomberg"),
                 ("Enabler", "ND-2", "Adjust discovery config + device config; re-parent 1402572, 1402574, 1459721 (SNMP/MID pilot) to this feature", "Stan Tomberg"),
             ]},
            {"id": "1517650", "ws": "SM",
             "name": "Silver-Tier Service Maps (App→Infra) + ≥75% Business-Service Inventory  ·  CO6 Aug 31",
             "stories": [
                 ("Enabler", "SM-E", "Lock before PI: secure app-owner list, finalize Silver/Gold tier app lists, confirm discovery method", "Tanzeel Rehman"),
                 ("Story",   "SM-1", "Gather + Build committed Silver batch (app→infra, discovery-side; feasible under test freeze Aug 5–15)", "Tanzeel / Vinay"),
             ]},
            {"id": "1517065", "ws": "QLY",
             "name": "Activate ServiceNow → Qualys Attribute Sync (PROD)  ·  CO6 Sep 30",
             "stories": [
                 ("Enabler", "Q-E",  "Confirm Qualys plug-in landed (1465952); re-scope 1428704 to SN→Qualys direction; rename parent feature", "Stan Tomberg"),
                 ("Story",   "Q-1",  "Install Qualys plugin Dev/Test/Prod (1428703); design field-mapping & sync schedule for owner, support group, SOX flag", "Stan Tomberg"),
             ]},
            {"id": "1517029", "ws": "CERT",
             "name": "Certify Computers  [doc-only prep — build starts Sprint 3.2]  ·  CO6 Sep 30",
             "stories": [
                 ("Story", "CC-1", "Document Computer certification process flow off 1480114 gap plan — doc-only; no PROD deploy during freeze", "Bhushan Salsekar"),
             ]},
            {"id": "1517032", "ws": "CERT",
             "name": "Certify Servers  [doc-only prep — build starts Sprint 3.2]  ·  CO6 Sep 30",
             "stories": [
                 ("Story", "SV-1", "Document Server certification process flow off 1480112 gap plan — doc-only; resolve `environment` Mandatory ruling (DEP-7)", "Bhushan Salsekar"),
             ]},
        ]
    },
    {
        "code": "3.2", "dates": "Aug 19 – Sep 1",
        "gates": "CO6 gate Aug 31 — Automated Credentialed Discovery Live  +  Silver Service Maps  +  ≥75% Business-Service Inventory",
        "features": [
            {"id": "1516993", "ws": "NET",
             "name": "Automated Credentialed Discovery Live — All Network Device Types  ·  ✅ CO6 Aug 31",
             "stories": [
                 ("Story",   "ND-3", "Deploy + validate discovery at scale across all 6 device types; zero failed authentications confirmed", "Stan Tomberg"),
                 ("Enabler", "ND-4", "Configure discovery schedules on defined intervals; confirm CMDB auto-updates each cycle with no manual intervention", "Stan Tomberg"),
             ]},
            {"id": "1517650", "ws": "SM",
             "name": "Silver-Tier Service Maps (App→Infra) + ≥75% Business-Service Inventory  ·  ✅ CO6 Aug 31",
             "stories": [
                 ("Story", "SM-2", "Validate + Publish Silver batch; owner sign-off; inventory reconciliation to ≥75% business-service inventory", "Tanzeel / Vinay"),
             ]},
            {"id": "1517065", "ws": "QLY",
             "name": "Activate ServiceNow → Qualys Attribute Sync (PROD)  ·  CO6 Sep 30",
             "stories": [
                 ("Enabler", "Q-2", "Build SN→Qualys config: field-mapping for CI owner, support group, SOX flag; transform maps; scheduled sync job", "Stan Tomberg"),
             ]},
            {"id": "1517029", "ws": "CERT",
             "name": "Certify Computers — CMDB Data Certification  ·  CO6 Sep 30",
             "stories": [
                 ("Enabler", "CC-2", "Build Computer certification policies/rules to PROD (post-freeze, on/after Aug 15); configure attestation rules + task routing", "Bhushan Salsekar"),
                 ("Enabler", "CC-3", "Stand up Computer certification tracking dashboard (coverage %, outstanding gaps, live refresh)", "Kiran Dhobale"),
             ]},
            {"id": "1517032", "ws": "CERT",
             "name": "Certify Servers — CMDB Data Certification  ·  CO6 Sep 30",
             "stories": [
                 ("Enabler", "SV-2", "Build Server certification policies/rules to PROD (resolve `environment` Mandatory ruling before build — DEP-7)", "Bhushan Salsekar"),
                 ("Enabler", "SV-3", "Stand up Server certification tracking dashboard (reconcile 3,917 vs 15,218 active count — DEP-5)", "Kiran Dhobale"),
             ]},
        ]
    },
    {
        "code": "3.3", "dates": "Sep 2 – Sep 15",
        "gates": "No CO6 gate this sprint — builds toward Sep 30  |  test freeze lifted; all PROD deployments now unblocked",
        "features": [
            {"id": "1517005", "ws": "NET",
             "name": "Mandatory Attribute Population via Discovery — Network Devices  ·  CO6 Sep 30",
             "stories": [
                 ("Story",   "ND-5", "Define mandatory attribute set for Network Devices with governance (Josh Sterling / Adam Gross, CCB Network Class Manager)", "Stan Tomberg"),
                 ("Enabler", "ND-6", "Map discovery output → mandatory attributes per device type; remediate blank mandatory fields; validate none-blank", "Stan Tomberg"),
             ]},
            {"id": "1517655", "ws": "SM",
             "name": "Gold-Tier Service Maps (Service→App) + Silver Validation Pass  ·  CO6 Sep 30",
             "stories": [
                 ("Story", "SM-3", "Build Gold-tier service maps (service→app layer) per app; owner-validated; teams enabled", "Tanzeel / Vinay"),
             ]},
            {"id": "1517065", "ws": "QLY",
             "name": "Activate ServiceNow → Qualys Attribute Sync (PROD)  ·  CO6 Sep 30",
             "stories": [
                 ("Story", "Q-3", "End-to-end test of SN→Qualys sync in non-prod; all 3 fields sync correctly; zero manual handoffs confirmed", "Stan Tomberg"),
             ]},
            {"id": "1517029", "ws": "CERT",
             "name": "Certify Computers — CMDB Data Certification  ·  CO6 Sep 30",
             "stories": [
                 ("Story", "CC-4", "Run Computer certification cycle; monitor completeness on dashboard; drive to 90% coverage target; escalate non-responses", "Bhushan Salsekar"),
             ]},
            {"id": "1517032", "ws": "CERT",
             "name": "Certify Servers — CMDB Data Certification  ·  CO6 Sep 30",
             "stories": [
                 ("Story", "SV-4", "Run Server certification cycle; monitor completeness on dashboard; drive to 90% coverage target; escalate non-responses", "Bhushan Salsekar"),
             ]},
            {"id": "1517037", "ws": "CERT",
             "name": "Certify Databases  [process doc starts 3.3; build in 3.4]  ·  CO6 Oct 30",
             "stories": [
                 ("Story", "DB-1", "Document Database certification process flow (resolve attribute-set discrepancy: slide vs. dashboard — CP-3 blocker — DEP-3)", "Bhushan Salsekar"),
             ]},
        ]
    },
    {
        "code": "3.4", "dates": "Sep 16 – Sep 29",
        "gates": "CO6 gate Sep 30 — Qualys Sync PROD  ·  Certify Computers  ·  Certify Servers  ·  Gold Service Maps + Silver Validation",
        "features": [
            {"id": "1517037", "ws": "CERT",
             "name": "Certify Databases — CMDB Data Certification  ·  CO6 Oct 30",
             "stories": [
                 ("Enabler", "DB-2", "Build Database certification policies/rules to PROD (scoped to reconciled active DB instance count)", "Bhushan Salsekar"),
                 ("Enabler", "DB-3", "Stand up Database certification tracking dashboard (watch Oracle/KY visibility gap — DEP-4)", "Kiran Dhobale"),
             ]},
            {"id": "1517040", "ws": "CERT",
             "name": "Certify Network Devices — CMDB Data Certification  ·  CO6 Oct 30",
             "stories": [
                 ("Story",   "NW-1", "⚠ Net-new audit spike: define Network Device audit scope + gap baseline (no prior spike exists for this class)", "Stan Tomberg"),
                 ("Story",   "NW-2", "Document Network Device certification process flow (after NW-1; depends on Obj 4 mandatory attributes)", "Bhushan Salsekar"),
             ]},
            {"id": "1517029", "ws": "CERT",
             "name": "Certify Computers — final: training  ·  ✅ CO6 Sep 30 done by Sep 29",
             "stories": [
                 ("Story", "CC-5", "Deliver Computer certification training to CI owners; office hours; quick-reference job aid — CO6 training artifact", "Joe Dames / M. Vazquez"),
             ]},
            {"id": "1517032", "ws": "CERT",
             "name": "Certify Servers — final: training  ·  ✅ CO6 Sep 30 done by Sep 29",
             "stories": [
                 ("Story", "SV-5", "Deliver Server certification training to CI owners; office hours; quick-reference job aid — CO6 training artifact", "Joe Dames / M. Vazquez"),
             ]},
            {"id": "1517655", "ws": "SM",
             "name": "Gold-Tier Maps + Silver Validation Pass — final  ·  ✅ CO6 Sep 30 done by Sep 29",
             "stories": [
                 ("Story", "SM-4", "Gold-tier owner sign-off + Silver re-validation pass; 15 Silver + Gold complete; teams enabled — CO6 Sep 30 gate", "Tanzeel"),
             ]},
            {"id": "1517065", "ws": "QLY",
             "name": "SN → Qualys Attribute Sync — final: PROD cutover  ·  ✅ CO6 Sep 30 done by Sep 29",
             "stories": [
                 ("Enabler", "Q-4", "PROD cutover + go-live validation; confirm sync active on schedule, all 3 fields, zero manual handoffs — CO6 Sep 30", "Stan Tomberg"),
             ]},
        ]
    },
    {
        "code": "3.5", "dates": "Sep 30 – Oct 13",
        "gates": "No new CO6 gate this sprint — builds toward Oct 30 gates",
        "features": [
            {"id": "1356646", "ws": "NET",
             "name": "Network Inventory Coverage Reconciliation & Owner Validation (≥90%)  ·  CO6 Oct 30",
             "stories": [
                 ("Story",   "ND-7", "Gap analysis: discovered network inventory vs. authoritative business-owner device list; quantify shortfall per type", "Stan Tomberg"),
                 ("Enabler", "ND-8", "Close coverage gaps (credential remediation / subnet scope expansion); build ≥90% coverage metric dashboard", "Stan Tomberg"),
             ]},
            {"id": "1518000", "ws": "SM",
             "name": "Remaining Contractor-Managed Silver Maps + All-Silver Service→App Layer  ·  CO6 Oct 30",
             "stories": [
                 ("Story", "SM-5", "Complete remaining Contractor-managed Silver apps (app→infra layer); owner-validated per app", "Vinay / Tanzeel"),
                 ("Story", "SM-6", "Build service→app layer for all Silver-tier apps; owner-validated; teams enabled", "Tanzeel"),
             ]},
            {"id": "1517037", "ws": "CERT",
             "name": "Certify Databases — CMDB Data Certification  ·  CO6 Oct 30",
             "stories": [
                 ("Story", "DB-4", "Run Database certification cycle; monitor completeness; drive to 90% target; escalate non-responses per process", "Bhushan Salsekar"),
             ]},
            {"id": "1517040", "ws": "CERT",
             "name": "Certify Network Devices — CMDB Data Certification  ·  CO6 Oct 30",
             "stories": [
                 ("Enabler", "NW-3", "Build Network Device certification policies to PROD (depends on Obj 4 mandatory attributes populated — Sep 30 prerequisite)", "Bhushan Salsekar"),
                 ("Enabler", "NW-4", "Stand up Network Device certification tracking dashboard", "Kiran Dhobale"),
                 ("Story",   "NW-5", "Run Network Device certification cycle; monitor completeness on dashboard; drive to 90% target", "Bhushan Salsekar"),
             ]},
        ]
    },
    {
        "code": "3.6 IP", "dates": "Oct 14 – Oct 27",
        "gates": "CO6 gate Oct 30 — Certify Databases  ·  Certify Network Devices  ·  Coverage ≥90%  ·  Remaining Silver Maps",
        "features": [
            {"id": "1517037", "ws": "CERT",
             "name": "Certify Databases — final: training + sign-off  ·  ✅ CO6 Oct 30",
             "stories": [
                 ("Story", "DB-5", "Deliver Database certification training to CI owners; training artifact satisfies CO6 Oct 30 Databases gate", "Joe Dames / M. Vazquez"),
             ]},
            {"id": "1517040", "ws": "CERT",
             "name": "Certify Network Devices — final: training + sign-off  ·  ✅ CO6 Oct 30",
             "stories": [
                 ("Story", "NW-6", "Deliver Network Device certification training to CI owners; training artifact satisfies CO6 Oct 30 Network Devices gate", "Joe Dames / M. Vazquez"),
             ]},
            {"id": "1356646", "ws": "NET",
             "name": "Network Inventory Coverage Reconciliation — final: owner sign-off  ·  ✅ CO6 Oct 30",
             "stories": [
                 ("Story", "ND-9", "Business-owner validation + sign-off confirming ≥90% network device coverage against authoritative inventory — CO6 Oct 30", "Stan Tomberg"),
             ]},
            {"id": "1518000", "ws": "SM",
             "name": "Remaining Silver + All-Silver Service→App Layer — final: sign-off  ·  ✅ CO6 Oct 30",
             "stories": [
                 ("Story", "SM-7", "Owner validation sign-off for remaining Contractor-managed Silver + service→app layer for all Silver — CO6 Oct 30", "Tanzeel"),
             ]},
        ]
    },
]

# Program board features (same 11 as the features deck)
FEATURES = [
    dict(id="1516993", ws="NET",  sprint="3.1", co6="Aug 31", short="Discovery Live — all device types"),
    dict(id="1517005", ws="NET",  sprint="3.3", co6="Sep 30", short="Mandatory Attribute Population"),
    dict(id="1356646", ws="NET",  sprint="3.5", co6="Oct 30", short="Coverage Reconciliation ≥90%"),
    dict(id="1517650", ws="SM",   sprint="3.1", co6="Aug 31", short="Silver-Tier Maps + ≥75% Inventory"),
    dict(id="1517655", ws="SM",   sprint="3.3", co6="Sep 30", short="Gold-Tier Maps + Silver Validation"),
    dict(id="1518000", ws="SM",   sprint="3.5", co6="Oct 30", short="Remaining Silver + Svc→App"),
    dict(id="1517029", ws="CERT", sprint="3.2", co6="Sep 30", short="Certify Computers"),
    dict(id="1517032", ws="CERT", sprint="3.2", co6="Sep 30", short="Certify Servers"),
    dict(id="1517037", ws="CERT", sprint="3.4", co6="Oct 30", short="Certify Databases"),
    dict(id="1517040", ws="CERT", sprint="3.4", co6="Oct 30", short="Certify Network Devices"),
    dict(id="1517065", ws="QLY",  sprint="3.1", co6="Sep 30", short="Activate SN→Qualys Sync (PROD)"),
]

SPRINTS_BOARD = [
    ("3.1",    "Aug 5–18"),
    ("3.2",    "Aug 19–Sep 1"),
    ("3.3",    "Sep 2–15"),
    ("3.4",    "Sep 16–29"),
    ("3.5",    "Sep 30–Oct 13"),
    ("3.6 IP", "Oct 14–27"),
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
        ("4 objectives  ·  11 features  ·  ~40 stories  ·  6 sprints", 15, WHITE, True, False),
        ("CMDB / CSDM team focus area  —  a subset of CO6", 13, RGBColor(0xC9, 0xD6, 0xE6), False, False),
        (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
    ])
    textbox(s, Inches(0.87), Inches(6.5), Inches(11.6), Inches(0.4),
            [(DRAFT_NOTE, 10.5, RGBColor(0x7F, 0x8C, 0xA6), False, True)])


# ─────────────────────────────────────────────────── SLIDE 2 — PROGRAM BOARD

def add_board(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_header(s, "PI-3 Program Board — Features Across 6 Sprints",
                 "11 features · color-coded by objective · click sprint tabs for story detail")
    usable = 12.2
    gap = 0.10
    colw = (usable - 5 * gap) / 6.0
    top = 1.32
    hdr_h = 0.62
    chip_h = 0.76
    chip_gap = 0.07

    for ci, (code, dates) in enumerate(SPRINTS_BOARD):
        cx = 0.55 + ci * (colw + gap)
        is_ip = "IP" in code
        col_fill = MUTED if is_ip else DARK
        rect(s, Inches(cx), Inches(top), Inches(colw), Inches(hdr_h), col_fill)
        textbox(s, Inches(cx), Inches(top + 0.04), Inches(colw), Inches(hdr_h - 0.06),
                [("Sprint " + code, 11, WHITE, True, False),
                 (dates, 8, RGBColor(0xC9, 0xD6, 0xE6), False, False)],
                MSO_ANCHOR.MIDDLE, PP_ALIGN.CENTER)

        feats = [f for f in FEATURES if f["sprint"] == code]
        chip_top = top + hdr_h + 0.08
        if not feats:
            rect(s, Inches(cx), Inches(chip_top), Inches(colw), Inches(chip_h), LIGHT)
            textbox(s, Inches(cx), Inches(chip_top), Inches(colw), Inches(chip_h),
                    [("— none —", 8.5, MUTED, False, True)], MSO_ANCHOR.MIDDLE, PP_ALIGN.CENTER)
            continue
        for fi, f in enumerate(feats):
            cy = chip_top + fi * (chip_h + chip_gap)
            vivid = WS[f["ws"]][1]
            rounded_rect(s, Inches(cx), Inches(cy), Inches(colw), Inches(chip_h), vivid)
            textbox(s, Inches(cx + 0.06), Inches(cy + 0.04),
                    Inches(colw - 0.12), Inches(chip_h - 0.08),
                    [(f["short"], 7.5, WHITE, True, False),
                     ("ADO " + f["id"], 6.5, RGBColor(0xE0, 0xEC, 0xF8), False, False),
                     ("CO6 " + f["co6"], 7, WHITE, True, False)],
                    MSO_ANCHOR.MIDDLE, PP_ALIGN.LEFT)

    # legend
    lx, ly = 0.55, 6.68
    textbox(s, Inches(lx), Inches(ly - 0.02), Inches(1.1), Inches(0.28),
            [("Objective:", 9, TEXT, True, False)], MSO_ANCHOR.MIDDLE)
    lx += 1.15
    for key in ["NET", "SM", "CERT", "QLY"]:
        name, vivid, _ = WS[key]
        rect(s, Inches(lx), Inches(ly + 0.01), Inches(0.22), Inches(0.22), vivid)
        textbox(s, Inches(lx + 0.28), Inches(ly - 0.02), Inches(2.7), Inches(0.28),
                [(name, 9, TEXT, False, False)], MSO_ANCHOR.MIDDLE)
        lx += 3.0


# ─────────────────────────────────────────────────── SLIDES 3–8 — SPRINT DETAIL

def add_sprint_detail(prs, blank, sd):
    s = prs.slides.add_slide(blank)
    code  = sd["code"]
    dates = sd["dates"]
    gates = sd["gates"]

    # count total rows: 1 header + N feature groups + sum of stories
    n_feat = len(sd["features"])
    n_stories = sum(len(f["stories"]) for f in sd["features"])
    n_rows = 1 + n_feat + n_stories   # col-header + feature groups + story rows

    slide_header(
        s,
        f"Sprint {code}  —  {dates}",
        gates
    )

    # table geometry
    tbl_top  = Inches(1.27)
    tbl_left = Inches(0.55)
    tbl_w    = Inches(12.2)
    avail_h  = Inches(5.75)
    tbl_h    = avail_h

    # column widths: ID | Type | Description | Owner
    COL_W = [Inches(0.72), Inches(0.82), Inches(8.1), Inches(2.56)]

    t = s.shapes.add_table(n_rows, 4, tbl_left, tbl_top, tbl_w, tbl_h).table
    for j, wdt in enumerate(COL_W):
        t.columns[j].width = wdt

    # column header row
    hdr_labels = ["ID", "Type", "Story / Enabler Description", "Owner"]
    for j, lbl in enumerate(hdr_labels):
        algn = PP_ALIGN.LEFT if j == 2 else PP_ALIGN.CENTER
        _tcell(t, 0, j, lbl, 9.5, WHITE, True, algn, DARK, MSO_ANCHOR.MIDDLE)

    row = 1
    for feat in sd["features"]:
        vivid = WS[feat["ws"]][1]
        # feature group row — merge all 4 columns
        t.cell(row, 0).merge(t.cell(row, 3))
        label = f"ADO {feat['id']}  ·  {feat['name']}  ·  {WS[feat['ws']][0]}"
        _tcell(t, row, 0, label, 9, WHITE, True, PP_ALIGN.LEFT, vivid, MSO_ANCHOR.MIDDLE)
        row += 1

        for stype, sid, sdesc, sowner in feat["stories"]:
            fill = LIGHT if row % 2 == 0 else WHITE
            tf, tc = STYPE.get(stype, (LIGHT, TEXT))
            _tcell(t, row, 0, sid,    9, ACCENT, True,  PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 1, stype,  8, tc,     True,  PP_ALIGN.CENTER, tf,   MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 2, sdesc,  9, TEXT,   False, PP_ALIGN.LEFT,   fill, MSO_ANCHOR.MIDDLE)
            _tcell(t, row, 3, sowner, 8.5, MUTED, False, PP_ALIGN.CENTER, fill, MSO_ANCHOR.MIDDLE)
            row += 1

    # draft note below table
    note_y = tbl_top + tbl_h + Inches(0.06)
    textbox(s, tbl_left, note_y, tbl_w, Inches(0.28),
            [(DRAFT_NOTE, 8.5, MUTED, False, True)])


# ─────────────────────────────────────────────────── BUILD + SAVE

def build_deck():
    prs = Presentation()
    prs.slide_width  = EMU_W
    prs.slide_height = EMU_H
    blank = prs.slide_layouts[6]

    add_title(prs, blank)
    add_board(prs, blank)
    for sd in SPRINT_DATA:
        add_sprint_detail(prs, blank, sd)

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
out  = os.path.join(here, f"PI3-Sprint-Stories-Plan-{EDITION}.pptx")
save_safe(build_deck(), out)
