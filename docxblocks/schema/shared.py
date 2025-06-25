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
    cell_styles: Optional[dict] = None    # Dict[Tuple[int, int], Any]
    column_widths: Optional[list] = None  # List[float]

class ImageStyle(BaseModel):
    max_width: Optional[str] = None   # E.g. "4in", "300px"
    max_height: Optional[str] = None
