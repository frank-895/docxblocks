"""
Rich Text Builder Module

This module provides the RichTextBuilder class for rendering various block types in Word documents.
It acts as a coordinator that delegates rendering to specialized builders for each block type.
"""

from docxblocks.schema.blocks import Block, TextBlock, HeadingBlock, BulletBlock, TableBlock, ImageBlock, PageBreakBlock, HeaderBlock, FooterBlock
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
            # Get the block type from the dictionary
            block_type = b.get('type')
            if not block_type:
                continue
                
            # Map block types to their corresponding classes
            block_class_map = {
                'text': TextBlock,
                'heading': HeadingBlock,
                'bullets': BulletBlock,
                'table': TableBlock,
                'image': ImageBlock,
                'page_break': PageBreakBlock,
                'header': HeaderBlock,
                'footer': FooterBlock
            }
            
            # Get the appropriate block class
            block_class = block_class_map.get(block_type)
            if not block_class:
                continue
                
            # Validate the block
            try:
                validated_block = block_class.model_validate(b)
                validated_blocks.append(validated_block)
            except:
                # If validation fails, skip this block
                continue
                
        for block in validated_blocks:
            if isinstance(block, TextBlock):
                # Only consecutive text blocks are grouped inline.
                self._render_text(block)
            else:
                # Any non-text block resets the inline group.
                self.text_builder = None
                if isinstance(block, HeadingBlock):
                    self._render_heading(block)
                elif isinstance(block, BulletBlock):
                    self._render_bullets(block)
                elif isinstance(block, TableBlock):
                    self._render_table(block)
                elif isinstance(block, ImageBlock):
                    self._render_image(block)
                elif isinstance(block, PageBreakBlock):
                    self._render_page_break(block)
                elif isinstance(block, HeaderBlock):
                    self._render_header(block)
                elif isinstance(block, FooterBlock):
                    self._render_footer(block)

    def _render_text(self, block: TextBlock):
        """
        Render a text block using the TextBuilder.
        
        Args:
            block: A validated TextBlock object
        """
        # Create text builder if it doesn't exist
        if self.text_builder is None:
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

    def _render_header(self, block: HeaderBlock):
        """
        Render a header block using the HeaderFooterBuilder.
        
        Args:
            block: A validated HeaderBlock object
        """
        # Reset text builder when we encounter a non-text block
        self.text_builder = None
        
        # Import here to avoid circular imports
        from docxblocks.builders.header_footer import HeaderFooterBuilder
        
        builder = HeaderFooterBuilder(self.doc)
        builder.build_header(block)
        # Headers don't affect the current insertion index

    def _render_footer(self, block: FooterBlock):
        """
        Render a footer block using the HeaderFooterBuilder.
        
        Args:
            block: A validated FooterBlock object
        """
        # Reset text builder when we encounter a non-text block
        self.text_builder = None
        
        # Import here to avoid circular imports
        from docxblocks.builders.header_footer import HeaderFooterBuilder
        
        builder = HeaderFooterBuilder(self.doc)
        builder.build_footer(block)
        # Footers don't affect the current insertion index