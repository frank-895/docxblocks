"""
Newline Example

This example demonstrates the simple newline handling in docxblocks:
- Every \n creates a new paragraph
- Every \n\n creates a new paragraph with a blank paragraph in between
- Text continues inline in the same paragraph unless \n is specified
- Works in both text blocks and table cells
- Mixed usage of single and double newlines
"""

from docx import Document
from docxblocks import DocxBuilder

def main():
    # Create a simple template
    doc = Document()
    doc.add_paragraph("{{content}}")
    doc.save("newline_template.docx")
    
    # Define blocks demonstrating newline functionality
    blocks = [
        {
            "type": "heading",
            "text": "Newline Handling Examples",
            "level": 1
        },
        {
            "type": "text",
            "text": "This document demonstrates how docxblocks handles different newline patterns:"
        },
        
        # Text block examples
        {
            "type": "heading",
            "text": "Text Block Examples",
            "level": 2
        },
        {
            "type": "text",
            "text": "Every newline creates a new paragraph:\nLine 1\nLine 2\nLine 3"
        },
        {
            "type": "text",
            "text": "Double newlines create paragraphs with blank lines:\n\nThis is a new paragraph with a blank line above it.\n\nAnd another paragraph with another blank line."
        },
        {
            "type": "text",
            "text": "Mixed usage:\nFirst line\nSecond line\n\nNew paragraph\n\nAnother paragraph"
        },
        
        # Table examples
        {
            "type": "heading",
            "text": "Table Cell Examples",
            "level": 2
        },
        {
            "type": "table",
            "content": {
                "headers": ["Type", "Example", "Result"],
                "rows": [
                    [
                        "Single \\n",
                        "Line 1\nLine 2\nLine 3",
                        "Each \\n creates a new paragraph"
                    ],
                    [
                        "Double \\n\\n",
                        "First paragraph.\n\nSecond paragraph.",
                        "Two paragraphs with blank line"
                    ],
                    [
                        "Mixed",
                        "Line 1\nLine 2\n\nNew paragraph\n\nAnother",
                        "Inline + paragraphs with blanks"
                    ],
                    [
                        "Header with \\n\\n",
                        "Description\n\nDetails",
                        "Header with two parts"
                    ]
                ]
            },
            "style": {
                "header_styles": {"bold": True, "bg_color": "f2f2f2"},
                "column_widths": [0.2, 0.4, 0.4]
            }
        },
        
        # Summary
        {
            "type": "text",
            "text": "Summary:\n\n• Every \\n: Creates a new paragraph\n• Every \\n\\n: Creates a new paragraph with a blank paragraph in between\n• Text continues inline in the same paragraph unless \\n is specified\n• Works in text blocks, table headers, and table cells\n• Perfect for structured content with proper spacing"
        }
    ]
    
    # Build the document
    builder = DocxBuilder("newline_template.docx")
    builder.insert("{{content}}", blocks)
    builder.save("newline_output.docx")

    # User's contact info scenario
    contact_blocks = [
        {
            "type": "text",
            "text": "First paragraph"
        },
        {
            "type": "text",
            "text": "\n\nPlease feel free to contact me should you have further queries. I can be contacted on "
        },
        {
            "type": "text",
            "text": "123-456-7890"
        },
        {
            "type": "text",
            "text": " or "
        },
        {
            "type": "text",
            "text": "test@example.com"
        },
    ]
    builder2 = DocxBuilder("newline_template.docx")
    builder2.insert("{{content}}", contact_blocks)
    builder2.save("newline_contact_output.docx")

    print("Newline example completed!")
    print("Check 'newline_output.docx' to see the result.")
    print("\nFeatures demonstrated:")
    print("- Every \\n creates a new paragraph")
    print("- Every \\n\\n creates a new paragraph with a blank paragraph in between")
    print("- Text continues inline in the same paragraph unless \\n is specified")
    print("- Works in text blocks and table cells")
    print("- Mixed usage of single and double newlines")
    print("\nContact info test completed! Check 'newline_contact_output.docx' for the result.")

if __name__ == "__main__":
    main() 