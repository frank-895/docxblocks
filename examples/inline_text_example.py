"""
Inline Text Example

This example demonstrates how docxblocks groups consecutive text blocks inline
and handles paragraph breaks with newlines.
"""

from docx import Document
from docxblocks import DocxBuilder

def main():
    # Create a simple template
    doc = Document()
    doc.add_paragraph("{{content}}")
    doc.save("inline_text_template.docx")
    
    # Define blocks demonstrating inline text grouping
    blocks = [
        {
            "type": "heading",
            "text": "Inline Text Grouping Examples",
            "level": 1
        },
        {
            "type": "text",
            "text": "This document demonstrates how docxblocks groups text blocks:"
        },
        
        # Basic inline grouping
        {
            "type": "heading",
            "text": "Basic Inline Grouping",
            "level": 2
        },
        {
            "type": "text",
            "text": "This text is split into "
        },
        {
            "type": "text",
            "text": "multiple blocks that are ",
            "style": {"bold": True}
        },
        {
            "type": "text",
            "text": "grouped together inline."
        },
        
        # Mixed inline and paragraphs
        {
            "type": "heading",
            "text": "Mixed Inline and Paragraphs",
            "level": 2
        },
        {
            "type": "text",
            "text": "First paragraph with "
        },
        {
            "type": "text",
            "text": "inline grouping",
            "style": {"italic": True}
        },
        {
            "type": "text",
            "text": "\nSecond paragraph with "
        },
        {
            "type": "text",
            "text": "more inline text",
            "style": {"font_color": "FF0000"}
        },
        {
            "type": "text",
            "text": " and even more."
        },
        
        # Complex styling example
        {
            "type": "heading",
            "text": "Complex Styling Example",
            "level": 2
        },
        {
            "type": "text",
            "text": "This line contains "
        },
        {
            "type": "text",
            "text": "bold text",
            "style": {"bold": True}
        },
        {
            "type": "text",
            "text": ", "
        },
        {
            "type": "text",
            "text": "italic text",
            "style": {"italic": True}
        },
        {
            "type": "text",
            "text": ", and "
        },
        {
            "type": "text",
            "text": "colored text",
            "style": {"font_color": "0000FF"}
        },
        {
            "type": "text",
            "text": " all in one paragraph."
        },
        
        # Table with inline text
        {
            "type": "heading",
            "text": "Table with Inline Text",
            "level": 2
        },
        {
            "type": "table",
            "content": {
                "headers": ["Name", "Description"],
                "rows": [
                    [
                        "Item 1",
                        "This is a description with "
                    ],
                    [
                        "Item 2",
                        "More text that continues "
                    ]
                ]
            },
            "style": {
                "header_styles": {"bold": True, "bg_color": "f2f2f2"},
                "column_widths": [0.3, 0.7]
            }
        },
        {
            "type": "text",
            "text": "bold text",
            "style": {"bold": True}
        },
        {
            "type": "text",
            "text": " in the table cell."
        },
        
        # Summary
        {
            "type": "text",
            "text": "Summary:\n\n• Consecutive text blocks without \\n are grouped inline\n• Each block can have its own styling\n• Newlines (\\n) start new paragraphs\n• Perfect for complex formatting within paragraphs"
        }
    ]
    
    # Build the document
    builder = DocxBuilder("inline_text_template.docx")
    builder.insert("{{content}}", blocks)
    builder.save("inline_text_output.docx")

    print("Inline text example completed!")
    print("Check 'inline_text_output.docx' to see the result.")
    print("\nFeatures demonstrated:")
    print("- Consecutive text blocks are grouped inline")
    print("- Each block can have individual styling")
    print("- Newlines start new paragraphs")
    print("- Complex formatting within paragraphs")
    print("- Table cells support inline text grouping")

if __name__ == "__main__":
    main() 