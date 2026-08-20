"""
CMDB CI Retirement Governance deck - response to stakeholder concerns about the
Computer & Server record cleanup (see cmdb-cleanup-root-cause-response-2026-07-23.md).

Narrative: how the CMDB gets initially populated (import -> credentialless
discovery -> credentials/subnets validated -> horizontal discovery -> cleanup ->
baseline), why cleanup is a defined stage in that journey (not an anomaly), what
actually happened in the July cleanup, the root cause, responses to the concerns
raised, safeguards already in place, and the go-forward governed lifecycle policy
(Identify -> Notify -> Approve -> Advance Notice -> Implement) gating every future
retirement.

Matches the house deck style (see build_audit_readiness_deck.py).

Single source of truth. Edit CONTENT, then run:
    python build_ci_retirement_governance_deck.py
Output:
    CMDB-CI-Retirement-Governance-<EDITION>.pptx
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
EDITION   = "2026-08-04"
TITLE     = "CMDB Server & Computer Cleanup"
SUBTITLE  = "Process, Root Cause, and Go-Forward Governance"
TAGLINE   = "Restoring Trust Through Transparency and Control"
AUTHOR    = "Manuel Vazquez  -  Scrum Master, CMDB-CSDM"
FOOTLABEL = "PPL CMDB-CSDM  |  CI Retirement Governance  -  Aug 4, 2026"

JOURNEY_STAGES = [
    ("1 - Manual Import", "Legacy tools & existing sources", False),
    ("2 - Credentialless Discovery", "Unauthenticated network scan", False),
    ("3 - Credentials & Subnets Validated", "The scope gate", False),
    ("4 - Horizontal Discovery", "Deep, authenticated scan", False),
    ("5 - Cleanup", "Retire unconfirmed pre-scope CIs", True),
    ("6 - Baseline", "Locked, trustworthy starting point", False),
]

LIFECYCLE_STEPS = [
    ("Identify", "CMDB Health criteria (staleness) - explicitly excludes non-discoverable in-scope assets like OT/SCADA"),
    ("Notify", "Automated workflow alerts affected stakeholders & owners - no silent state changes"),
    ("Approve", "Explicit sign-off required from responsible stakeholders & SMEs before proceeding"),
    ("Advance Notice", "Issued before implementation - time for downstream teams to decommission cleanly"),
    ("Implement", "Change executed only after every gate above is satisfied"),
]

WHY_CARDS = [
    ("What happened",
     "A one-time cleanup retired Computer and Server records that were loaded into the CMDB from legacy sources as an initial starting point, before ServiceNow Discovery scope was finalized."),
    ("The concern raised",
     "Active operational assets may have been caught in that cleanup, with risk to data integrity, operations, governance, and compliance."),
    ("What this deck covers",
     "How the CMDB gets populated, why cleanup is a defined stage in that process, what actually happened, the root cause, and the governance controls now gating every future retirement."),
]

IMPORT_DISCOVERY_CARDS = [
    ("1 - Manual Import",
     "Before any automated scanning starts, the CMDB is seeded with what already exists - exports from tools like SCCM, prior inventory spreadsheets, other management platforms, vendor asset lists. Gives a starting population, but it is inherently stale and incomplete."),
    ("2 - Credentialless Discovery",
     "An unauthenticated network scan identifies live IPs and does basic fingerprinting. Answers one question: what is out there that we do not already know about? Needs zero access approvals - fast, but shallow."),
]

SCOPE_GATE_STATEMENT = "Discovery only ever covers subnets explicitly in scope."
SCOPE_GATE_BULLETS = [
    "Before deeper access is granted, three things must be locked down: which subnets are in scope, the right credentials for each platform, and that those credentials validate with zero failed logins on a sample.",
    "This step depends on security teams and server owners granting access - not on CMDB tooling.",
    "This is the crux of the root cause: many subnets - including those hosting OT, SCADA, and NERC-related devices - are intentionally out of scope, by design, not by oversight.",
]

BASELINE_BULLETS = [
    "Horizontal discovery logs into every in-scope server and pulls real configuration data - this is what makes CMDB data trustworthy instead of an import snapshot.",
    "A baseline is supposed to represent ground truth. Before it is locked, every CI that discovery did NOT confirm gets retired - not deleted - so the starting number is not inflated by records that no longer exist or were never in scope.",
    "Retiring unconfirmed pre-scope records before baseline is a defined step in this process - not an ad-hoc or erroneous action.",
]

WHAT_HAPPENED_BULLETS = [
    "A single, one-time query identified and retired the qualifying records - not an automated or recurring process writing to the CMDB on a schedule.",
    "Criteria: records not already Retired whose Discovery Source was a legacy or manual origin (ImportSet, iTeam, Manual Entry, CherWell KY, CherWell PA, or empty).",
    "All records meeting the criteria were retired, across both the Computer and Server classes.",
    "The action was reviewed with key stakeholders in advance - the CMDB team did not do this unilaterally.",
]

ROOT_CAUSE_BULLETS = [
    "Initial CMDB loads were bulk collections from existing sources, imported as a starting point before Discovery scope was finalized - never validated for scope when they entered the CMDB.",
    "ServiceNow Discovery is scoped to specific, prescribed subnets. Multiple subnets - including those hosting OT, SCADA, and NERC-related devices - are intentionally out of scope.",
    "Retirement logic based on the absence of active discovery does not act on those out-of-scope assets, because they were never in the discovered inventory to begin with.",
    "NERC CIP is currently out of scope for this CMDB effort; a separate, parallel initiative is evaluating NERC-specific solutions.",
]

CONCERNS_1 = [
    ("Active CIs automatically retired",
     "Done by a one-time script, not an automated or recurring rule. Reviewed with key stakeholders beforehand, not unilaterally."),
    ("Potential widespread / undiscovered impact",
     "Retired records were unvalidated pre-scope imports, not authoritatively discovered assets. Any confirmed as a legitimate in-scope asset is restored immediately."),
    ("Communication / stakeholder awareness",
     "The cleanup was reviewed with key stakeholders. Communication is deliberately staged: key stakeholders now to stabilize the baseline, then operational teams as it is confirmed."),
    ("Operational risk (monitoring alerts)",
     "Where a retired record was still referenced downstream, restoring it resolves the discrepancy. Over 40 records have already been restored this way."),
]

CONCERNS_2 = [
    ("OT / SCADA / CIP assets are different",
     "Agreed - this is central. Those assets sit on out-of-scope subnets, are not discovered, and are not maintained in the CMDB. OT and CIP are handled by a parallel effort."),
    ("Insufficient retirement controls",
     "Agreed. Establishing a governed CMDB Health and lifecycle policy - staleness-based candidates, automated notification, explicit approval, advance notice (see Go-Forward Governance)."),
    ("Compliance / NERC CIP",
     "NERC CIP is out of scope today, and the CMDB is not its system of record. A parallel initiative owns NERC-specific solutions and governance."),
    ("Root cause & remediation",
     "Root cause: unvalidated pre-scope legacy imports, plus a CMDB scope narrower than assumed. Remediation: the governed CMDB Health retirement policy."),
]

SAFEGUARDS = [
    ("Retired ≠ Deleted", "Every retired record is fully recoverable. No data is lost."),
    ("One-Time, Not Recurring", "A baseline stabilization action - not a standing automated rule writing to the CMDB on a schedule."),
    ("40+ Records Restored", "Any record confirmed as a legitimate in-scope asset has been restored on request - already proven in practice."),
]

GOVERNANCE_BULLETS = [
    "Policy requirements will be defined with stakeholder input.",
    "Formally approved by the Change Control Board (CCB) - chaired by Josh Sterling - before any development or implementation.",
    "The policy will comply with all existing change, configuration management, and governance processes.",
]
GOVERNANCE_STATEMENT = "No future retirement bypasses this gate."

NEXT_STEPS = [
    "Define the CMDB Health and retirement lifecycle policy with stakeholder input (staleness criteria, automated notification, explicit approval, advance notice).",
    "Submit the policy to the CCB for approval before development.",
    "Continue restoring any record identified as a legitimate in-scope asset (40+ done so far).",
    "Keep stabilizing the in-scope CMDB baseline, and widen communication as it firms up.",
]

# ---------------------------------------------------------------------------
# THEME  (matches build_audit_readiness_deck.py)
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
RULE   = RGBColor(0xDD, 0xE3, 0xEA)

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


def cell(t, i, j, lines, size, color, bold=False, align=PP_ALIGN.LEFT, fill=None, anchor=None):
    c = t.cell(i, j)
    if fill is not None:
        c.fill.solid(); c.fill.fore_color.rgb = fill
    if anchor is not None:
        c.vertical_anchor = anchor
    tf = c.text_frame; tf.word_wrap = True
    if isinstance(lines, str):
        lines = [lines]
    for k, ln in enumerate(lines):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_before = Pt(0); p.space_after = Pt(2)
        r = p.add_run(); r.text = ln
        _set(r, size, color, bold)


def header(slide, title, subtitle=None):
    rect(slide, 0, 0, EMU_W, Inches(1.05), DARK)
    rect(slide, 0, Inches(1.05), EMU_W, Inches(0.06), ACCENT)
    textbox(slide, Inches(0.55), Inches(0.18), Inches(12.2), Inches(0.55),
            [(title, 24, WHITE, True, False)], MSO_ANCHOR.MIDDLE)
    if subtitle:
        textbox(slide, Inches(0.57), Inches(0.66), Inches(12.2), Inches(0.32),
                [(subtitle, 12, RGBColor(0xC9, 0xD6, 0xE6), False, False)], MSO_ANCHOR.MIDDLE)
    textbox(slide, Inches(0.55), Inches(7.08), Inches(10), Inches(0.32),
            [(FOOTLABEL, 9, MUTED, False, False)])


def bullet_list(slide, y, items, x=0.55, w=12.2, size=12.5, gap=0.68):
    yy = y
    for txt in items:
        rect(slide, Inches(x), Inches(yy + 0.09), Inches(0.12), Inches(0.12), ACCENT)
        textbox(slide, Inches(x + 0.28), Inches(yy), Inches(w - 0.28), Inches(gap - 0.05), [(txt, size, TEXT, False, False)])
        yy += gap
    return yy


def info_card(slide, y, label, body, color=ACCENT, h=1.05):
    rect(slide, Inches(0.55), Inches(y), Inches(0.14), Inches(h), color)
    textbox(slide, Inches(0.85), Inches(y), Inches(11.9), Inches(0.34), [(label, 14, DARK, True, False)])
    textbox(slide, Inches(0.85), Inches(y + 0.36), Inches(11.9), Inches(h - 0.36), [(body, 11.5, TEXT, False, False)])


def process_flow(slide, y, items, chip_h=1.35):
    x0, w_total, arrow_w = 0.55, 12.2, 0.28
    n = len(items)
    chip_w = (w_total - (n - 1) * arrow_w) / n
    x = x0
    for i, (title, caption, highlight) in enumerate(items):
        fill = ACCENT if highlight else LIGHT
        title_c = WHITE if highlight else DARK
        cap_c = RGBColor(0xC9, 0xD6, 0xE6) if highlight else MUTED
        rect(slide, Inches(x), Inches(y), Inches(chip_w), Inches(chip_h), fill)
        rect(slide, Inches(x), Inches(y), Inches(chip_w), Inches(0.07), RED if highlight else GREY)
        textbox(slide, Inches(x + 0.1), Inches(y + 0.16), Inches(chip_w - 0.2), Inches(0.55),
                [(title, 11.5, title_c, True, False)])
        textbox(slide, Inches(x + 0.1), Inches(y + 0.68), Inches(chip_w - 0.2), Inches(chip_h - 0.76),
                [(caption, 9, cap_c, False, False)])
        x += chip_w
        if i < n - 1:
            arr = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x), Inches(y + chip_h / 2 - 0.11), Inches(arrow_w), Inches(0.22))
            arr.fill.solid(); arr.fill.fore_color.rgb = GREY
            arr.line.fill.background(); arr.shadow.inherit = False
            x += arrow_w


def concerns_table(slide, y, rows):
    n = 1 + len(rows)
    t = slide.shapes.add_table(n, 2, Inches(0.55), Inches(y), Inches(12.2), Inches(0.4 + 1.0 * len(rows))).table
    t.columns[0].width = Inches(3.7)
    t.columns[1].width = Inches(8.5)
    cell(t, 0, 0, "Concern Raised", 11.5, WHITE, True, PP_ALIGN.LEFT, DARK, MSO_ANCHOR.MIDDLE)
    cell(t, 0, 1, "Response", 11.5, WHITE, True, PP_ALIGN.LEFT, DARK, MSO_ANCHOR.MIDDLE)
    t.rows[0].height = Inches(0.4)
    for i, (concern, response) in enumerate(rows, start=1):
        fill = LIGHT if i % 2 else WHITE
        cell(t, i, 0, concern, 11, DARK, True, PP_ALIGN.LEFT, fill, MSO_ANCHOR.MIDDLE)
        cell(t, i, 1, response, 10.5, TEXT, False, PP_ALIGN.LEFT, fill, MSO_ANCHOR.MIDDLE)
        t.rows[i].height = Inches(1.0)


def safeguard_chip(slide, x, y, w, h, title, body, color):
    rect(slide, Inches(x), Inches(y), Inches(w), Inches(h), LIGHT)
    rect(slide, Inches(x), Inches(y), Inches(w), Inches(0.08), color)
    textbox(slide, Inches(x + 0.18), Inches(y + 0.22), Inches(w - 0.36), Inches(0.5),
            [(title, 14, DARK, True, False)])
    textbox(slide, Inches(x + 0.18), Inches(y + 0.78), Inches(w - 0.36), Inches(h - 0.92),
            [(body, 10.5, TEXT, False, False)])


def big_statement(slide, y, text, color=ACCENT, h=0.9):
    rect(slide, Inches(0.55), Inches(y), Inches(12.2), Inches(h), color)
    textbox(slide, Inches(0.75), Inches(y), Inches(11.8), Inches(h),
            [(text, 20, WHITE, True, False)], MSO_ANCHOR.MIDDLE, PP_ALIGN.LEFT)


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
        ("A response to stakeholder concerns about the July 2026 Computer & Server record cleanup", 16, WHITE, True, False),
        ("How the CMDB is populated, what happened, why, and the controls now gating every future retirement", 13.5, RGBColor(0xC9, 0xD6, 0xE6), False, False),
        (AUTHOR, 12, RGBColor(0x9F, 0xB2, 0xCC), False, False),
    ])


def add_why(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Why We're Here", "Responding to concerns raised about the Computer & Server record cleanup")
    y = 1.5
    for label, body in WHY_CARDS:
        info_card(s, y, label, body, h=1.55)
        y += 1.85


def add_journey(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "How the CMDB Gets Populated", "The initial population journey - six defined stages, ending in a locked baseline")
    process_flow(s, 1.9, JOURNEY_STAGES, chip_h=1.9)
    textbox(s, Inches(0.55), Inches(4.3), Inches(12.2), Inches(0.6),
            [("Cleanup (stage 5) is a defined step in this journey - not an ad-hoc or erroneous event. It exists so the baseline reflects only confirmed, in-scope assets.",
              12.5, DARK, True, False)])


def add_import_discovery(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Stage Detail: Import + Credentialless Discovery", "The provisional starting point - before anything is validated against scope")
    cw = (12.2 - 0.3) / 2
    x = 0.55
    for title, body in IMPORT_DISCOVERY_CARDS:
        rect(s, Inches(x), Inches(1.5), Inches(cw), Inches(3.4), LIGHT)
        rect(s, Inches(x), Inches(1.5), Inches(cw), Inches(0.08), ACCENT)
        textbox(s, Inches(x + 0.2), Inches(1.75), Inches(cw - 0.4), Inches(0.5), [(title, 15, DARK, True, False)])
        textbox(s, Inches(x + 0.2), Inches(2.3), Inches(cw - 0.4), Inches(2.4), [(body, 11.5, TEXT, False, False)])
        x += cw + 0.3
    textbox(s, Inches(0.55), Inches(5.15), Inches(12.2), Inches(0.5),
            [("Both stages are inherently provisional - neither is validated against defined scope yet.", 12, MUTED, False, True)])


def add_scope_gate(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Credentials, Subnets, Validation", "The scope gate - the crux of the root cause")
    big_statement(s, 1.55, SCOPE_GATE_STATEMENT)
    bullet_list(s, 2.85, SCOPE_GATE_BULLETS, gap=0.85, size=13)


def add_baseline(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Horizontal Discovery → Why Cleanup Precedes Baseline", "Cleanup is how the baseline stays trustworthy")
    bullet_list(s, 1.6, BASELINE_BULLETS, gap=1.15, size=13.5)


def add_what_happened(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "What Actually Happened", "The facts of the July 2026 Computer & Server cleanup")
    bullet_list(s, 1.6, WHAT_HAPPENED_BULLETS, gap=1.0, size=13)


def add_root_cause(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Root Cause", "A scope gap - not a faulty process")
    bullet_list(s, 1.6, ROOT_CAUSE_BULLETS, gap=1.0, size=13)


def add_concerns(prs, blank, title, rows, part):
    s = prs.slides.add_slide(blank)
    header(s, "Concerns Raised → Responses (" + part + ")", "Direct responses to each concern raised by stakeholders")
    concerns_table(s, 1.55, rows)


def add_safeguards(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Safeguards Already in Place", "Controls that were in effect during the July cleanup")
    w = (12.2 - 2 * 0.3) / 3
    x = 0.55
    for title, body in SAFEGUARDS:
        safeguard_chip(s, x, 1.7, w, 2.6, title, body, GREEN)
        x += w + 0.3


def add_lifecycle(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Transition to a Managed, Governed Process", "Every future retirement runs through this gated lifecycle")
    steps = [(t, c, False) for t, c in LIFECYCLE_STEPS]
    process_flow(s, 1.9, steps, chip_h=2.6)
    textbox(s, Inches(0.55), Inches(4.85), Inches(12.2), Inches(0.6),
            [("No CI is retired silently. Identification, notification, approval, and notice all happen before implementation.",
              12.5, DARK, True, False)])


def add_governance(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Governance Authority", "Who approves this policy before it is built")
    bullet_list(s, 1.6, GOVERNANCE_BULLETS, gap=0.95, size=13.5)
    big_statement(s, 5.1, GOVERNANCE_STATEMENT, color=DARK, h=0.85)


def add_next_steps(prs, blank):
    s = prs.slides.add_slide(blank)
    header(s, "Next Steps", "What happens from here")
    y = 1.6
    for i, txt in enumerate(NEXT_STEPS, start=1):
        rect(s, Inches(0.55), Inches(y), Inches(0.5), Inches(0.5), ACCENT)
        textbox(s, Inches(0.55), Inches(y), Inches(0.5), Inches(0.5), [(str(i), 16, WHITE, True, False)], MSO_ANCHOR.MIDDLE, PP_ALIGN.CENTER)
        textbox(s, Inches(1.25), Inches(y), Inches(11.5), Inches(0.85), [(txt, 13, TEXT, False, False)], MSO_ANCHOR.MIDDLE)
        y += 1.15


def add_closing(prs, blank):
    s = prs.slides.add_slide(blank)
    rect(s, 0, 0, EMU_W, EMU_H, DARK)
    rect(s, 0, Inches(4.15), EMU_W, Inches(0.08), ACCENT)
    textbox(s, Inches(0.8), Inches(2.7), Inches(11.7), Inches(1.0), [("Questions & Discussion", 36, WHITE, True, False)])
    textbox(s, Inches(0.82), Inches(3.55), Inches(11.7), Inches(0.5), [(TAGLINE, 15, RGBColor(0x9F, 0xB2, 0xCC), False, True)])
    textbox(s, Inches(0.82), Inches(4.4), Inches(11.7), Inches(0.5), [(AUTHOR, 13, RGBColor(0xC9, 0xD6, 0xE6), False, False)])


def build_deck():
    prs = Presentation()
    prs.slide_width = EMU_W
    prs.slide_height = EMU_H
    blank = prs.slide_layouts[6]
    add_title(prs, blank)
    add_why(prs, blank)
    add_journey(prs, blank)
    add_import_discovery(prs, blank)
    add_scope_gate(prs, blank)
    add_baseline(prs, blank)
    add_what_happened(prs, blank)
    add_root_cause(prs, blank)
    add_concerns(prs, blank, "Concerns 1-2", CONCERNS_1, "1 of 2")
    add_concerns(prs, blank, "Concerns 3-4", CONCERNS_2, "2 of 2")
    add_safeguards(prs, blank)
    add_lifecycle(prs, blank)
    add_governance(prs, blank)
    add_next_steps(prs, blank)
    add_closing(prs, blank)
    return prs


def save_safe(prs, path):
    try:
        prs.save(path); print("Saved", os.path.basename(path), "-", len(prs.slides._sldIdLst), "slides")
    except PermissionError:
        base, ext = os.path.splitext(path)
        alt = base + "-new" + ext
        prs.save(alt); print("Target locked - saved to", os.path.basename(alt))


here = os.path.dirname(os.path.abspath(__file__))
save_safe(build_deck(), os.path.join(here, "CMDB-CI-Retirement-Governance-" + EDITION + ".pptx"))
