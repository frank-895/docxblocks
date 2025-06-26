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
            # Use regex to properly handle consecutive newlines
            import re
            
            # Split by newlines but preserve information about multiple consecutive newlines
            # This regex keeps the newlines in the split results
            parts = re.split(r'(\n+)', text)
            
            for part in parts:
                if not part:  # Skip empty strings
                    continue
                    
                if part.startswith('\n'):
                    # This is a sequence of newlines - create blank paragraphs
                    # Number of blank paragraphs = number of newlines - 1
                    num_blanks = len(part) - 1
                    for _ in range(num_blanks):
                        para = self.doc.add_paragraph(
                            style=block.style.style if block.style and block.style.style else "Normal"
                        )
                        self.parent.insert(self.index, para._element)
                        self.index += 1
                    
                    # The last newline creates a new paragraph for the next content
                    self.current_paragraph = None
                else:
                    # This is actual text content
                    current_style_name = block.style.style if block.style and block.style.style else "Normal"
                    current_align = block.style.align if block.style else None
                    
                    # Check if we need a new paragraph due to alignment change
                    if (self.current_paragraph is None or 
                        getattr(self.current_paragraph, '_last_align', None) != current_align):
                        
                        self.current_paragraph = self.doc.add_paragraph(style=current_style_name)
                        # Apply paragraph alignment when creating new paragraph
                        if current_align:
                            set_paragraph_alignment(self.current_paragraph, current_align)
                        
                        # Store alignment and style for comparison with subsequent blocks
                        self.current_paragraph._last_align = current_align
                        self.current_paragraph._last_style = current_style_name
                        
                        self.parent.insert(self.index, self.current_paragraph._element)
                        self.index += 1
                    
                    run = self.current_paragraph.add_run(part)
                    apply_style_to_run(run, block.style)
            
            # After processing text with newlines, keep current_paragraph set
            # so that subsequent inline text can be added to the last paragraph created
        else:
            # Handle inline text
            # Handle inline text - original behavior but check for alignment changes
            if self.current_paragraph is None:
                # Start a new paragraph
                current_style_name = block.style.style if block.style and block.style.style else "Normal"
                current_align = block.style.align if block.style else None
                
                self.current_paragraph = self.doc.add_paragraph(style=current_style_name)
                # Apply paragraph alignment when creating new paragraph
                if current_align:
                    set_paragraph_alignment(self.current_paragraph, current_align)
                
                self.parent.insert(self.index, self.current_paragraph._element)
                self.index += 1
            else:
                # Check if alignment has changed and we need a new paragraph
                current_align = block.style.align if block.style else None
                last_align = getattr(self.current_paragraph, '_last_align', None)
                
                if last_align != current_align:
                    # Need new paragraph due to alignment change
                    current_style_name = block.style.style if block.style and block.style.style else "Normal"
                    self.current_paragraph = self.doc.add_paragraph(style=current_style_name)
                    if current_align:
                        set_paragraph_alignment(self.current_paragraph, current_align)
                    self.parent.insert(self.index, self.current_paragraph._element)
                    self.index += 1
            
            # Store the alignment for next comparison (even for first time)
            self.current_paragraph._last_align = block.style.align if block.style else None
            
            # Add text to current paragraph
            run = self.current_paragraph.add_run(text)
            apply_style_to_run(run, block.style)

 