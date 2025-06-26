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
    Process text content and handle \n\n patterns by creating paragraphs with blank lines.
    
    This function splits text by \n\n and creates separate paragraphs for each part,
    with blank paragraphs inserted between them. Single \n characters remain as
    literal newlines within paragraphs.
    
    Args:
        doc: The python-docx Document object
        text: The text content to process
        style: TextStyle object for styling (optional)
        is_empty: Whether the original text was empty (for placeholder styling)
    
    Returns:
        list: List of paragraph elements that were created
    """
    paragraphs = []
    
    # Check for \n\n pattern and handle it specially
    if "\n\n" in text:
        # Split by \n\n to separate content that should be in different paragraphs
        parts = text.split("\n\n")
        for i, part in enumerate(parts):
            if i > 0:
                # Add a blank line before the new paragraph
                blank_para = doc.add_paragraph(
                    style=style.style if style and style.style else "Normal"
                )
                paragraphs.append(blank_para._element)
                
                # Create new paragraph for this part
                para = doc.add_paragraph(
                    style=style.style if style and style.style else "Normal"
                )
                paragraphs.append(para._element)
            else:
                # Create paragraph for the first part
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
    else:
        # No \n\n found, create a single paragraph
        para = doc.add_paragraph(
            style=style.style if style and style.style else "Normal"
        )
        run = para.add_run(text)
        
        # Apply block style, but override with placeholder style if text is empty
        if is_empty:
            apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
        else:
            apply_style_to_run(run, style)
        
        paragraphs.append(para._element)
    
    return paragraphs


def add_text_to_cell(cell, text, style=None, is_empty=False):
    """
    Add text content to a table cell with proper newline handling.
    
    This function processes text content and adds it to a table cell,
    handling \n\n patterns by creating multiple paragraphs within the cell.
    
    Args:
        cell: The table cell element
        text: The text content to add
        style: TextStyle object for styling (optional)
        is_empty: Whether the original text was empty (for placeholder styling)
    """
    # Clear existing content
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.text = ""
    
    # Check for \n\n pattern and handle it specially
    if "\n\n" in text:
        # Split by \n\n to separate content that should be in different paragraphs
        parts = text.split("\n\n")
        for i, part in enumerate(parts):
            if i > 0:
                # Add a blank paragraph before the new content
                blank_para = cell.add_paragraph()
                blank_para.text = ""
                
                # Create new paragraph for this part
                para = cell.add_paragraph()
            else:
                # Use the first paragraph or create one if needed
                if cell.paragraphs:
                    para = cell.paragraphs[0]
                else:
                    para = cell.add_paragraph()
            
            # Add the part as a run to the current paragraph
            if part:  # Only add non-empty parts
                run = para.add_run(part)
                
                # Apply block style, but override with placeholder style if text is empty
                if is_empty:
                    apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
                else:
                    apply_style_to_run(run, style)
    else:
        # No \n\n found, add text to the first paragraph
        if cell.paragraphs:
            para = cell.paragraphs[0]
        else:
            para = cell.add_paragraph()
        
        run = para.add_run(text)
        
        # Apply block style, but override with placeholder style if text is empty
        if is_empty:
            apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
        else:
            apply_style_to_run(run, style) 