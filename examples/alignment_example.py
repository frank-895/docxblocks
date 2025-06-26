from docx import Document
from docxblocks.core.inserter import DocxBuilder

def main():
    # Create a simple template
    doc = Document()
    doc.add_paragraph("{{content}}")
    doc.save("alignment_template.docx")
    
    # Define comprehensive alignment examples
    blocks = [
        # Title
        {
            "type": "heading",
            "text": "DocxBlocks Alignment Examples",
            "level": 1,
            "style": {"align": "center", "bold": True}
        },
        
        # Text block alignments
        {
            "type": "heading",
            "text": "Text Block Alignments",
            "level": 2,
            "style": {"align": "left"}
        },
        {
            "type": "text",
            "text": "Left aligned text - This text is aligned to the left margin.",
            "style": {"align": "left"}
        },
        {
            "type": "text", 
            "text": "Center aligned text - This text is centered between margins.",
            "style": {"align": "center"}
        },
        {
            "type": "text",
            "text": "Right aligned text - This text is aligned to the right margin.", 
            "style": {"align": "right"}
        },
        {
            "type": "text",
            "text": "Justified text - This is a longer paragraph that demonstrates text justification. When text is justified, it is aligned to both the left and right margins by adjusting the spacing between words. This creates a clean, professional appearance often used in books and formal documents.",
            "style": {"align": "justify"}
        },
        
        # Multi-line text alignment
        {
            "type": "heading",
            "text": "Multi-line Text Alignment",
            "level": 3,
            "style": {"align": "left"}
        },
        {
            "type": "text",
            "text": "First centered line\nSecond centered line\nThird centered line",
            "style": {"align": "center"}
        },
        {
            "type": "text",
            "text": "Justified paragraph one\n\nJustified paragraph two with enough text to demonstrate how justification works across multiple paragraphs in the same text block.",
            "style": {"align": "justify"}
        },
        
        # Heading alignments
        {
            "type": "heading",
            "text": "Heading Alignments",
            "level": 2,
            "style": {"align": "left"}
        },
        {
            "type": "heading",
            "text": "Left Aligned Heading",
            "level": 3,
            "style": {"align": "left"}
        },
        {
            "type": "heading",
            "text": "Center Aligned Heading",
            "level": 3,
            "style": {"align": "center"}
        },
        {
            "type": "heading",
            "text": "Right Aligned Heading",
            "level": 3,
            "style": {"align": "right"}
        },
        {
            "type": "heading",
            "text": "Justified Heading",
            "level": 3,
            "style": {"align": "justify"}
        },
        
        # Bullet list alignments
        {
            "type": "heading",
            "text": "Bullet List Alignments",
            "level": 2,
            "style": {"align": "left"}
        },
        {
            "type": "text",
            "text": "Left aligned bullets:",
            "style": {"bold": True}
        },
        {
            "type": "bullets",
            "items": ["Left bullet item one", "Left bullet item two"],
            "style": {"align": "left"}
        },
        {
            "type": "text",
            "text": "Center aligned bullets:",
            "style": {"bold": True}
        },
        {
            "type": "bullets",
            "items": ["Center bullet item one", "Center bullet item two"],
            "style": {"align": "center"}
        },
        {
            "type": "text",
            "text": "Right aligned bullets:",
            "style": {"bold": True}
        },
        {
            "type": "bullets",
            "items": ["Right bullet item one", "Right bullet item two"],
            "style": {"align": "right"}
        },
        {
            "type": "text",
            "text": "Justified bullets:",
            "style": {"bold": True}
        },
        {
            "type": "bullets",
            "items": ["Justified bullet item with longer text to demonstrate alignment", "Another justified bullet item"],
            "style": {"align": "justify"}
        },
        
        # Table alignments
        {
            "type": "heading",
            "text": "Table Alignments",
            "level": 2,
            "style": {"align": "left"}
        },
        
        # Header alignment example
        {
            "type": "text",
            "text": "Header Alignment Examples:",
            "style": {"bold": True}
        },
        {
            "type": "table",
            "content": {
                "headers": ["Left Header", "Center Header", "Right Header", "Justified Header"],
                "rows": [
                    ["Sample data", "Sample data", "Sample data", "Sample data with more text"]
                ]
            },
            "style": {
                "header_styles": {"align": "left", "bold": True, "bg_color": "e6f3ff"},
                "column_widths": [0.25, 0.25, 0.25, 0.25]
            }
        },
        
        # Column alignment example
        {
            "type": "text",
            "text": "Column Alignment Examples:",
            "style": {"bold": True}
        },
        {
            "type": "table",
            "content": {
                "headers": ["Left Column", "Center Column", "Right Column", "Justified Column"],
                "rows": [
                    ["Left text", "Center text", "Right text", "Justified text with longer content"],
                    ["More left", "More center", "More right", "More justified text for demonstration"],
                    ["Even more", "Even more", "Even more", "Even more justified content for testing"]
                ]
            },
            "style": {
                "header_styles": {"bold": True, "bg_color": "f0f0f0"},
                "column_styles": {
                    0: {"align": "left"},
                    1: {"align": "center"},
                    2: {"align": "right"},
                    3: {"align": "justify"}
                },
                "column_widths": [0.25, 0.25, 0.25, 0.25]
            }
        },
        
        # Row alignment example
        {
            "type": "text",
            "text": "Row Alignment Examples:",
            "style": {"bold": True}
        },
        {
            "type": "table",
            "content": {
                "headers": ["Column 1", "Column 2"],
                "rows": [
                    ["Left row cell 1", "Left row cell 2"],
                    ["Center row cell 1", "Center row cell 2"],
                    ["Right row cell 1", "Right row cell 2"],
                    ["Justified row cell 1", "Justified row cell 2 with longer text"]
                ]
            },
            "style": {
                "header_styles": {"bold": True, "bg_color": "f0f0f0"},
                "row_styles": {
                    0: {"align": "left", "bg_color": "fff0f0"},
                    1: {"align": "center", "bg_color": "f0fff0"},
                    2: {"align": "right", "bg_color": "f0f0ff"},
                    3: {"align": "justify", "bg_color": "fffff0"}
                },
                "column_widths": [0.5, 0.5]
            }
        },
        
        # Individual cell alignment example
        {
            "type": "text",
            "text": "Individual Cell Alignment Examples:",
            "style": {"bold": True}
        },
        {
            "type": "table",
            "content": {
                "headers": ["Mixed Alignments", "Description"],
                "rows": [
                    ["Left cell", "Center cell"],
                    ["Right cell", "Justified cell with longer text content for demonstration"]
                ]
            },
            "style": {
                "header_styles": {"bold": True, "bg_color": "f0f0f0"},
                "cell_styles": {
                    (0, 0): {"align": "left", "bg_color": "fff0f0"},
                    (0, 1): {"align": "center", "bg_color": "f0fff0"},
                    (1, 0): {"align": "right", "bg_color": "f0f0ff"},
                    (1, 1): {"align": "justify", "bg_color": "fffff0"}
                },
                "column_widths": [0.3, 0.7]
            }
        },
        
        # Multi-line content in table cells
        {
            "type": "text",
            "text": "Multi-line Cell Content Alignment:",
            "style": {"bold": True}
        },
        {
            "type": "table",
            "content": {
                "headers": ["Multi-line Content"],
                "rows": [
                    ["Line 1\nLine 2\nLine 3 - all justified"],
                    ["Paragraph 1\n\nParagraph 2 with longer text - all centered"]
                ]
            },
            "style": {
                "header_styles": {"bold": True, "bg_color": "f0f0f0"},
                "row_styles": {
                    0: {"align": "justify"},
                    1: {"align": "center"}
                }
            }
        },
        
        # Summary
        {
            "type": "heading",
            "text": "Summary",
            "level": 2,
            "style": {"align": "center"}
        },
        {
            "type": "text",
            "text": "This document demonstrates all four alignment options (left, center, right, justify) across all DocxBlocks block types:\n\n• Text blocks (single and multi-line)\n• Headings (levels 1-6)\n• Bullet lists\n• Table headers\n• Table columns\n• Table rows\n• Individual table cells\n• Multi-line content in table cells\n\nAll alignment features work consistently across the entire DocxBlocks library.",
            "style": {"align": "justify"}
        }
    ]
    
    # Build the document
    builder = DocxBuilder("alignment_template.docx")
    builder.insert("{{content}}", blocks)
    builder.save("alignment_output.docx")
    
    print("Comprehensive alignment example generated: alignment_output.docx")
    print("\nThis example demonstrates:")
    print("- Text alignment: left, center, right, justify")
    print("- Heading alignment: all levels and alignments")
    print("- Bullet list alignment: all alignment options")
    print("- Table header alignment")
    print("- Table column alignment")
    print("- Table row alignment")
    print("- Individual table cell alignment")
    print("- Multi-line content alignment in text and table cells")

if __name__ == "__main__":
    main() 