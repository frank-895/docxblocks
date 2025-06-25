"""
Rich Text Builder Module

This module provides the RichTextBuilder class for rendering various block types in Word documents.
It acts as a coordinator that delegates rendering to specialized builders for each block type.
"""

from docxblocks.schema.blocks import Block, TextBlock, HeadingBlock, BulletBlock, TableBlock, ImageBlock, PageBreakBlock
from docxblocks.builders.text import TextBuilder
from docxblocks.builders.heading import HeadingBuilder
from docxblocks.builders.bullet import BulletBuilder
from docxblocks.builders.table import TableBuilder
from docxblocks.builders.image import ImageBuilder
from docxblocks.builders.page_break import PageBreakBuilder


class RichTextBuilder:
    """
    Coordinator class for rendering various block types in Word documents.
    
    This builder acts as a central coordinator that validates block data and
    delegates rendering to specialized builders for each block type. It supports
    text, heading, bullet, table, image, and page break blocks.
    
    The builder uses Pydantic validation to ensure proper block structure and
    handles validation errors gracefully by skipping invalid blocks.
    
    Attributes:
        doc: The python-docx Document object
        parent: The parent XML element where content will be inserted
        index: The insertion index within the parent element
        text_builder: Shared TextBuilder instance for handling inline text
    """
    
    def __init__(self, doc, parent, index):
        """
        Initialize the RichTextBuilder.
        
        Args:
            doc: The python-docx Document object
            parent: The parent XML element where content will be inserted
            index: The insertion index within the parent element
        """
        self.doc = doc
        self.parent = parent
        self.index = index
        self.text_builder = None

    def render(self, blocks: list):
        """
        Render a list of block dictionaries into the document.
        
        This method validates each block using Pydantic, determines the block type,
        and delegates rendering to the appropriate specialized builder. Invalid
        blocks are skipped gracefully.
        
        Args:
            blocks: List of block dictionaries to render. Each block should contain
                   a 'type' field and appropriate data for that block type.
        """
        validated_blocks = []
        for b in blocks:
            # Try to validate as each block type
            for block_class in [TextBlock, HeadingBlock, BulletBlock, TableBlock, ImageBlock, PageBreakBlock]:
                try:
                    validated_block = block_class.model_validate(b)
                    validated_blocks.append(validated_block)
                    break
                except:
                    continue
            else:
                # If no block type matches, skip this block
                continue
                
        for block in validated_blocks:
            if isinstance(block, TextBlock):
                self._render_text(block)
            elif isinstance(block, HeadingBlock):
                self._render_heading(block)
            elif isinstance(block, BulletBlock):
                self._render_bullets(block)
            elif isinstance(block, TableBlock):
                self._render_table(block)
            elif isinstance(block, ImageBlock):
                self._render_image(block)
            elif isinstance(block, PageBreakBlock):
                self._render_page_break(block)

    def _render_text(self, block: TextBlock):
        """
        Render a text block using the TextBuilder.
        
        Args:
            block: A validated TextBlock object
        """
        # Create text builder if it doesn't exist or if this is a new paragraph block
        if self.text_builder is None or block.new_paragraph:
            self.text_builder = TextBuilder(self.doc, self.parent, self.index)
        
        self.text_builder.build(block)
        # Update index based on how many paragraphs were added
        self.index = self.text_builder.index

    def _render_heading(self, block: HeadingBlock):
        """
        Render a heading block using the HeadingBuilder.
        
        Args:
            block: A validated HeadingBlock object
        """
        # Reset text builder when we encounter a non-text block
        self.text_builder = None
        
        builder = HeadingBuilder(self.doc, self.parent, self.index)
        builder.build(block)
        # Update index based on how many paragraphs were added
        self.index = builder.index

    def _render_bullets(self, block: BulletBlock):
        """
        Render a bullet block using the BulletBuilder.
        
        Args:
            block: A validated BulletBlock object
        """
        # Reset text builder when we encounter a non-text block
        self.text_builder = None
        
        builder = BulletBuilder(self.doc, self.parent, self.index)
        builder.build(block)
        # Update index based on how many paragraphs were added
        self.index = builder.index

    def _render_table(self, block: TableBlock):
        """
        Render a table block using the TableBuilder.
        
        Args:
            block: A validated TableBlock object
        """
        # Reset text builder when we encounter a non-text block
        self.text_builder = None
        
        TableBuilder.build(
            self.doc,
            placeholder=None,
            content=block.content,
            parent=self.parent,
            index=self.index,
            **(block.style.model_dump() if block.style else {})
        )
        self.index += 1

    def _render_image(self, block: ImageBlock):
        """
        Render an image block using the ImageBuilder.
        
        Args:
            block: A validated ImageBlock object
        """
        # Reset text builder when we encounter a non-text block
        self.text_builder = None
        
        ImageBuilder.build(
            self.doc,
            placeholder=None,
            image_path=block.path,
            parent=self.parent,
            index=self.index,
            **(block.style.model_dump() if block.style else {})
        )
        self.index += 1

    def _render_page_break(self, block: PageBreakBlock):
        """
        Render a page break block using the PageBreakBuilder.
        
        Args:
            block: A validated PageBreakBlock object
        """
        # Reset text builder when we encounter a non-text block
        self.text_builder = None
        
        builder = PageBreakBuilder(self.doc, self.parent, self.index)
        builder.build(block)
        # Update index based on how many paragraphs were added
        self.index = builder.index