from pydantic import BaseModel, Field
from typing import Optional, List, Union, Literal

class TextStyle(BaseModel):
    bold: Optional[bool] = None
    italic: Optional[bool] = None
    align: Optional[Literal["left", "center", "right", "justify"]] = None
    font_color: Optional[str] = None  # Hex color like "FF0000"
    style: Optional[str] = None  # Word style name like "Normal", "Heading 1"

class TableStyle(BaseModel):
    column_widths: Optional[List[float]] = None  # Fractions of page width
    row_widths: Optional[List[float]] = None  # Fractions of page height
    header_styles: Optional[dict] = None  # Styling for header row
    column_styles: Optional[dict] = None  # Styling by column index
    row_styles: Optional[dict] = None  # Styling by row index
    cell_styles: Optional[dict] = None  # Styling by (row, col) tuple

class ImageStyle(BaseModel):
    max_width: Optional[str] = None   # E.g. "4in", "300px"
    max_height: Optional[str] = None
