from docx import Document
from docxblocks.core.inserter import DocxBuilder

doc = Document()
doc.add_paragraph("{{main}}")
doc.save("text_block_template.docx")

blocks = [
    {
        "type": "text",
        "text": "Hello, world!\nThis is a multi-line text block.",
        "style": {
            "bold": True,
            "font_color": "1E90FF",
            "align": "center"
        }
    }
]

builder = DocxBuilder("text_block_template.docx")
builder.insert("{{main}}", blocks)
builder.save("text_block_output.docx")
print("Text block example generated: text_block_output.docx") 