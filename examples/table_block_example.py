from docx import Document
from docxblocks.core.inserter import DocxBuilder

doc = Document()
doc.add_paragraph("{{main}}")
doc.save("table_block_template.docx")

blocks = [
    {
        "type": "table",
        "content": {
            "headers": ["Name", "Age", "City"],
            "rows": [
                ["Alice", "30", "London"],
                ["Bob", "25", "Paris"],
                ["Charlie", "35", "Berlin"]
            ]
        },
        "style": {
            "header_styles": {"bold": True, "bg_color": "E0E0E0"},
            "column_styles": {0: {"bold": True}},
            "row_styles": {1: {"bg_color": "FFF8DC"}},
            "cell_styles": {(2, 2): {"font_color": "FF0000"}},
            "column_widths": [0.4, 0.3, 0.3],
            "row_widths": [0.5, 0.4, 0.4, 0.4]
        }
    }
]

builder = DocxBuilder("table_block_template.docx")
builder.insert("{{main}}", blocks)
builder.save("table_block_output.docx")
print("Table block example generated: table_block_output.docx") 