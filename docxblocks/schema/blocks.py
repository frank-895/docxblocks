from pydantic import BaseModel, Field
from typing import Union, List, Literal, Optional

from docxblocks.schema.shared import TextStyle, TableStyle, ImageStyle


class BaseBlock(BaseModel):
    type: str


class TextBlock(BaseBlock):
    type: Literal["text"]
    text: str
    style: Optional[TextStyle] = None


class HeadingBlock(BaseBlock):
    type: Literal["heading"]
    text: str
    level: int = Field(default=1, ge=1, le=6)
    style: Optional[TextStyle] = None


class BulletBlock(BaseBlock):
    type: Literal["bullets"]
    items: List[str]
    style: Optional[TextStyle] = None


class TableBlock(BaseBlock):
    type: Literal["table"]
    content: dict  # Could be refined later with more detailed schema
    style: Optional[TableStyle] = None


class ImageBlock(BaseBlock):
    type: Literal["image"]
    path: str
    style: Optional[ImageStyle] = None


Block = Union[TextBlock, HeadingBlock, BulletBlock, TableBlock, ImageBlock]
