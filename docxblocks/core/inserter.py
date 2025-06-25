from docx import Document
from docxblocks.utils.placeholder import find_placeholder_paragraph
from docxblocks.builders.rich_text import RichTextBuilder

class DocxBuilder:
    def __init__(self, template_path):
        self.doc = Document(template_path)

    def insert(self, placeholder, blocks: list):
        paragraph = find_placeholder_paragraph(self.doc, placeholder)
        if not paragraph:
            raise ValueError(f"Placeholder '{placeholder}' not found.")

        parent = paragraph._element.getparent()
        index = parent.index(paragraph._element)
        parent.remove(paragraph._element)

        builder = RichTextBuilder(self.doc, parent, index)
        builder.render(blocks)

    def save(self, output_path):
        self.doc.save(output_path)
