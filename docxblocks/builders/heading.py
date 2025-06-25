"""
Heading Builder Module

This module provides the HeadingBuilder class for rendering heading blocks in Word documents.
It handles heading text with different levels (1-6) and optional styling.
"""

from docxblocks.schema.blocks import HeadingBlock
from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run, set_paragraph_alignment
from docxblocks.constants import DEFAULT_EMPTY_VALUE_TEXT, DEFAULT_EMPTY_VALUE_STYLE


class HeadingBuilder:
    """
    Builder class for rendering heading blocks in Word documents.
    
    This builder handles heading content with different levels (1-6) and optional
    styling. It automatically applies appropriate Word heading styles based on
    the heading level. Empty text is replaced with a consistent placeholder.
    
    Attributes:
        doc: The python-docx Document object
        parent: The parent XML element where content will be inserted
        index: The insertion index within the parent element
    """
    
    def __init__(self, doc, parent, index):
        """
        Initialize the HeadingBuilder.
        
        Args:
            doc: The python-docx Document object
            parent: The parent XML element where content will be inserted
            index: The insertion index within the parent element
        """
        self.doc = doc
        self.parent = parent
        self.index = index

    def build(self, block: HeadingBlock):
        """
        Build and render a heading block in the document.
        
        This method processes the heading block, handles empty values with placeholders,
        applies appropriate Word heading styles, and renders the heading text.
        
        Args:
            block: A validated HeadingBlock object containing heading text, level, and styling
        """
        # Handle empty text with placeholder
        text = block.text.strip() if block.text else DEFAULT_EMPTY_VALUE_TEXT
        
        style_name = (
            block.style.style if block.style and block.style.style else f"Heading {block.level}"
        )
        para = self.doc.add_paragraph(style=style_name)
        run = para.add_run(text)
        
        # Apply block style, but override with placeholder style if text is empty
        if not block.text or not block.text.strip():
            apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
        else:
            apply_style_to_run(run, block.style)
            
        set_paragraph_alignment(para, block.style.align if block.style else None)
        self.parent.insert(self.index, para._element)
        self.index += 1 