"""
Build the PI-4 Implementation Plan appendix slide.

One standalone slide, to be appended behind slide 6 of
PI4-Objectives-Features-2026-10-14.pptx. The main deck is not modified.

Grid, colours and type are copied from slide 6 (Program Board) so the two read
as siblings. Sprint columns 4.1-4.7 sit at exactly the same x positions; a
narrow PI-3 IP column is added to the left of 4.1 to show requirements runways
that fall before the PI starts.

Phase bands:  Requirements/Spike (light tint) -> Build & Test (solid)
              -> Validate & Release (outlined)
Gate diamond: objective colour = on track, amber = tight, red = no margin.

Source data: pi4-implementation-plan-appendix.md
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

OUT = "PI4-Implementation-Plan-Appendix-2026-10-14.pptx"

# ---------------------------------------------------------------- palette ---
NAVY = RGBColor(0x1E, 0x27, 0x61)
INK = RGBColor(0x1A, 0x1A, 0x2E)
GREY = RGBColor(0x6B, 0x72, 0x80)
RULE = RGBColor(0xD5, 0xD9, 0xE2)
SHADE = RGBColor(0xED, 0xEF, 0xF4)
AMBER = RGBColor(0xB9, 0x77, 0x0E)
RED = RGBColor(0xC0, 0x39, 0x2B)

OBJ = {
    "net": RGBColor(0x1E, 0x27, 0x61),
    "map": RGBColor(0x0B, 0x6E, 0x7F),
    "adopt": RGBColor(0x9C, 0x6F, 0x15),
    "life": RGBColor(0x6D, 0x2E, 0x46),
}


def tint(c, pct):
    """Blend colour toward white. pct = share of the original colour."""
    return RGBColor(
        int(c[0] + (255 - c[0]) * (1 - pct)),
        int(c[1] + (255 - c[1]) * (1 - pct)),
        int(c[2] + (255 - c[2]) * (1 - pct)),
    )


# ------------------------------------------------------------------ layout ---
LBL_X, LBL_W = 0.50, 3.55
IP_X, IP_W = 4.15, 0.60
COL_W = 1.15
COL = {  # sprint -> x (identical to slide 6)
    "4.1": 4.75, "4.2": 5.90, "4.3": 7.05, "4.4": 8.20,
    "4.5": 9.35, "4.6": 10.50, "4.7": 11.65,
}
GRID_T, GRID_H = 1.45, 4.79
ROW_T = [2.22, 2.56, 2.89, 3.23, 3.56, 3.90, 4.23, 4.57, 4.90, 5.24, 5.57, 5.91]

SPRINTS = [
    ("4.1", "Oct 28 – Nov 10"), ("4.2", "Nov 11 – Nov 24"),
    ("4.3", "Nov 25 – Dec 8"), ("4.4", "Dec 9 – Dec 22"),
    ("4.5", "Dec 23 – Jan 5"), ("4.6", "Jan 6 – Jan 19"),
    ("4.7 IP", "Jan 20 – Feb 2"),
]

GATE_DEC31 = 9.94   # x of the Dec 31 diamond, as on slide 6
GATE_NOV30 = 7.39
GATE_JAN30 = 12.40
GATE_FEB2 = 12.65

# ---------------------------------------------------------------- the rows ---
# (deliverable, name, ado, objective, req, build, vr, gate_x, status)
# req / build / vr are (x, width) in inches; None = no window
ROWS = [
    ("D3", "15 Maps (1 of 3)", "1646517", "map",
     (IP_X, IP_W), (COL["4.1"], COL_W), (COL["4.2"], COL_W), GATE_NOV30, "tight"),
    ("D8", "CMDB Correctness", "1639335", "life",
     (IP_X, IP_W), (COL["4.1"], 2.30), (COL["4.3"], COL_W), GATE_DEC31, "ok"),
    ("D4", "15 Maps (2 of 3)", "1642237", "map",
     (COL["4.1"], COL_W), (COL["4.2"], COL_W), (COL["4.3"], COL_W), GATE_DEC31, "ok"),
    ("D9", "Non-Discoverable CI Interface", "1640795", "life",
     (COL["4.1"], COL_W), (COL["4.2"], COL_W), (COL["4.3"], COL_W), GATE_DEC31, "ok"),
    ("D7", "Adoption Campaign", "1639308", "adopt",
     (COL["4.1"], COL_W), (COL["4.2"], 5.75), None, GATE_JAN30, "none"),
    ("D6", "Stakeholder Notifications", "1642240", "map",
     (COL["4.2"], COL_W), (COL["4.3"], COL_W), (COL["4.4"], COL_W), GATE_DEC31, "tight"),
    ("D10", "Server Build Flow", "1640805", "life",
     (COL["4.2"], COL_W), (COL["4.3"], 2.30), (COL["4.6"], COL_W), GATE_FEB2, "ok"),
    ("D2", "Cisco Catalyst", "1639225", "net",
     (COL["4.2"], COL_W), (COL["4.3"], 2.30), (COL["4.6"], COL_W), GATE_FEB2, "ok"),
    ("D11", "Server Decommission Flow", "1640819", "life",
     (COL["4.3"], COL_W), (COL["4.4"], 3.45), (COL["4.7"], 0.90), GATE_FEB2, "none"),
    ("D5", "15 Maps (3 of 3)", "1642332", "map",
     (COL["4.4"], COL_W), (COL["4.6"], COL_W), (COL["4.7"], 0.90), GATE_FEB2, "none"),
    ("D12", "Service Map Update Item", "1640844", "life",
     (COL["4.4"], COL_W), (COL["4.6"], COL_W), (COL["4.7"], 0.90), GATE_FEB2, "none"),
    ("TBC", "Qualys", "1639239", "net",
     (COL["4.4"], COL_W), (COL["4.6"], 2.05), None, GATE_FEB2, "none"),
]

GATE_COLOUR = {"ok": None, "tight": AMBER, "none": RED}


# ----------------------------------------------------------------- helpers ---
def textbox(slide, x, y, w, h, runs, align=PP_ALIGN.LEFT, spacing=None):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if spacing:
            p.space_after = Pt(spacing)
        for text, size, bold, colour in line:
            r = p.add_run()
            r.text = text
            r.font.name = "Calibri"
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.color.rgb = colour
    return tb


def rect(slide, x, y, w, h, fill=None, line=None, lw=1.0):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                               Inches(w), Inches(h))
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(lw)
    s.shadow.inherit = False
    return s


def diamond(slide, x, y, size, colour):
    s = slide.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(x), Inches(y),
                               Inches(size), Inches(size))
    s.fill.solid()
    s.fill.fore_color.rgb = colour
    s.line.fill.background()
    s.shadow.inherit = False
    return s


def connector(slide, x1, x2, y, colour=RULE):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x1), Inches(y),
                               Inches(x2 - x1), Inches(0.01))
    s.fill.solid()
    s.fill.fore_color.rgb = colour
    s.line.fill.background()
    s.shadow.inherit = False
    return s


# ------------------------------------------------------------------- build ---
prs = Presentation()
prs.slide_width = Inches(13.3333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

# title block
tb = slide.shapes.add_textbox(Inches(0.50), Inches(0.33), Inches(12.30), Inches(0.55))
p = tb.text_frame.paragraphs[0]
r = p.add_run()
r.text = "PI-4 Implementation Plan — Phase Timeline"
r.font.name, r.font.size, r.font.bold = "Cambria", Pt(31), True
r.font.color.rgb = NAVY

textbox(slide, 0.52, 0.90, 12.30, 0.30, [[(
    "Appendix to slide 6  ·  bar colour = objective, as slide 6  ·  three phase bands "
    "per feature  ·  diamond marks the AP00288 gate, triangle the OCM sign-off  ·  "
    "requirements runway shown left of the PI where it falls in PI-3 IP",
    11.5, False, GREY)]])

textbox(slide, 0.50, 6.95, 12.30, 0.30, [[(
    "PPL CMDB-CSDM  |  PI-4 Implementation Plan  |  SOW AP00288  |  Oct 14, 2026",
    10, False, GREY)]])

# column shading: PI-3 IP (before the PI) and 4.5 (holiday)
rect(slide, IP_X, GRID_T, IP_W, GRID_H, fill=tint(NAVY, 0.07))
rect(slide, COL["4.5"], GRID_T, COL_W, GRID_H, fill=SHADE)

# column dividers + headers
textbox(slide, LBL_X, 1.48, LBL_W, 0.56, [[("Feature", 10, True, GREY)]])
rect(slide, IP_X, GRID_T, 0.008, GRID_H, fill=RULE)
textbox(slide, IP_X, 1.48, IP_W, 0.56,
        [[("PI-3 IP", 9, True, GREY)], [("Oct 14–27", 7.5, False, GREY)]])
for key, dates in SPRINTS:
    x = COL[key.split()[0]]
    rect(slide, x, GRID_T, 0.008, GRID_H, fill=RULE)
    textbox(slide, x, 1.48, COL_W, 0.56,
            [[(key, 10, True, NAVY)], [(dates, 10, False, NAVY)]])
rect(slide, IP_X, 2.07, 12.80 - IP_X, 0.01, fill=RULE)

# rows
for (deliv, name, ado, obj, req, build, vr, gate_x, status), y in zip(ROWS, ROW_T):
    c = OBJ[obj]
    textbox(slide, LBL_X, y, LBL_W, 0.34, [[
        (deliv + "  ", 9, True, c),
        (name + "   ", 9, False, INK),
        (ado, 8, False, GREY),
    ]])

    bar_y = y + 0.07
    rect(slide, req[0], bar_y, req[1], 0.20, fill=tint(c, 0.30))
    rect(slide, build[0], bar_y, build[1], 0.20, fill=c)
    end = build[0] + build[1]
    if vr:
        rect(slide, vr[0], bar_y, vr[1], 0.20, fill=RGBColor(0xFF, 0xFF, 0xFF),
             line=c, lw=1.25)
        end = vr[0] + vr[1]

    gate_c = GATE_COLOUR[status] or c
    if gate_x - end > 0.05:
        connector(slide, end, gate_x, y + 0.17,
                  RED if status == "none" else RULE)
    diamond(slide, gate_x, y + 0.10, 0.14, gate_c)

    if deliv == "D7":  # only confirmed OCM sign-off in scope today
        # sits in the gap between build end and gate — the window that does not exist
        s = slide.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE,
                                   Inches(11.92), Inches(bar_y + 0.02),
                                   Inches(0.15), Inches(0.15))
        s.fill.solid()
        s.fill.fore_color.rgb = c
        s.line.fill.background()
        s.shadow.inherit = False

# ------------------------------------------------------------------ legend ---
LY = 6.34


def swatch(x, kind, c, label, w):
    if kind == "tint":
        rect(slide, x, LY + 0.07, 0.26, 0.10, fill=tint(c, 0.30))
    elif kind == "solid":
        rect(slide, x, LY + 0.07, 0.26, 0.10, fill=c)
    elif kind == "outline":
        rect(slide, x, LY + 0.05, 0.26, 0.14,
             fill=RGBColor(0xFF, 0xFF, 0xFF), line=c, lw=1.25)
    elif kind == "diamond":
        diamond(slide, x + 0.05, LY + 0.04, 0.13, c)
    textbox(slide, x + 0.32, LY, w, 0.24, [[(label, 9, False, GREY)]])
    return x + 0.32 + w + 0.18


x = textbox(slide, LBL_X, LY, 0.70, 0.24,
            [[("Phase:", 9, True, GREY)]]) and LBL_X + 0.76
x = swatch(x, "tint", NAVY, "Requirements / Spike", 1.28)
x = swatch(x, "solid", NAVY, "Build & Test", 0.80)
x = swatch(x, "outline", NAVY, "Validate & Release", 1.18)
x = swatch(x, "diamond", NAVY, "gate on track", 0.92)
x = swatch(x, "diamond", AMBER, "tight (<10 days)", 1.05)
x = swatch(x, "diamond", RED, "no validation margin", 1.30)

textbox(slide, LBL_X, 6.64, 12.30, 0.28, [[
    ("Phase dates derived from the ADO sprint spans on slide 3 — requirements = "
     "one sprint ending where build starts; validate & release = one sprint after "
     "build ends. Sprint 4.5 treated as unavailable. ", 8.5, False, GREY),
    ("D7 and Qualys have no validate-and-release window at all; D11, D5 and D12 "
     "finish on their gate date. Tripwire has no ADO item and cannot be scheduled. "
     "December change-freeze dates unconfirmed.", 8.5, True, GREY),
]])

prs.save(OUT)
print("wrote", OUT)
