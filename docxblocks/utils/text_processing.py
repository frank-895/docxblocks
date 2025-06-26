"""
Text Processing Utilities

This module provides shared text processing utilities for handling newline patterns
consistently across different block types (text, table cells, etc.).
"""

from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run
from docxblocks.constants import DEFAULT_EMPTY_VALUE_STYLE, DEFAULT_EMPTY_VALUE_TEXT


def process_text_with_newlines(container, text, style=None, is_empty=False):
    """
    Process text content and handle newlines by creating new paragraphs in a container (doc or cell).
    
    Args:
        container: The python-docx Document or table cell object
        text: The text content to process
        style: TextStyle object for styling (optional)
        is_empty: Whether the original text was empty (for placeholder styling)
    
    Returns:
        list: List of paragraph elements that were created
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
        paragraphs.append(para._element)
        return paragraphs

    lines = text.split('\n')
    i = 0
    while i < len(lines):
        if lines[i]:
            # If there are preceding empty lines, add blank paragraphs for each
            j = i - 1
            blank_count = 0
            while j >= 0 and lines[j] == '':
                blank_count += 1
                j -= 1
            for _ in range(blank_count):
                blank_para = container.add_paragraph(
                    style=style.style if style and style.style else "Normal"
                )
                paragraphs.append(blank_para._element)
            # Add the non-empty paragraph
            para = container.add_paragraph(
                style=style.style if style and style.style else "Normal"
            )
            paragraphs.append(para._element)
            run = para.add_run(lines[i])
            if is_empty:
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, style)
        i += 1
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