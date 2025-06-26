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
        and either adds text to the current paragraph (inline) or creates new paragraphs.
        It handles \n by creating new paragraphs, and the spacing parameter to add extra blank lines.
        
        Args:
            block: A validated TextBlock object containing text content and styling
        """
        # Handle empty text with placeholder
        text = block.text if block.text else DEFAULT_EMPTY_VALUE_TEXT
        
        if not block.new_paragraph and "\n" not in text:
            # Inline text - add to current paragraph or create new one if none exists
            created_new_paragraph = False
            if self.current_paragraph is None:
                self.current_paragraph = self.doc.add_paragraph(
                    style=block.style.style if block.style and block.style.style else "Normal"
                )
                self.parent.insert(self.index, self.current_paragraph._element)
                created_new_paragraph = True
            
            # Add text as a run to the current paragraph
            run = self.current_paragraph.add_run(text)
            
            # Apply block style, but override with placeholder style if text is empty
            if not block.text or not block.text.strip():
                apply_style_to_run(run, TextStyle(**DEFAULT_EMPTY_VALUE_STYLE))
            else:
                apply_style_to_run(run, block.style)
            
            if created_new_paragraph:
                self.index += 1
        else:
            # New paragraph or text with newlines - always process with newlines
            self.current_paragraph = None  # Reset for next inline group
            
            # Process text with newlines since \n or new_paragraph is present
            paragraphs = process_text_with_newlines(
                self.doc, text, block.style, 
                is_empty=(not block.text or not block.text.strip())
            )
            
            # Insert the processed paragraphs
            for i, para_element in enumerate(paragraphs):
                self.parent.insert(self.index + i, para_element)
            self.index += len(paragraphs)
            
            # After new_paragraph or \n, reset current_paragraph so next inline block starts fresh
            self.current_paragraph = None

        # Handle spacing - add extra blank lines after the text
        if block.spacing and block.spacing > 1:
            for _ in range(block.spacing - 1):
                blank_para = self.doc.add_paragraph(
                    style=block.style.style if block.style and block.style.style else "Normal"
                )
                self.parent.insert(self.index, blank_para._element)
                self.index += 1 