"""
Page Break Example

This example demonstrates the new page break functionality for creating
multi-page documents with proper page breaks.
"""

from docx import Document
from docxblocks import DocxBuilder

def main():
    # Create a simple template
    doc = Document()
    doc.add_paragraph("{{content}}")
    doc.save("page_break_template.docx")
    
    # Define blocks with page breaks
    blocks = [
        # First page content
        {"type": "heading", "text": "Executive Summary", "level": 1},
        {"type": "text", "text": "This is the first page of our report."},
        {"type": "text", "text": "It contains the executive summary and key findings."},
        
        # Page break to second page
        {"type": "page_break"},
        
        # Second page content
        {"type": "heading", "text": "Detailed Analysis", "level": 1},
        {"type": "text", "text": "This is the second page with detailed analysis."},
        {
            "type": "table",
            "content": {
                "headers": ["Metric", "Value", "Status"],
                "rows": [
                    ["Revenue", "$1.2M", "Good"],
                    ["Growth", "15%", "Excellent"],
                    ["Efficiency", "85%", "Good"]
                ]
            },
            "style": {
                "header_styles": {"bold": True, "bg_color": "f2f2f2"}
            }
        },
        
        # Page break to third page
        {"type": "page_break"},
        
        # Third page content
        {"type": "heading", "text": "Conclusions", "level": 1},
        {"type": "text", "text": "This is the final page with conclusions."},
        {"type": "bullets", "items": [
            "Overall performance is strong",
            "Key metrics are trending upward",
            "Recommendations for next quarter"
        ]},
    ]
    
    # Build the document
    builder = DocxBuilder("page_break_template.docx")
    builder.insert("{{content}}", blocks)
    builder.save("page_break_output.docx")
    
    print("Page break example completed!")
    print("Check 'page_break_output.docx' to see the result.")
    print("\nKey features demonstrated:")
    print("- Page breaks between different sections")
    print("- Multi-page document structure")
    print("- Combination of page breaks with other block types")
    print("- Proper document flow across pages")

if __name__ == "__main__":
    main() 