"""
Newline Example

This example demonstrates the intelligent newline handling in docxblocks:
- Single \n characters remain as literal newlines (inline)
- Double \n\n creates new paragraphs with blank lines
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
            "text": "This document demonstrates how docxblocks handles different newline patterns:",
            "new_paragraph": True
        },
        
        # Text block examples
        {
            "type": "heading",
            "text": "Text Block Examples",
            "level": 2
        },
        {
            "type": "text",
            "text": "Single newlines remain inline:\nLine 1\nLine 2\nLine 3",
            "new_paragraph": True
        },
        {
            "type": "text",
            "text": "Double newlines create paragraphs:\n\nThis is a new paragraph with a blank line above it.\n\nAnd another paragraph with another blank line.",
            "new_paragraph": True
        },
        {
            "type": "text",
            "text": "Mixed usage:\nFirst line\nSecond line\n\nNew paragraph\n\nAnother paragraph",
            "new_paragraph": True
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
                        "All lines in one paragraph"
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
            "text": "Summary:\n\n• Single \\n: Remains inline within paragraphs\n• Double \\n\\n: Creates new paragraphs with blank lines\n• Works in text blocks, table headers, and table cells\n• Perfect for structured content with proper spacing",
            "new_paragraph": True
        }
    ]
    
    # Build the document
    builder = DocxBuilder("newline_template.docx")
    builder.insert("{{content}}", blocks)
    builder.save("newline_output.docx")
    
    print("Newline example completed!")
    print("Check 'newline_output.docx' to see the result.")
    print("\nFeatures demonstrated:")
    print("- Single \\n characters remain inline")
    print("- Double \\n\\n creates new paragraphs with blank lines")
    print("- Works in text blocks and table cells")
    print("- Mixed usage of single and double newlines")

if __name__ == "__main__":
    main() 