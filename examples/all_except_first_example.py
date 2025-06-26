from docx import Document
from docxblocks.core.inserter import DocxBuilder

# Create a simple template
doc = Document()
doc.add_paragraph("{{content}}")
doc.save("all_except_first_template.docx")

# Example: Clean first page (like a cover page) with headers/footers on subsequent pages
blocks = [
    # Header for all pages except the first
    {
        "type": "header",
        "apply_to": "all_except_first",
        "content": [
            {
                "type": "text",
                "text": "Company Report\tConfidential\tPage {{page}}",
                "style": {"align": "center", "font_color": "666666"}
            }
        ]
    },
    
    # Footer for all pages except the first
    {
        "type": "footer",
        "apply_to": "all_except_first",
        "content": [
            {
                "type": "text",
                "text": "© 2024 Company Name\tInternal Use Only\t{{date}}",
                "style": {"align": "center", "font_color": "999999", "italic": True}
            }
        ]
    },
    
    # Page 1: Cover page (clean, no header/footer)
    {
        "type": "heading",
        "text": "ANNUAL REPORT 2024",
        "level": 1,
        "style": {"align": "center", "bold": True}
    },
    {
        "type": "text",
        "text": "\n\n\n",  # Add some space
    },
    {
        "type": "text",
        "text": "Company Name",
        "style": {"align": "center", "bold": True}
    },
    {
        "type": "text",
        "text": "Fiscal Year 2024 Results",
        "style": {"align": "center", "italic": True}
    },
    {
        "type": "text",
        "text": "\n\n\n\nPrepared by: Finance Department\nDate: January 2025",
        "style": {"align": "center"}
    },
    
    # Page break to next page
    {
        "type": "page_break"
    },
    
    # Page 2: Content with header/footer
    {
        "type": "heading",
        "text": "Executive Summary",
        "level": 1
    },
    {
        "type": "text",
        "text": "This page and all subsequent pages will have the header and footer. The first page (cover page) remains clean without any header or footer content."
    },
    {
        "type": "text",
        "text": "This is perfect for reports, proposals, and documents where you want a professional cover page followed by structured content pages."
    },
    
    # Page break to demonstrate on multiple pages
    {
        "type": "page_break"
    },
    
    # Page 3: More content with header/footer
    {
        "type": "heading",
        "text": "Financial Overview",
        "level": 1
    },
    {
        "type": "text",
        "text": "This is page 3, which also has the header and footer. Notice how the page numbering and headers work consistently across all pages except the first."
    },
    {
        "type": "table",
        "content": {
            "headers": ["Metric", "2023", "2024", "Change"],
            "rows": [
                ["Revenue", "$1.2M", "$1.5M", "+25%"],
                ["Profit", "$200K", "$300K", "+50%"],
                ["Employees", "25", "32", "+28%"]
            ]
        },
        "style": {
            "header_styles": {"bold": True, "bg_color": "E0E0E0"}
        }
    }
]

# Build the document
builder = DocxBuilder("all_except_first_template.docx")
builder.insert("{{content}}", blocks)
builder.save("all_except_first_output.docx")
print("All-except-first example generated: all_except_first_output.docx")
print("Note: Page 1 has no header/footer, pages 2+ have headers and footers") 