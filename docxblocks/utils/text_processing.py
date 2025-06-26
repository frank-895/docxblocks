"""
Text Processing Utilities

This module provides shared text processing utilities for handling newline patterns
consistently across different block types (text, table cells, etc.).
"""

from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run
from docxblocks.constants import DEFAULT_EMPTY_VALUE_STYLE, DEFAULT_EMPTY_VALUE_TEXT


def process_text_with_newlines(doc, text, style=None, is_empty=False):
    """
    Process text content and handle newlines by creating new paragraphs.
    
    This function handles newline patterns:
    - \n creates a new paragraph (no extra spacing)
    - \n\n creates a new paragraph with one blank paragraph before it
    - \n\n\n creates a new paragraph with two blank paragraphs before it
    - And so on for more consecutive newlines
    
    Args:
        doc: The python-docx Document object
        text: The text content to process
        style: TextStyle object for styling (optional)
        is_empty: Whether the original text was empty (for placeholder styling)
    
    Returns:
        list: List of paragraph elements that were created
    """
    paragraphs = []
    if not text:
        para = doc.add_paragraph(
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

    # Split the text by newlines to process each part
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if i == 0:
            # First line - just create a paragraph with the content
            para = doc.add_paragraph(
                style=style.style if style and style.style else "Normal"
            )
            paragraphs.append(para._element)
            
            if line:  # Only add non-empty content
                run = para.add_run(line)
                if is_empty:
                    apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
                else:
                    apply_style_to_run(run, style)
        else:
            # For subsequent lines, check if the previous line was empty
            # If the previous line was empty, we need to add blank paragraphs
            if i > 0 and lines[i-1] == '':
                # Count consecutive empty lines to determine how many blank paragraphs to add
                consecutive_empty = 0
                j = i - 1
                while j >= 0 and lines[j] == '':
                    consecutive_empty += 1
                    j -= 1
                
                # Add blank paragraphs (one less than consecutive empty lines)
                for _ in range(consecutive_empty - 1):
                    blank_para = doc.add_paragraph(
                        style=style.style if style and style.style else "Normal"
                    )
                    paragraphs.append(blank_para._element)
            
            # Create paragraph for current line
            para = doc.add_paragraph(
                style=style.style if style and style.style else "Normal"
            )
            paragraphs.append(para._element)
            
            if line:  # Only add non-empty content
                run = para.add_run(line)
                if is_empty:
                    apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
                else:
                    apply_style_to_run(run, style)
    
    return paragraphs


def add_text_to_cell(cell, text, style=None, is_empty=False):
    """
    Add text content to a table cell with proper newline handling.
    
    This function processes text content and adds it to a table cell,
    handling newline patterns consistently with process_text_with_newlines:
    - \n creates a new paragraph (no extra spacing)
    - \n\n creates a new paragraph with one blank paragraph before it
    - \n\n\n creates a new paragraph with two blank paragraphs before it
    
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
    
    if not text:
        # Handle empty text
        cell.add_paragraph()
        return
    
    # Split the text by newlines to process each part
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if i == 0:
            # First line - just create a paragraph with the content
            para = cell.add_paragraph()
            
            if line:  # Only add non-empty content
                run = para.add_run(line)
                if is_empty:
                    apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
                else:
                    apply_style_to_run(run, style)
        else:
            # For subsequent lines, check if the previous line was empty
            # If the previous line was empty, we need to add blank paragraphs
            if i > 0 and lines[i-1] == '':
                # Count consecutive empty lines to determine how many blank paragraphs to add
                consecutive_empty = 0
                j = i - 1
                while j >= 0 and lines[j] == '':
                    consecutive_empty += 1
                    j -= 1
                
                # Add blank paragraphs (one less than consecutive empty lines)
                for _ in range(consecutive_empty - 1):
                    cell.add_paragraph()
            
            # Create paragraph for current line
            para = cell.add_paragraph()
            
            if line:  # Only add non-empty content
                run = para.add_run(line)
                if is_empty:
                    apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
                else:
                    apply_style_to_run(run, style)