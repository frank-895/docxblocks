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
    as a separate paragraph with proper Word bullet formatting. Empty items are replaced
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
        and renders each item as a properly formatted bulleted paragraph with appropriate styling.
        
        Args:
            block: A validated BulletBlock object containing list items and styling
        """
        # Handle empty items list
        items = block.items if block.items else [DEFAULT_EMPTY_VALUE_TEXT]
        
        for item in items:
            # Create paragraph with bullet formatting
            para = self.doc.add_paragraph()
            
            # Handle empty item text
            item_text = item.strip() if item else DEFAULT_EMPTY_VALUE_TEXT
            
            # Add the text as a run
            run = para.add_run(item_text)
            
            # Apply block style, but override with placeholder style if item is empty
            if not item or not item.strip():
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, block.style)
            
            # Set paragraph alignment
            set_paragraph_alignment(para, block.style.align if block.style else None)
            
            # Apply bullet formatting to the paragraph
            self._apply_bullet_formatting(para)
            
            # Insert into parent at the specified index
            self.parent.insert(self.index, para._element)
            self.index += 1
    
    def _apply_bullet_formatting(self, paragraph):
        """
        Apply proper bullet formatting to a paragraph.
        
        This method uses python-docx's built-in bullet functionality to create
        proper Word-compatible bullet points that will display correctly in any
        Word document without requiring custom styles.
        
        Args:
            paragraph: The python-docx Paragraph object to format
        """
        try:
            # Use python-docx's built-in bullet functionality
            paragraph.style = self.doc.styles['List Bullet']
        except KeyError:
            # Fallback: try to create a bullet style programmatically
            self._create_bullet_style(paragraph)
    
    def _create_bullet_style(self, paragraph):
        """
        Create a bullet style programmatically if the default doesn't exist.
        
        This is a fallback method that creates a basic bullet style using
        python-docx's style creation capabilities.
        
        Args:
            paragraph: The python-docx Paragraph object to format
        """
        try:
            # Try to create a bullet style
            bullet_style = self.doc.styles.add_style('DocxBlocks_Bullet', 1)  # 1 = WD_STYLE_TYPE.PARAGRAPH
            
            # Set up basic bullet formatting
            paragraph_format = bullet_style.paragraph_format
            paragraph_format.left_indent = 720000  # 0.5 inches in EMUs
            paragraph_format.first_line_indent = -360000  # -0.25 inches in EMUs
            
            # Apply the style
            paragraph.style = bullet_style
            
        except Exception:
            # Final fallback: just add a bullet character manually
            # This ensures the library always works, even if bullet styling fails
            current_text = paragraph.text
            if not current_text.startswith('•'):
                paragraph.text = f"• {current_text}" 