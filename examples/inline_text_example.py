"""
Inline Text Example

This example demonstrates the new inline text functionality where text blocks
are inline by default and only create new paragraphs when explicitly specified.
"""

from docx import Document
from docxblocks import DocxBuilder

def main():
    # Create a simple template
    doc = Document()
    doc.add_paragraph("{{content}}")
    doc.save("inline_text_template.docx")
    
    # Define blocks with inline text
    blocks = [
        # Inline text blocks - these will all be on the same line
        {"type": "text", "text": "Participant Name: "},
        {"type": "text", "text": "John Doe", "style": {"bold": True}},
        {"type": "text", "text": " (ID: "},
        {"type": "text", "text": "12345", "style": {"font_color": "007700"}},
        {"type": "text", "text": ")"},
        
        # Force a new paragraph
        {"type": "text", "text": "Status: Active", "new_paragraph": True},
        
        # More inline text
        {"type": "text", "text": "This is a "},
        {"type": "text", "text": "summary", "style": {"bold": True, "italic": True}},
        {"type": "text", "text": " of the participant's information."},
        
        # A heading (always creates a new paragraph)
        {"type": "heading", "text": "Contact Details", "level": 2},
        
        # More inline text after the heading
        {"type": "text", "text": "Phone: "},
        {"type": "text", "text": "555-1234", "style": {"font_color": "0000FF"}},
        {"type": "text", "text": " | Email: "},
        {"type": "text", "text": "john.doe@example.com", "style": {"font_color": "0000FF"}},
    ]
    
    # Build the document
    builder = DocxBuilder("inline_text_template.docx")
    builder.insert("{{content}}", blocks)
    builder.save("inline_text_output.docx")
    
    print("Inline text example completed!")
    print("Check 'inline_text_output.docx' to see the result.")
    print("\nKey features demonstrated:")
    print("- Text blocks are inline by default (no new paragraphs)")
    print("- Use 'new_paragraph: true' to force a new paragraph")
    print("- Different styling can be applied to inline text segments")
    print("- Headings and other block types still create new paragraphs")

if __name__ == "__main__":
    main() 