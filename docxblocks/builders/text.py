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
    
    This builder handles plain text content with optional styling. By default,
    text blocks are inline (added to the current paragraph). Only when new_paragraph
    is True will a new paragraph be created.
    
    Attributes:
        doc: The python-docx Document object
        parent: The parent XML element where content will be inserted
        index: The insertion index within the parent element
        current_paragraph: The current paragraph for inline text (if any)
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
        
        This method processes the text block, handles empty values with placeholders,
        and creates new paragraphs for all newlines. It also handles the spacing
        parameter to add extra blank lines after the text.
        
        Args:
            block: A validated TextBlock object containing text content and styling
        """
        # Handle empty text with placeholder
        text = block.text if block.text else DEFAULT_EMPTY_VALUE_TEXT
        
        # Always process text with newlines since all newlines create new paragraphs
        paragraphs = process_text_with_newlines(
            self.doc, text, block.style, 
            is_empty=(not block.text or not block.text.strip())
        )
        
        # Insert the processed paragraphs
        for i, para_element in enumerate(paragraphs):
            self.parent.insert(self.index + i, para_element)
        self.index += len(paragraphs)
        self.current_paragraph = None  # Always reset after block

        # Handle spacing - add extra blank lines after the text
        if block.spacing and block.spacing > 1:
            for _ in range(block.spacing - 1):
                blank_para = self.doc.add_paragraph(
                    style=block.style.style if block.style and block.style.style else "Normal"
                )
                self.parent.insert(self.index, blank_para._element)
                self.index += 1 