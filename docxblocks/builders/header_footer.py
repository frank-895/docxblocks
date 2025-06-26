"""
Header/Footer Builder Module

This module provides the HeaderFooterBuilder class for setting up headers and footers
in Word documents. It integrates with the existing block system to allow headers and
footers to contain the same content types as the main document.
"""

from docx.enum.section import WD_HEADER_FOOTER
from docxblocks.schema.blocks import HeaderBlock, FooterBlock
from docxblocks.builders.rich_text import RichTextBuilder


class HeaderFooterBuilder:
    """
    Builder class for configuring document headers and footers.
    
    This builder handles the setup of headers and footers across document sections,
    supporting different configurations for first page, odd/even pages, and all pages.
    Header and footer content can include any of the standard block types supported
    by the rich text builder.
    
    Attributes:
        doc: The python-docx Document object
    """
    
    def __init__(self, doc):
        """
        Initialize the HeaderFooterBuilder.
        
        Args:
            doc: The python-docx Document object
        """
        self.doc = doc

    def build_header(self, header_block: HeaderBlock, section_index: int = 0):
        """
        Build a header for the specified section.
        
        Args:
            header_block: A validated HeaderBlock object containing header configuration
            section_index: Index of the section to apply the header to (default: 0)
        """
        section = self.doc.sections[section_index]
        
        # Determine which header(s) to configure based on apply_to setting
        if header_block.apply_to == "all":
            self._configure_header(section.header, header_block.content)
        elif header_block.apply_to == "first":
            section.different_first_page_header_footer = True
            self._configure_header(section.first_page_header, header_block.content)
        elif header_block.apply_to == "all_except_first":
            # Enable different first page but leave first page header empty
            section.different_first_page_header_footer = True
            # Configure header for all pages except first (default header applies to pages 2+)
            self._configure_header(section.header, header_block.content)
        elif header_block.apply_to == "odd":
            # Set up odd/even headers - default header is used for odd pages
            self.doc.settings.odd_and_even_pages_header_footer = True
            self._configure_header(section.header, header_block.content)
        elif header_block.apply_to == "even":
            # Set up odd/even headers - even header is used for even pages
            self.doc.settings.odd_and_even_pages_header_footer = True
            self._configure_header(section.even_page_header, header_block.content)

    def build_footer(self, footer_block: FooterBlock, section_index: int = 0):
        """
        Build a footer for the specified section.
        
        Args:
            footer_block: A validated FooterBlock object containing footer configuration
            section_index: Index of the section to apply the footer to (default: 0)
        """
        section = self.doc.sections[section_index]
        
        # Determine which footer(s) to configure based on apply_to setting
        if footer_block.apply_to == "all":
            self._configure_footer(section.footer, footer_block.content)
        elif footer_block.apply_to == "first":
            section.different_first_page_header_footer = True
            self._configure_footer(section.first_page_footer, footer_block.content)
        elif footer_block.apply_to == "all_except_first":
            # Enable different first page but leave first page footer empty
            section.different_first_page_header_footer = True
            # Configure footer for all pages except first (default footer applies to pages 2+)
            self._configure_footer(section.footer, footer_block.content)
        elif footer_block.apply_to == "odd":
            # Set up odd/even footers - default footer is used for odd pages
            self.doc.settings.odd_and_even_pages_header_footer = True
            self._configure_footer(section.footer, footer_block.content)
        elif footer_block.apply_to == "even":
            # Set up odd/even footers - even footer is used for even pages
            self.doc.settings.odd_and_even_pages_header_footer = True
            self._configure_footer(section.even_page_footer, footer_block.content)

    def _configure_header(self, header, content_blocks):
        """
        Configure a specific header with the provided content blocks.
        
        Args:
            header: The python-docx header object (_Header)
            content_blocks: List of block dictionaries to render in the header
        """
        # Clear any existing content
        for paragraph in header.paragraphs:
            p_element = paragraph._element
            p_element.getparent().remove(p_element)
        
        # Add content using the rich text builder
        builder = RichTextBuilder(self.doc, header._element, 0)
        builder.render(content_blocks)

    def _configure_footer(self, footer, content_blocks):
        """
        Configure a specific footer with the provided content blocks.
        
        Args:
            footer: The python-docx footer object (_Footer)
            content_blocks: List of block dictionaries to render in the footer
        """
        # Clear any existing content
        for paragraph in footer.paragraphs:
            p_element = paragraph._element
            p_element.getparent().remove(p_element)
        
        # Add content using the rich text builder
        builder = RichTextBuilder(self.doc, footer._element, 0)
        builder.render(content_blocks) 