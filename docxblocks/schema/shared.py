from pydantic import BaseModel
from typing import Optional, Literal

class TextStyle(BaseModel):
    bold: Optional[bool] = False
    italic: Optional[bool] = False
    font_color: Optional[str] = None  # Hex string, e.g. "FF0000"
    align: Optional[Literal["left", "center", "right"]] = None
    style: Optional[str] = None       # Word paragraph style name

class TableStyle(BaseModel):
    header_styles: Optional[dict] = None  # Dict[str, Any]
    column_styles: Optional[dict] = None  # Dict[int, Any]
    row_styles: Optional[dict] = None     # Dict[int, Any] - styling by row index
    cell_styles: Optional[dict] = None    # Dict[Tuple[int, int], Any]
    column_widths: Optional[list] = None  # List[float] - width fractions for columns
    row_widths: Optional[list] = None     # List[float] - height fractions for rows

class ImageStyle(BaseModel):
    max_width: Optional[str] = None   # E.g. "4in", "300px"
    max_height: Optional[str] = None
