from pydantic import BaseModel, Field, validator
from typing import Union, List, Literal, Optional

from docxblocks.schema.shared import TextStyle, TableStyle, ImageStyle


class BaseBlock(BaseModel):
    type: str


class TextBlock(BaseBlock):
    type: Literal["text"]
    text: str = Field(..., description="Text content - can be empty string")
    style: Optional[TextStyle] = None


class HeadingBlock(BaseBlock):
    type: Literal["heading"]
    text: str = Field(..., description="Heading text - can be empty string")
    level: int = Field(default=1, ge=1, le=6)
    style: Optional[TextStyle] = None


class BulletBlock(BaseBlock):
    type: Literal["bullets"]
    items: List[str] = Field(..., description="List of bullet items - can contain empty strings")
    style: Optional[TextStyle] = None


class TableBlock(BaseBlock):
    type: Literal["table"]
    content: dict = Field(..., description="Table content with headers and rows")
    style: Optional[TableStyle] = None


class ImageBlock(BaseBlock):
    type: Literal["image"]
    path: str = Field(..., description="Path to image file - can be empty or invalid")
    style: Optional[ImageStyle] = None


class PageBreakBlock(BaseBlock):
    type: Literal["page_break"]
    # No additional fields needed for a simple page break


class HeaderBlock(BaseBlock):
    type: Literal["header"]
    content: List[dict] = Field(..., description="List of block dictionaries for header content")
    apply_to: Optional[Literal["all", "first", "odd", "even", "all_except_first"]] = Field(default="all", description="Which pages to apply header to")


class FooterBlock(BaseBlock):
    type: Literal["footer"]
    content: List[dict] = Field(..., description="List of block dictionaries for footer content") 
    apply_to: Optional[Literal["all", "first", "odd", "even", "all_except_first"]] = Field(default="all", description="Which pages to apply footer to")


Block = Union[TextBlock, HeadingBlock, BulletBlock, TableBlock, ImageBlock, PageBreakBlock, HeaderBlock, FooterBlock]
