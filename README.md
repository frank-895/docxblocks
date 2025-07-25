# DocxBlocks

A Python library for building Word documents using a block-based API. Create complex documents with simple, readable code.

## 🚀 Quick Start

```python
from docxblocks import DocxBuilder

# Create blocks
blocks = [
    {"type": "heading", "text": "Report Title", "level": 1},
    {"type": "text", "text": "This is the first paragraph."},
    {"type": "text", "text": "This continues inline."},
    {"type": "text", "text": "\nThis starts a new paragraph."},
    {"type": "table", "content": {
        "headers": ["Name", "Value"],
        "rows": [["Item 1", "100"], ["Item 2", "200"]]
    }}
]

# Build document
builder = DocxBuilder("template.docx")
builder.insert("{{content}}", blocks)
builder.save("output.docx")
```

## 📋 Features

- **Block-based API**: Each piece of content is a simple dictionary
- **Smart text grouping**: Consecutive text blocks are grouped inline
- **Simple newlines**: Every `\n` creates a new paragraph
- **Rich styling**: Bold, italic, colors, alignment, and more
- **Table support**: Headers, rows, column widths, cell styling
- **Image handling**: Automatic sizing with DPI calculation
- **Template support**: Use existing Word templates as starting points
- **Error handling**: Graceful fallbacks for missing content

## 📖 Installation

```bash
pip install docxblocks
```

## 🎯 Basic Usage

### Template Setup

Create a Word document with placeholders:

```
{{header}}

{{main}}

{{footer}}
```

### Block-Based API (Core Concept)

Each piece of content is a block:

```python
{
  "type": "text",
  "text": "All systems operational.",
  "style": {
    "bold": True,
    "italic": False,
    "font_color": "007700",
    "align": "center",
    "style": "Normal"
  }
}
```

### Text Block Behavior

Text blocks have simple, predictable behavior:

- **Every `\n`**: Always starts a new paragraph
- **Inline grouping**: Consecutive text blocks without `\n` are grouped together
- **`spacing`**: Adds extra blank paragraphs after the block

```python
{"type": "text", "text": "Line 1\nLine 2\nLine 3"}
# Renders as three paragraphs: Line 1, Line 2, Line 3

{"type": "text", "text": "First paragraph\n\nSecond paragraph"}
# Renders as: First paragraph, [blank paragraph], Second paragraph

{"type": "text", "text": "First", "spacing": 1}
# Renders as a new paragraph, then one blank paragraph after
```

### Table Cell Behavior

Table cells and headers follow the same rules:

- **Every `\n`**: Always starts a new paragraph within the cell
- **Inline grouping**: Consecutive cell blocks without `\n` are grouped together

```python
{
    "type": "table",
    "content": {
        "headers": ["Name", "Description\nDetails"],
        "rows": [
            ["Item 1", "First paragraph.\nSecond paragraph."],
            ["Item 2", "Line 1\n\nLine 2 with empty line above"]
        ]
    }
}
# Each '\n' creates a new paragraph, each '\n\n' creates paragraph with empty line before
```

Block types:

| Type         | Required Keys     | Optional Keys     |
|--------------|-------------------|-------------------|
| `text`       | `text`            | `style`, `spacing`| 
| `heading`    | `text`, `level`   | `style`           |
| `bullets`    | `items`           | `style`           |
| `table`      | `content`         | `style`           |
| `image`      | `path`            | `style`           |
| `page_break` | -                 | -                 |
| `header`     | `content`         | `apply_to`        |
| `footer`     | `content`         | `apply_to`        |

## 🎨 Styling

### Text Styling
```python
{
    "type": "text",
    "text": "Styled text",
    "style": {
        "bold": True,
        "italic": False,
        "font_color": "FF0000",  # Red
        "align": "center",       # "left", "center", "right", "justify"
        "style": "Normal"
    }
}
```

### Alignment Options
All block types support four alignment options:
```python
# Text alignment examples
{"type": "text", "text": "Left aligned", "style": {"align": "left"}}
{"type": "text", "text": "Centered text", "style": {"align": "center"}}
{"type": "text", "text": "Right aligned", "style": {"align": "right"}}
{"type": "text", "text": "Justified text that adjusts spacing for clean edges", "style": {"align": "justify"}}

# Works with all block types
{"type": "heading", "text": "Centered Heading", "level": 1, "style": {"align": "center"}}
{"type": "bullets", "items": ["Item 1", "Item 2"], "style": {"align": "right"}}
```

### Table Styling
```python
{
    "type": "table",
    "content": {"headers": ["A", "B"], "rows": [["1", "2"]]},
    "style": {
        "column_widths": [0.3, 0.7],
        "header_styles": {"bold": True, "bg_color": "f2f2f2"},
        "column_styles": {0: {"font_color": "FF0000"}}
    }
}
```

**Rich Content in Cells:** Table cells can contain text, images, bullets, and headings. See [STYLEGUIDE.md](STYLEGUIDE.md) for examples.

### Image Styling
```python
{
    "type": "image",
    "path": "logo.png",
    "style": {
        "max_width": "4in",
        "max_height": "300px",
        "wrap_text": "square",
        "horizontal_align": "left",
        "vertical_align": "top",
        "distance_from_text": "0.1in"
    }
}
```

**Text Wrapping Options:** `inline`, `square`, `tight`, `through`, `top_and_bottom`, `behind`, `in_front`

**Positioning:** `horizontal_align` (left/center/right), `vertical_align` (top/middle/bottom), `distance_from_text`

See [STYLEGUIDE.md](STYLEGUIDE.md) for comprehensive styling examples.

## 📄 Headers and Footers

DocxBlocks supports customizable headers and footers that can contain any combination of supported block types.

### Basic Usage
```python
blocks = [
    {
        "type": "header",
        "apply_to": "all",
        "content": [
            {
                "type": "text",
                "text": "Company Name\tDocument Title\tPage {{page}}",
                "style": {"align": "center", "font_color": "666666"}
            }
        ]
    },
    {
        "type": "footer", 
        "apply_to": "all_except_first",
        "content": [
            {
                "type": "text",
                "text": "© 2024 Company. All rights reserved.",
                "style": {"align": "center", "italic": True}
            }
        ]
    }
]
```

**Apply To Options:** `"all"`, `"all_except_first"`, `"first"`, `"odd"`, `"even"`

See [STYLEGUIDE.md](STYLEGUIDE.md) for advanced examples including images and tables in headers/footers.

## 🔧 Advanced Features

### Mixed Content
```python
blocks = [
    {"type": "heading", "text": "Section 1", "level": 2},
    {"type": "text", "text": "Introduction "},
    {"type": "text", "text": "with ", "style": {"bold": True}},
    {"type": "text", "text": "inline styling."},
    {"type": "bullets", "items": ["Point 1", "Point 2"]},
    {"type": "table", "content": {...}},
    {"type": "page_break"},
    {"type": "heading", "text": "Section 2", "level": 2}
]
```

### Template Variables
```python
# Template.docx contains: "Hello {{name}}, here is your {{report_type}} report."

builder = DocxBuilder("template.docx")
builder.insert("{{name}}", [{"type": "text", "text": "John"}])
builder.insert("{{report_type}}", [{"type": "text", "text": "monthly"}])
builder.save("output.docx")
```

## 📚 Examples

See the `examples/` directory for complete working examples:

- `text_block_example.py` - Basic text blocks and styling
- `table_block_example.py` - Table creation and styling
- `header_footer_example.py` - Headers and footers with various configurations
- `all_except_first_example.py` - Cover page example with clean first page and headers on content pages
- `newline_example.py` - Newline handling and paragraph behavior
- `inline_text_example.py` - Inline text grouping
- `alignment_example.py` - Text alignment with left, center, right, and justify
- `combined_example.py` - Mixed block types

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🐛 Issues

Found a bug? Have a feature request? Please open an issue on GitHub.