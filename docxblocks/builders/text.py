"""
Text Builder Module

This module provides the TextBuilder class for rendering text blocks in Word documents.
It handles plain text content with optional styling and supports multi-line text.
"""

from docxblocks.schema.blocks import TextBlock
from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run, set_paragraph_alignment
from docxblocks.constants import DEFAULT_EMPTY_VALUE_TEXT, DEFAULT_EMPTY_VALUE_STYLE


class TextBuilder:
    """
    Builder class for rendering text blocks in Word documents.
    
    This builder handles plain text content with optional styling. It supports
    multi-line text by splitting on newlines and creating separate paragraphs
    for each line. Empty text is replaced with a consistent placeholder.
    
    Attributes:
        doc: The python-docx Document object
        parent: The parent XML element where content will be inserted
        index: The insertion index within the parent element
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

    def build(self, block: TextBlock):
        """
        Build and render a text block in the document.
        
        This method processes the text block, handles empty values with placeholders,
        splits multi-line text, and applies styling to each paragraph.
        
        Args:
            block: A validated TextBlock object containing text content and styling
        """
        # Handle empty text with placeholder
        text = block.text.strip() if block.text else DEFAULT_EMPTY_VALUE_TEXT
        lines = text.split("\n")
        
        for line in lines:
            para = self.doc.add_paragraph(
                style=block.style.style if block.style and block.style.style else "Normal"
            )
            run = para.add_run(line)
            
            # Apply block style, but override with placeholder style if text is empty
            if not block.text or not block.text.strip():
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, block.style)
                
            set_paragraph_alignment(para, block.style.align if block.style else None)
            self.parent.insert(self.index, para._element)
            self.index += 1 