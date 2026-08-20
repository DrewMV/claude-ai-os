"""
CMDB Audit Update - PI2 accomplishments and PI3 activities building on them.
Two slides: (1) PI2 governance/discovery/certification foundation, ratified and
closed; (2) PI3 certification + network discovery execution against that
baseline, including one flagged open gap (network device coverage/scheduling)
so the picture stays honest for an audit audience.

Matches the house deck style (see build_ci_retirement_governance_deck.py /
build_audit_readiness_deck.py).

Single source of truth. Edit CONTENT, then run:
    python build_pi2_pi3_audit_update_deck.py
Output:
    CMDB-Audit-Update-PI2-PI3-<EDITION>.pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------------------------------------------------------------------------
# CONTENT
# ---------------------------------------------------------------------------
EDITION   = "2026-08-20"
FOOTLABEL = "PPL CMDB-CSDM  |  CMDB Audit Update - PI2 Accomplishments & PI3 Activities  |  Aug 20, 2026"

TITLE     = "CMDB Audit Sync"
SUBTITLE  = "PI2 Accomplishments & PI3 Activities"
TAGLINE   = "Governance Ratified. Certification and Discovery in Execution."
AUTHOR    = "Manuel Vazquez  -  Product Owner, CMDB-CSDM"
MEETING_DATE = "August 20, 2026"

PI2_CARDS = [
    ("Approved Data Dictionary", "15 decisions · 4 classes",
     "CCB-ratified July 21, 2026 (CMP Stage 1): Business Application, Computer, Server, Database. Establishes source of truth, mandatory rules, and audit scope for the CMDB.",
     None),
    ("ESS-02 Alignment", "Closed",
     "Validation completed and the story closed. Computer and Server data dictionaries are explicitly scoped to ESS-02 audit requirements.",
     None),
    ("Automated Discovery - Computer & Server", "Live & Validated",
     "SCCM / Discovery source-of-truth precedence established for both classes. Credentials enabling discovery completed.",
     None),
    ("Data Certification Pilot - Business Application", "Deployed to PROD",
     "Pilot group identified; certification dashboard UAT signed off and live in PROD - validating the certification workflow ahead of expansion to all CI classes.",
     None),
]
PI2_BANNER = ("Result: a CCB-ratified governance baseline for Business Application, Computer, "
              "Server, and Database data - the foundation PI3 certification and discovery build on.")

PI3_BRIDGE = "Built on the PI2 baseline: ratified Data Dictionary · validated Discovery · closed ESS-02 alignment"

PI3_CARDS = [
    ("Certify Computers & Servers", "Gate: Sep 30",
     "Active in Sprint 3.2 (started Aug 19). Certification criteria are drawn directly from the CCB-ratified data dictionary.",
     None),
    ("Certify Databases & Network Devices", "Gate: Oct 30",
     "Planned for Sprint 3.4 - stories are already pulling forward into Sprint 3.2, ahead of schedule.",
     None),
    ("Network Device Auto Discovery", "Gate: Aug 31",
     "Credentialed discovery live and validated for Routers, Switches, and Firewalls - extending the Computer/Server discovery model to network devices.",
     None),
    ("Database Auto-Discovery - PI2 Carryover", "Credential Issue - Active",
     "Enhanced Database Discovery (MS-SQL/Oracle) continues from PI2 under Feature 1554951. Sprint 3.1 is actively resolving a Linux Discovery credential issue blocking DB host connectivity (8 pts, Active).",
     "amber"),
]
PI3_BANNER = ("CO6 Objectives 3 & 4 - every certification and discovery gate is measured "
              "against the PI2-ratified governance baseline.")

# ---------------------------------------------------------------------------
# THEME  (matches build_ci_retirement_governance_deck.py)
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

EMU_W, EMU_H = Inches(13.333), Inches(7.5)
FONT = "Segoe UI"


def _set(run, size, color, bold=False, italic=False):
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = FONT


def rect(slide, x, y, w, h, color):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
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
        r = p.add_run(); r.text = text
        _set(r, size, color, bold, italic)
    return tb


def header(slide, title, subtitle=None):
    rect(slide, 0, 0, EMU_W, Inches(1.05), DARK)
    rect(slide, 0, Inches(1.05), EMU_W, Inches(0.06), ACCENT)
    textbox(slide, Inches(0.55), Inches(0.18), Inches(12.2), Inches(0.55),
            [(title, 24, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
    if subtitle:
        textbox(slide, Inches(0.57), Inches(0.66), Inches(12.2), Inches(0.32),
                [(subtitle, 12, RGBColor(0xC9, 0xD6, 0xE6), False, False)], MSO_ANCHOR.MIDDLE)
    textbox(slide, Inches(0.55), Inches(7.1), Inches(10), Inches(0.3),
            [(FOOTLABEL, 9, MUTED, False, False)])


def stat_card(slide, x, y, w, h, title, stat, body, flag=None):
    accent = AMBER if flag == "amber" else ACCENT
    rect(slide, Inches(x), Inches(y), Inches(w), Inches(h), LIGHT)
    rect(slide, Inches(x), Inches(y), Inches(w), Inches(0.08), accent)
    textbox(slide, Inches(x + 0.22), Inches(y + 0.2), Inches(w - 0.44), Inches(0.42),
            [(stat, 18, accent, True, False)])
    textbox(slide, Inches(x + 0.22), Inches(y + 0.66), Inches(w - 0.44), Inches(0.5),
            [(title, 13.5, DARK, True, False)])
    textbox(slide, Inches(x + 0.22), Inches(y + 1.14), Inches(w - 0.44), Inches(h - 1.28),
            [(body, 10.5, TEXT, False, False)])


def bridge_line(slide, y, text):
    textbox(slide, Inches(0.55), Inches(y), Inches(12.2), Inches(0.4),
            [(text, 12.5, MUTED, False, True)])


def big_statement(slide, y, text, color=ACCENT, h=0.6):
    rect(slide, Inches(0.55), Inches(y), Inches(12.2), Inches(h), color)
    textbox(slide, Inches(0.8), Inches(y), Inches(11.7), Inches(h),
            [(text, 14.5, WHITE, True, False)], MSO_ANCHOR.MIDDLE, PP_ALIGN.LEFT)


def card_grid(slide, cards, grid_y, card_h, gap_x=0.3, gap_y=0.2):
    x0, w_total = 0.55, 12.2
    card_w = (w_total - gap_x) / 2
    positions = [
        (x0, grid_y),
        (x0 + card_w + gap_x, grid_y),
        (x0, grid_y + card_h + gap_y),
        (x0 + card_w + gap_x, grid_y + card_h + gap_y),
    ]
    for (title, stat, body, flag), (x, y) in zip(cards, positions):
        stat_card(slide, x, y, card_w, card_h, title, stat, body, flag)


# ---------------------------------------------------------------------------
# SLIDE BUILDERS
# ---------------------------------------------------------------------------
def add_title(prs, blank):
    s = prs.slides.add_slide(blank)
    rect(s, 0, 0, EMU_W, EMU_H, DARK)
    rect(s, 0, Inches(4.55), EMU_W, Inches(0.08), ACCENT)
    textbox(s, Inches(0.8), Inches(1.55), Inches(11.7), Inches(1.2), [(TITLE, 40, WHITE, True, False)])
    textbox(s, Inches(0.82), Inches(2.68), Inches(11.7), Inches(0.55), [(SUBTITLE, 19, RGBColor(0xC9, 0xD6, 0xE6), False, False)])
    textbox(s, Inches(0.82), Inches(3.28), Inches(11.7), Inches(0.5), [(TAGLINE, 15, RGBColor(0x9F, 0xB2, 0xCC), False, True)])
    textbox(s, Inches(0.82), Inches(4.75), Inches(11.7), Inches(1.6), [
        (MEETING_DATE, 16, WHITE, True, False),
        ("PI2 governance foundation ratified; PI3 certification and discovery execution underway", 13.5, RGBColor(0xC9, 0xD6, 0xE6), False, False),
        (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
    ])


def add_pi2_slide(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "PI2 - CMDB Audit Foundation",
           "Governance ratified, discovery validated, certification piloted")
    grid_y, card_h = 1.55, 2.15
    card_grid(s, PI2_CARDS, grid_y, card_h)
    big_statement(s, grid_y + 2 * card_h + 0.2 + 0.2, PI2_BANNER)


def add_pi3_slide(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "PI3 - Building on the PI2 Foundation",
           "CO6 Objectives 3 & 4 - certification and discovery execution against the ratified baseline")
    bridge_line(s, 1.4, PI3_BRIDGE)
    grid_y, card_h = 1.95, 1.95
    card_grid(s, PI3_CARDS, grid_y, card_h)
    big_statement(s, grid_y + 2 * card_h + 0.2 + 0.2, PI3_BANNER)


# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------
def main():
    prs = Presentation()
    prs.slide_width = EMU_W
    prs.slide_height = EMU_H
    blank = prs.slide_layouts[6]

    add_title(prs, blank)
    add_pi2_slide(prs, blank)
    add_pi3_slide(prs, blank)

    out = f"CMDB-Audit-Update-PI2-PI3-{EDITION}.pptx"
    prs.save(out)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
