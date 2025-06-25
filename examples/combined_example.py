from docx import Document
from docxblocks.core.inserter import DocxBuilder

doc = Document()
doc.add_paragraph("{{main}}")
doc.save("combined_template.docx")

blocks = [
    {
        "type": "heading",
        "text": "Report Title",
        "level": 1,
        "style": {"align": "center", "bold": True}
    },
    {
        "type": "text",
        "text": "This is a summary section.\nIt supports multiple lines.",
        "style": {"italic": True, "align": "left"}
    },
    {
        "type": "bullets",
        "items": ["First bullet", "Second bullet", "Third bullet"],
        "style": {"font_color": "008000"}
    },
    {
        "type": "table",
        "content": {
            "headers": ["Metric", "Value"],
            "rows": [["Accuracy", "95%"], ["Loss", "0.05"]]
        },
        "style": {"header_styles": {"bg_color": "E0E0E0"}}
    },
    {
        "type": "image",
        "path": "nonexistent.png",
        "style": {"max_width": "2in"}
    }
]

builder = DocxBuilder("combined_template.docx")
builder.insert("{{main}}", blocks)
builder.save("combined_output.docx")
print("Combined example generated: combined_output.docx") 