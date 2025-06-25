from docx.shared import RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def apply_style_to_run(run, style):
    """Apply font styling to a run based on a TextStyle or compatible object."""
    if not style:
        return
    font = run.font
    if style.bold is not None:
        font.bold = style.bold
    if style.italic is not None:
        font.italic = style.italic
    if style.font_color:
        font.color.rgb = RGBColor.from_string(style.font_color)

def set_paragraph_alignment(paragraph, align):
    """
    Set paragraph alignment based on string.

    This is the canonical alignment setter for all block types (table cells, rows, columns, tables, headings, text, etc).
    Args:
        paragraph: The python-docx Paragraph object to align.
        align: One of 'left', 'center', or 'right'.
    """
    align_map = {
        "left": WD_ALIGN_PARAGRAPH.LEFT,
        "center": WD_ALIGN_PARAGRAPH.CENTER,
        "right": WD_ALIGN_PARAGRAPH.RIGHT,
    }
    if align in align_map:
        paragraph.alignment = align_map[align]
