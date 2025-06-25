"""
Page Break Builder Module

This module provides the PageBreakBuilder class for rendering page break blocks in Word documents.
It handles page break insertion with proper Word document structure.
"""

from docx.enum.text import WD_BREAK
from docxblocks.schema.blocks import PageBreakBlock


class PageBreakBuilder:
    """
    Builder class for rendering page break blocks in Word documents.
    
    This builder handles page break insertion by creating a new paragraph
    with a page break run. Page breaks are inserted as separate paragraphs
    to maintain proper document structure.
    
    Attributes:
        doc: The python-docx Document object
        parent: The parent XML element where content will be inserted
        index: The insertion index within the parent element
    """
    
    def __init__(self, doc, parent, index):
        """
        Initialize the PageBreakBuilder.
        
        Args:
            doc: The python-docx Document object
            parent: The parent XML element where content will be inserted
            index: The insertion index within the parent element
        """
        self.doc = doc
        self.parent = parent
        self.index = index

    def build(self, block: PageBreakBlock):
        """
        Build and render a page break block in the document.
        
        This method creates a new paragraph with a page break run and
        inserts it into the document at the specified location.
        
        Args:
            block: A validated PageBreakBlock object
        """
        # Create a new paragraph for the page break
        para = self.doc.add_paragraph()
        run = para.add_run()
        
        # Add the page break
        run.add_break(WD_BREAK.PAGE)
        
        # Insert the paragraph into the document
        self.parent.insert(self.index, para._element)
        self.index += 1 