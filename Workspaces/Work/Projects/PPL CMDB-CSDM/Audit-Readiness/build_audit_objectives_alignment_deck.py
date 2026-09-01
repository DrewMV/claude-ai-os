"""
CMDB Governance & Lifecycle Advisory Review - status update structured against
Corporate Audit Services' own three engagement objectives (per the audit's
Scope & Objectives one-pager), rather than by PI2/PI3 delivery increments.

Same intent as CMDB-Audit-Update-PI2-PI3 (audit-facing progress update), but a
DIFFERENT deck: one slide per audit objective, so the walkthrough follows the
auditor's own framework instead of the delivery team's.

Matches the house deck style (see build_pi2_pi3_audit_update_deck.py).

Single source of truth. Edit CONTENT, then run:
    python build_audit_objectives_alignment_deck.py
Output:
    CMDB-Audit-Objectives-Alignment-<EDITION>.pptx
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
FOOTLABEL = "PPL CMDB-CSDM  |  CMDB Governance & Lifecycle Advisory Review - Status Update  |  Aug 20, 2026"

TITLE     = "CMDB Governance & Lifecycle Advisory Review"
SUBTITLE  = "Status Update Aligned to Audit Objectives"
TAGLINE   = "Data Completeness & Accuracy  -  Governance Structure  -  Stakeholder Engagement (OCM)"
AUTHOR    = "Manuel Vazquez  -  Product Owner, CMDB-CSDM"
MEETING_DATE = "August 20, 2026"

OBJ1_CARDS = [
    ("Approved Data Dictionary", "CCB-Ratified Jul 21",
     "CMP Stage 1 defines Mandatory / Audited attributes for all 4 core CI classes - the agreed standard for completeness and accuracy.",
     None),
    ("Data Certification Program", "4 CI Classes",
     "End-to-end process, PROD build, dashboards, and training. Computers & Servers gate Sep 30; Databases & Network Devices gate Oct 30.",
     None),
    ("Automated Discovery", "Computer, Server, Network - Live",
     "SCCM/Discovery precedence live for Computer & Server; credentialed discovery validated for Routers, Switches, and Firewalls.",
     None),
    ("Open Data Gaps", "2 Active Blockers",
     "Database discovery credential issue (Active, 8 pts) and network device coverage for 3 of 6 device types plus scheduling automation - both tracked toward their gates.",
     "amber"),
]
OBJ1_BANNER = ("Objective 1: management has a documented plan - a ratified Data Dictionary and an "
               "active Certification Program - and is executing it, with two known data-completeness gaps being tracked to closure.")

OBJ2_CARDS = [
    ("Change Control Board (CCB)", "Chair: Josh Sterling",
     "Standing governance authority. Ratifies attribute governance, ownership assignments, and audit scope for the CMDB data model.",
     None),
    ("Class Managers Assigned", "4 of 4 Core Classes",
     "Todd Dierksheide (Business App), Monica Green / Paul Becker (Computer), Ray Reuter (Server & Database) - named, accountable owners per class.",
     None),
    ("Configuration Management Plan (CMP)", "Stage 1 of 3 Ratified",
     "Stage 1 (Data Dictionary) ratified July 21. Stage 2 (Lifecycle & Health Targets) and Stage 3 (Governance Process & Controls, gate Sep 30) in progress.",
     None),
    ("CI Retirement Governance Policy", "Approval-Gated",
     "Identify - Notify - Approve - Advance Notice - Implement. A controlled, audit-trailed workflow for every future CI retirement, pending formal CCB approval.",
     None),
]
OBJ2_BANNER = ("Objective 2: a standing governance body, named class owners, and a staged CMP are in "
               "place - periodic data validation formalizes further as CMP Stage 2 and 3 land.")

OBJ3_CARDS = [
    ("Monthly CMDB Audit Sync", "Recurring - 3rd Thursday",
     "Standing communication cadence with PPL Audit and key stakeholders, confirmed ongoing since July 2026.",
     None),
    ("CCB Ratification Sessions", "Jul 21 Session Held",
     "Formal stakeholder review and approval events for governance artifacts, such as the Data Dictionary ratification.",
     None),
    ("Certification Training & Office Hours", "In Flight",
     "Kick-off, policy execution, monitoring, office hours, and feedback loops built into the certification rollout for each CI class.",
     None),
    ("Staged Communication Model", "Proven in Practice",
     "Used during the July cleanup response - key stakeholders engaged first, broader operational teams as the baseline stabilized.",
     None),
]
OBJ3_BANNER = ("Objective 3: recurring communication cadences and structured training/feedback loops "
               "are operating today, and were stress-tested during the July cleanup response.")

# ---------------------------------------------------------------------------
# THEME  (matches build_pi2_pi3_audit_update_deck.py)
# ---------------------------------------------------------------------------
DARK   = RGBColor(0x1F, 0x3A, 0x5F)
ACCENT = RGBColor(0x2E, 0x6D, 0xB4)
LIGHT  = RGBColor(0xF4, 0xF6, 0xF9)
TEXT   = RGBColor(0x2D, 0x2D, 0x2D)
MUTED  = RGBColor(0x6B, 0x72, 0x80)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
AMBER  = RGBColor(0xE0, 0x8A, 0x00)

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
            [(title, 22, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
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
            [(stat, 17, accent, True, False)])
    textbox(slide, Inches(x + 0.22), Inches(y + 0.64), Inches(w - 0.44), Inches(0.56),
            [(title, 13, DARK, True, False)])
    textbox(slide, Inches(x + 0.22), Inches(y + 1.18), Inches(w - 0.44), Inches(h - 1.32),
            [(body, 10, TEXT, False, False)])


def big_statement(slide, y, text, color=ACCENT, h=0.65):
    rect(slide, Inches(0.55), Inches(y), Inches(12.2), Inches(h), color)
    textbox(slide, Inches(0.8), Inches(y), Inches(11.7), Inches(h),
            [(text, 13.5, WHITE, True, False)], MSO_ANCHOR.MIDDLE, PP_ALIGN.LEFT)


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
    textbox(s, Inches(0.8), Inches(1.35), Inches(11.7), Inches(1.6), [(TITLE, 34, WHITE, True, False)])
    textbox(s, Inches(0.82), Inches(2.68), Inches(11.7), Inches(0.55), [(SUBTITLE, 19, RGBColor(0xC9, 0xD6, 0xE6), False, False)])
    textbox(s, Inches(0.82), Inches(3.28), Inches(11.7), Inches(0.5), [(TAGLINE, 14, RGBColor(0x9F, 0xB2, 0xCC), False, True)])
    textbox(s, Inches(0.82), Inches(4.75), Inches(11.7), Inches(1.6), [
        (MEETING_DATE, 16, WHITE, True, False),
        ("Corporate Audit Services engagement: CMDB Governance and Lifecycle Advisory Review", 13.5, RGBColor(0xC9, 0xD6, 0xE6), False, False),
        (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
    ])


def add_objective_slide(prs, blank, number, title, cards, banner):
    s = prs.slides.add_slide(blank)
    header(s, f"Audit Objective {number} - {title}",
           "Corporate Audit Services  |  CMDB Governance and Lifecycle Advisory Review")
    grid_y, card_h = 1.55, 2.15
    card_grid(s, cards, grid_y, card_h)
    big_statement(s, grid_y + 2 * card_h + 0.2 + 0.2, banner)


# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------
def main():
    prs = Presentation()
    prs.slide_width = EMU_W
    prs.slide_height = EMU_H
    blank = prs.slide_layouts[6]

    add_title(prs, blank)
    add_objective_slide(prs, blank, 1, "Data Completeness & Accuracy", OBJ1_CARDS, OBJ1_BANNER)
    add_objective_slide(prs, blank, 2, "Governance Structure & Ownership", OBJ2_CARDS, OBJ2_BANNER)
    add_objective_slide(prs, blank, 3, "Stakeholder Engagement & OCM", OBJ3_CARDS, OBJ3_BANNER)

    out = f"CMDB-Audit-Objectives-Alignment-{EDITION}.pptx"
    prs.save(out)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
