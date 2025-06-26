"""
Text Processing Utilities

This module provides shared text processing utilities for handling newline patterns
consistently across different block types (text, table cells, etc.).
"""

from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run
from docxblocks.constants import DEFAULT_EMPTY_VALUE_STYLE


def process_text_with_newlines(doc, text, style=None, is_empty=False):
    """
    Process text content and handle newlines by creating new paragraphs.
    
    This function splits text by \n and creates separate paragraphs for each part.
    Every \n creates a new paragraph, including empty ones.
    
    Args:
        doc: The python-docx Document object
        text: The text content to process
        style: TextStyle object for styling (optional)
        is_empty: Whether the original text was empty (for placeholder styling)
    
    Returns:
        list: List of paragraph elements that were created
    """
    paragraphs = []
    
    # Split by \n to handle all newlines as paragraph breaks
    parts = text.split("\n")
    
    for i, part in enumerate(parts):
        # Create new paragraph for this part (including empty ones)
        para = doc.add_paragraph(
            style=style.style if style and style.style else "Normal"
        )
        paragraphs.append(para._element)
        
        # Add the part as a run to the current paragraph
        if part:  # Only add non-empty parts
            run = para.add_run(part)
            
            # Apply block style, but override with placeholder style if text is empty
            if is_empty:
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, style)
    
    return paragraphs


def add_text_to_cell(cell, text, style=None, is_empty=False):
    """
    Add text content to a table cell with proper newline handling.
    
    This function processes text content and adds it to a table cell,
    handling \n patterns by creating multiple paragraphs within the cell.
    Behaves exactly like process_text_with_newlines for consistency.
    
    Args:
        cell: The table cell element
        text: The text content to add
        style: TextStyle object for styling (optional)
        is_empty: Whether the original text was empty (for placeholder styling)
    """
    # Clear all existing paragraphs in the cell
    for paragraph in cell.paragraphs:
        p = paragraph._element
        p.getparent().remove(p)
    
    # Split by \n to handle all newlines as paragraph breaks
    parts = text.split("\n")
    
    for i, part in enumerate(parts):
        # Create new paragraph for this part (including empty ones)
        para = cell.add_paragraph()
        
        # Add the part as a run to the current paragraph
        if part:  # Only add non-empty parts
            run = para.add_run(part)
            
            # Apply block style, but override with placeholder style if text is empty
            if is_empty:
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, style)