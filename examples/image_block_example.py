from docx import Document
from docxblocks.core.inserter import DocxBuilder

doc = Document()
doc.add_paragraph("{{main}}")
doc.save("image_block_template.docx")

blocks = [
    {
        "type": "image",
        "path": "nonexistent_image.png",
        "style": {
            "max_width": "3in",
            "max_height": "2in"
        }
    }
]

builder = DocxBuilder("image_block_template.docx")
builder.insert("{{main}}", blocks)
builder.save("image_block_output.docx")
print("Image block example generated: image_block_output.docx") 