"""
Text Processing Utilities

This module provides shared text processing utilities for handling newline patterns
consistently across different block types (text, table cells, etc.).
"""

from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run, set_paragraph_alignment
from docxblocks.constants import DEFAULT_EMPTY_VALUE_STYLE, DEFAULT_EMPTY_VALUE_TEXT


def process_text_with_newlines(container, text, style=None, is_empty=False):
    """
    For each segment in text.split('\n'), create a new paragraph (even if the segment is empty).
    - Single \n creates a new paragraph (no blank)
    - Double \n\n creates a blank paragraph
    - Inline grouping is preserved unless a \n is present
    """
    paragraphs = []
    if not text:
        para = container.add_paragraph(
            style=style.style if style and style.style else "Normal"
        )
        # Add placeholder text for empty content
        run = para.add_run(DEFAULT_EMPTY_VALUE_TEXT)
        if is_empty:
            apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
        else:
            apply_style_to_run(run, style)
        
        # Apply paragraph alignment
        if style and style.align:
            set_paragraph_alignment(para, style.align)
        paragraphs.append(para._element)
        return paragraphs

    lines = text.split('\n')
    for line in lines:
        para = container.add_paragraph(
            style=style.style if style and style.style else "Normal"
        )
        paragraphs.append(para._element)
        if line:
            run = para.add_run(line)
            if is_empty:
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, style)
        
        # Apply paragraph alignment for all paragraphs (even empty ones)
        if style and style.align:
            set_paragraph_alignment(para, style.align)
    return paragraphs


def add_text_to_cell(cell, text, style=None, is_empty=False):
    """
    Add text content to a table cell with proper newline handling.
    This uses the unified process_text_with_newlines logic for consistency.
    """
    # Clear all existing paragraphs in the cell
    for paragraph in cell.paragraphs:
        p = paragraph._element
        p.getparent().remove(p)
    process_text_with_newlines(cell, text, style=style, is_empty=is_empty) 