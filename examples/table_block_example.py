from docx import Document
from docxblocks.core.inserter import DocxBuilder
from PIL import Image
import tempfile
import os

# Create a test image for the example
with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
    img = Image.new('RGB', (120, 60), color='blue')
    img.save(tmp_file.name, dpi=(96, 96))
    logo_path = tmp_file.name

doc = Document()
doc.add_paragraph("{{main}}")
doc.save("table_block_template.docx")

blocks = [
    {
        "type": "heading",
        "text": "Basic Table Example",
        "level": 1
    },
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
            "column_widths": [0.4, 0.3, "0.3"],
            "row_widths": [0.5, 0.4, 0.4, 0.4]
        }
    },
    {
        "type": "heading",
        "text": "Rich Content Table Example",
        "level": 1
    },
    {
        "type": "text",
        "text": "This table demonstrates rich content in cells including text, images, bullets, and headings:"
    },
    {
        "type": "table",
        "content": {
            "headers": ["Product", "Description", "Features", "Image"],
            "rows": [
                [
                    "Product A",
                    [
                        {"type": "heading", "text": "Premium Product", "level": 3},
                        {"type": "text", "text": "High-quality product with excellent features.", "style": {"italic": True}}
                    ],
                    [
                        {"type": "bullets", "items": ["Feature 1", "Feature 2", "Feature 3"]}
                    ],
                    [
                        {"type": "image", "path": logo_path, "style": {"max_width": "1in"}}
                    ]
                ],
                [
                    "Product B",
                    "Simple text description",
                    [
                        {"type": "bullets", "items": ["Basic feature", "Standard quality"]}
                    ],
                    "No image"
                ],
                [
                    "Product C",
                    [
                        {"type": "text", "text": "Description:", "style": {"bold": True}},
                        {"type": "text", "text": "Advanced product with multiple components."}
                    ],
                    [
                        {"type": "heading", "text": "Key Features", "level": 4},
                        {"type": "bullets", "items": ["Advanced feature 1", "Advanced feature 2"]}
                    ],
                    [
                        {"type": "image", "path": logo_path, "style": {"max_width": "0.8in"}}
                    ]
                ]
            ]
        },
        "style": {
            "header_styles": {"bold": True, "bg_color": "D0E0FF", "align": "center"},
            "column_widths": [0.2, 0.3, 0.3, 0.2]
        }
    }
]

builder = DocxBuilder("table_block_template.docx")
builder.insert("{{main}}", blocks)
builder.save("table_block_output.docx")

# Clean up the temporary image
os.unlink(logo_path)

print("Table block example generated: table_block_output.docx")
print("This example demonstrates both basic tables and rich content in cells!") 