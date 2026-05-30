---
type: project-note
workspace: Work
project: Python-Automation
tags: [work, engineering, process, tool]
updated: 2026-05-30
summary: "Python-based document automation: PDF splitting by outline hierarchy (PyMuPDF + Ghostscript) and branded PowerPoint generation (python-pptx + MGB palette)."
base_confidence: 0.88
lifecycle: draft
lifecycle_changed: 2026-05-30
provenance: "Distilled from 2 Claude conversations (May 2026). Extracted from actual code design sessions."
---

# Python Document Automation

Patterns for automating document creation and transformation with Python.

## PDF Splitting by Outline Hierarchy

Split large PDFs into smaller files using the document's bookmark structure.

**Approach:**
- Use `PyMuPDF` (`fitz`) to parse the PDF outline (bookmarks)
- Treat **Level 2 headings** as folder names, **Level 3 headings** as individual PDF filenames
- Extract page ranges for each section and write sub-PDFs
- Post-process with **Ghostscript** to deduplicate embedded fonts (prevents size bloat when many sub-PDFs share the same fonts)

**Key libraries:**
```python
import fitz  # PyMuPDF — outline parsing, page extraction
# Then: gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite ... for font deduplication
```

**Ghostscript command for font dedup:**
```bash
gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
   -dSubsetFonts=true -dCompressFonts=true \
   -sOutputFile=output.pdf input.pdf
```

## PowerPoint Generation (python-pptx)

Automated slide generation with `python-pptx`, including the MGB brand palette.

**MGB (Mass General Brigham) Brand System:**
- Primary colors: MGB Blue, Teal, Charcoal
- Typography: Georgia (headings), Calibri (body)
- Use `RGBColor(r, g, b)` for exact brand colors

**Pattern:**
1. Load data from Excel (`openpyxl` or `pandas`)
2. Create/modify a `.pptx` template
3. Populate slide placeholders or draw shapes programmatically
4. Apply brand colors and fonts per MGB guidelines

**Key objects:**
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation("template.pptx")
slide = prs.slides[0]
tf = slide.shapes[0].text_frame
tf.paragraphs[0].font.color.rgb = RGBColor(0x00, 0x43, 0x87)  # MGB Blue
```

## Related Pages

- [[servicenow-analytics]] — the primary consumer of these PowerPoint reports
