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
        and either adds text to the current paragraph (inline) or creates a new paragraph.
        
        Args:
            block: A validated TextBlock object containing text content and styling
        """
        # Handle empty text with placeholder
        text = block.text if block.text else DEFAULT_EMPTY_VALUE_TEXT
        
        if not block.new_paragraph:
            # Add to current paragraph or create new one if none exists
            if self.current_paragraph is None:
                self.current_paragraph = self.doc.add_paragraph(
                    style=block.style.style if block.style and block.style.style else "Normal"
                )
                self.parent.insert(self.index, self.current_paragraph._element)
                self.index += 1
            
            # Add text as a run to the current paragraph
            run = self.current_paragraph.add_run(text)
            
            # Apply block style, but override with placeholder style if text is empty
            if not block.text or not block.text.strip():
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, block.style)
        else:
            # If text contains newlines, create a paragraph for each line
            lines = text.split("\n")
            for i, line in enumerate(lines):
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
                self.current_paragraph = para 