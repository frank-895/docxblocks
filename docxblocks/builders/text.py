"""
Text Builder Module

This module provides the TextBuilder class for rendering text blocks in Word documents.
It handles plain text content with optional styling and supports multi-line text.
"""

from docxblocks.schema.blocks import TextBlock
from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run, set_paragraph_alignment
from docxblocks.utils.text_processing import process_text_with_newlines
from docxblocks.constants import DEFAULT_EMPTY_VALUE_TEXT, DEFAULT_EMPTY_VALUE_STYLE


class TextBuilder:
    """
    Builder class for rendering text blocks in Word documents.
    
    Simple rules:
    - Every \n starts a new paragraph
    - Consecutive blocks without \n are grouped inline
    - Empty text gets placeholder text
    """
    
    def __init__(self, doc, parent, index):
        """
        Initialize the TextBuilder.
        
        Args:
            doc: The python-docx Document object
            parent: The parent XML element where content will be inserted
            index: The insertion index within the parent element
        """
        self.doc = doc
        self.parent = parent
        self.index = index
        self.current_paragraph = None

    def build(self, block: TextBlock):
        """
        Build and render a text block in the document.
        
        Simple logic:
        - If text contains \n: split into paragraphs
        - If text is empty: add placeholder
        - Otherwise: add to current paragraph or start new one
        """
        text = block.text if block.text is not None else DEFAULT_EMPTY_VALUE_TEXT
        is_empty = not text.strip()

        # Handle empty text
        if not text or is_empty:
            para = self.doc.add_paragraph(
                style=block.style.style if block.style and block.style.style else "Normal"
            )
            run = para.add_run(DEFAULT_EMPTY_VALUE_TEXT)
            apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            self.parent.insert(self.index, para._element)
            self.index += 1
            self.current_paragraph = None
            return

        # Handle text with newlines
        if "\n" in text:
            # Split by newlines and create a paragraph for each part
            lines = text.split("\n")
            for line in lines:
                para = self.doc.add_paragraph(
                    style=block.style.style if block.style and block.style.style else "Normal"
                )
                self.parent.insert(self.index, para._element)
                self.index += 1
                
                if line:  # Only add non-empty content
                    run = para.add_run(line)
                    apply_style_to_run(run, block.style)
            
            # After newlines, set current_paragraph to the last paragraph created
            # so subsequent inline blocks are grouped
            if lines and any(line.strip() for line in lines):
                self.current_paragraph = para
            else:
                self.current_paragraph = None
        else:
            # Handle inline text
            if self.current_paragraph is None:
                # Start a new paragraph
                self.current_paragraph = self.doc.add_paragraph(
                    style=block.style.style if block.style and block.style.style else "Normal"
                )
                self.parent.insert(self.index, self.current_paragraph._element)
                self.index += 1
            
            # Add text to current paragraph
            run = self.current_paragraph.add_run(text)
            apply_style_to_run(run, block.style)

        # Handle spacing parameter
        if block.spacing and block.spacing > 1:
            for _ in range(block.spacing - 1):
                blank_para = self.doc.add_paragraph(
                    style=block.style.style if block.style and block.style.style else "Normal"
                )
                self.parent.insert(self.index, blank_para._element)
                self.index += 1
            # Spacing ends the current paragraph
            self.current_paragraph = None 