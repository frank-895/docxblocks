"""
Bullet Builder Module

This module provides the BulletBuilder class for rendering bullet list blocks in Word documents.
It handles lists of items with optional styling and bullet point formatting.
"""

from docxblocks.schema.blocks import BulletBlock
from docxblocks.schema.shared import TextStyle
from docxblocks.utils.styles import apply_style_to_run, set_paragraph_alignment
from docxblocks.constants import DEFAULT_EMPTY_VALUE_TEXT, DEFAULT_EMPTY_VALUE_STYLE


class BulletBuilder:
    """
    Builder class for rendering bullet list blocks in Word documents.
    
    This builder handles lists of items with optional styling. Each item is rendered
    as a separate paragraph with a bullet point (•) prefix. Empty items are replaced
    with consistent placeholders.
    
    Attributes:
        doc: The python-docx Document object
        parent: The parent XML element where content will be inserted
        index: The insertion index within the parent element
    """
    
    def __init__(self, doc, parent, index):
        """
        Initialize the BulletBuilder.
        
        Args:
            doc: The python-docx Document object
            parent: The parent XML element where content will be inserted
            index: The insertion index within the parent element
        """
        self.doc = doc
        self.parent = parent
        self.index = index

    def build(self, block: BulletBlock):
        """
        Build and render a bullet list block in the document.
        
        This method processes the bullet block, handles empty values with placeholders,
        and renders each item as a bulleted paragraph with appropriate styling.
        
        Args:
            block: A validated BulletBlock object containing list items and styling
        """
        # Handle empty items list
        items = block.items if block.items else [DEFAULT_EMPTY_VALUE_TEXT]
        
        for item in items:
            para = self.doc.add_paragraph()
            
            # Handle empty item text
            item_text = item.strip() if item else DEFAULT_EMPTY_VALUE_TEXT
            run = para.add_run(f"• {item_text}")
            
            # Apply block style, but override with placeholder style if item is empty
            if not item or not item.strip():
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, block.style)
                
            set_paragraph_alignment(para, block.style.align if block.style else None)
            self.parent.insert(self.index, para._element)
            self.index += 1 