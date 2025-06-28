# DocxBlocks Style Guide

This guide provides comprehensive documentation for styling and formatting options available in DocxBlocks.

## Block Types

### Text Blocks
```python
{
    "type": "text",
    "text": "Your text content here",
    "style": {
        "bold": True,
        "italic": False,
        "font_color": "FF0000",
        "align": "center",
        "style": "Normal"
    },
    "spacing": 2
}
```

### Heading Blocks
```python
{
    "type": "heading",
    "text": "Your heading",
    "level": 1,  # 1-6
    "style": {
        "bold": True,
        "font_color": "0000FF",
        "align": "left"
    }
}
```

### Bullet Lists
```python
{
    "type": "bullets",
    "items": ["Item 1", "Item 2", "Item 3"],
    "style": {
        "bold": False,
        "font_color": "000000",
        "align": "left"
    }
}
```

### Tables
```python
{
    "type": "table",
    "content": {
        "headers": ["Header 1", "Header 2"],
        "rows": [
            ["Row 1 Col 1", "Row 1 Col 2"],
            ["Row 2 Col 1", "Row 2 Col 2"]
        ]
    },
    "style": {
        "column_widths": [0.5, 0.5],
        "header_styles": {"bold": True, "bg_color": "f2f2f2"},
        "column_styles": {0: {"font_color": "FF0000"}},
        "row_styles": {0: {"bg_color": "e6e6e6"}},
        "cell_styles": {(0, 0): {"bold": True}}
    }
}
```

#### Rich Content in Table Cells

Table cells can contain either plain text (string) or rich content (list of block dictionaries):

```python
{
    "type": "table",
    "content": {
        "headers": ["Product", "Description", "Features", "Image"],
        "rows": [
            [
                "Product A",
                [
                    {"type": "heading", "text": "Premium Product", "level": 3},
                    {"type": "text", "text": "High-quality product with excellent features.", "style": {"italic": True}},
                    {"type": "image", "path": "logo.png", "style": {"max_width": "1in", "wrap_text": "inline"}},
                    {"type": "bullets", "items": ["Feature 1", "Feature 2", "Feature 3"]}
                ],
                [
                    {"type": "bullets", "items": ["Advanced feature 1", "Advanced feature 2"]}
                ],
                [
                    {"type": "image", "path": "product_a.png", "style": {"max_width": "1.5in", "wrap_text": "square"}}
                ]
            ],
            [
                "Product B",
                "Simple text description",  # Plain text still works
                [
                    {"type": "bullets", "items": ["Basic feature", "Standard quality"]}
                ],
                "No image"
            ]
        ]
    }
}
```

**Supported Rich Content Types in Cells:**
- **Text blocks** with styling (bold, italic, color, alignment)
- **Images** with sizing constraints and text wrapping
- **Bullet lists** with custom styling
- **Headings** (levels 1-6) for cell structure
- **Mixed content** - combine multiple block types in one cell

**Backward Compatibility:** All existing plain text cells continue to work exactly as before.

### Images
```python
{
    "type": "image",
    "path": "path/to/image.jpg",
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

#### Text Wrapping Modes
- `"inline"`: Image flows with text (default behavior)
- `"square"`: Text wraps around rectangular boundary
- `"tight"`: Text follows image contours more closely
- `"through"`: Text flows through image areas
- `"top_and_bottom"`: Image between paragraphs, no side text
- `"behind"`: Image behind text (background effect)
- `"in_front"`: Image in front of text (overlay effect)

#### Positioning Options
- `horizontal_align`: "left", "center", "right"
- `vertical_align`: "top", "middle", "bottom"
- `distance_from_text`: Spacing around image (e.g., "0.1in", "10px")

#### Text Wrapping Examples

```python
# Inline wrapping (default) - image flows with text
{"type": "image", "path": "icon.png", "style": {"wrap_text": "inline"}}

# Square wrapping - text flows around rectangular boundary
{"type": "image", "path": "photo.jpg", "style": {"wrap_text": "square", "horizontal_align": "left"}}

# Tight wrapping - text follows image contours
{"type": "image", "path": "logo.png", "style": {"wrap_text": "tight", "horizontal_align": "right"}}

# Top and bottom - image between paragraphs
{"type": "image", "path": "banner.png", "style": {"wrap_text": "top_and_bottom", "horizontal_align": "center"}}

# Behind text - image as background
{"type": "image", "path": "watermark.png", "style": {"wrap_text": "behind", "horizontal_align": "center"}}

# In front of text - image overlays text
{"type": "image", "path": "stamp.png", "style": {"wrap_text": "in_front"}}

# Combined example with positioning and distance
{
    "type": "image",
    "path": "company_logo.png",
    "style": {
        "max_width": "2.5in",
        "wrap_text": "square",
        "horizontal_align": "right",
        "vertical_align": "top",
        "distance_from_text": "0.15in"
    }
}
```

### Page Breaks
```python
{
    "type": "page_break"
}
```

### Headers
```python
{
    "type": "header",
    "apply_to": "all",  # "all", "all_except_first", "first", "odd", "even"
    "content": [
        {
            "type": "text",
            "text": "Company Name\tDocument Title\tPage {{page}}",
            "style": {"align": "center", "font_color": "666666"}
        },
        {
            "type": "table",
            "content": {
                "headers": ["Company", "Document"],
                "rows": [["ACME Corp", "Annual Report"]]
            }
        }
    ]
}
```

### Footers
```python
{
    "type": "footer",
    "apply_to": "all_except_first",  # Perfect for cover pages
    "content": [
        {
            "type": "text",
            "text": "© 2024 Company. All rights reserved.",
            "style": {"align": "center", "italic": True}
        }
    ]
}
```

#### Advanced Header/Footer Examples

**Header with Image and Text Wrapping:**
```python
{
    "type": "header",
    "apply_to": "all",
    "content": [
        {
            "type": "image",
            "path": "logo.png",
            "style": {
                "max_width": "1.5in",
                "wrap_text": "square",
                "horizontal_align": "right"
            }
        },
        {
            "type": "text",
            "text": "Company Report",
            "style": {"align": "left", "bold": True}
        }
    ]
}
```

**Footer with Table and Styling:**
```python
{
    "type": "footer",
    "apply_to": "all_except_first",
    "content": [
        {
            "type": "table",
            "content": {
                "headers": ["Company", "Document", "Date"],
                "rows": [["ACME Corp", "Annual Report", "2024"]]
            },
            "style": {
                "column_widths": [0.3, 0.4, 0.3],
                "header_styles": {"bold": True, "font_color": "666666"}
            }
        }
    ]
}
```

**Page-Specific Headers:**
```python
# Special header for first page only
{
    "type": "header",
    "apply_to": "first", 
    "content": [
        {
            "type": "text",
            "text": "CONFIDENTIAL REPORT",
            "style": {"align": "center", "bold": True}
        }
    ]
}

# Different headers for odd/even pages (useful for books)
{
    "type": "header",
    "apply_to": "odd",
    "content": [
        {
            "type": "text", 
            "text": "Chapter Title\t\tPage {{page}}",
            "style": {"align": "left"}
        }
    ]
}

{
    "type": "header",
    "apply_to": "even",
    "content": [
        {
            "type": "text",
            "text": "Page {{page}}\t\tBook Title", 
            "style": {"align": "right"}
        }
    ]
}
```

**Cover Page Example:**
```python
blocks = [
    {
        "type": "header",
        "apply_to": "all_except_first",
        "content": [
            {
                "type": "text",
                "text": "Company Report\tConfidential\tPage {{page}}",
                "style": {"align": "center"}
            }
        ]
    },
    # Page 1: Clean cover page (no header/footer)
    {"type": "heading", "text": "ANNUAL REPORT 2024", "level": 1, "style": {"align": "center"}},
    {"type": "page_break"},
    # Page 2+: Content with headers/footers
    {"type": "heading", "text": "Executive Summary", "level": 1}
]
```

## Styling Options

### Text Styling
- `bold`: Boolean for bold text
- `italic`: Boolean for italic text
- `font_color`: Hex color string (e.g., "FF0000" for red)
- `align`: Text alignment ("left", "center", "right", "justify")
- `style`: Word paragraph style name (e.g., "Normal", "Heading 1")

### Alignment Options
All block types support four alignment options:
- `"left"`: Align text to the left margin (default)
- `"center"`: Center text between margins
- `"right"`: Align text to the right margin  
- `"justify"`: Align text to both left and right margins by adjusting word spacing

Alignment works consistently across:
- Text blocks (including multi-line text with `\n`)
- Headings (all levels 1-6)
- Bullet lists
- Table headers
- Table columns (applied to all cells in the column)
- Table rows (applied to all cells in the row)
- Individual table cells (highest priority)

**Alignment Priority in Tables**: Cell styles override row styles, which override column styles, which override header styles.

### Table Styling
- `column_widths`: List of width fractions (e.g., [0.3, 0.7])
- `header_styles`: Dictionary of header styling
- `column_styles`: Dictionary of column styling by index
- `row_styles`: Dictionary of row styling by index
- `cell_styles`: Dictionary of cell styling by (row, col) tuple
- `bg_color`: Background color as hex string

### Image Styling
- `max_width`: Maximum width constraint (e.g., "4in", "300px")
- `max_height`: Maximum height constraint (e.g., "4in", "300px")

### Header and Footer Options
- `apply_to`: Controls which pages display the header/footer
  - `"all"`: Apply to all pages (default)
  - `"all_except_first"`: Apply to all pages except the first (perfect for cover pages)
  - `"first"`: Apply only to the first page
  - `"odd"`: Apply to odd-numbered pages (enables odd/even headers)
  - `"even"`: Apply to even-numbered pages (enables odd/even headers)
- `content`: List of block dictionaries that can include any supported block type

## Text and Paragraph Rules

- **Consecutive text blocks** without `\n` are grouped inline by default (in the same paragraph).
- **Every `\n`** in a text block always starts a new paragraph.
- **Every `\n\n`** in a text block creates a new paragraph with a blank paragraph in between.
- **Every `\n\n\n`** creates a new paragraph with two blank paragraphs in between.
- After a new paragraph (from `\n`), the next inline block starts a new paragraph group.
- Table cells and headers behave the same way as text blocks: every `\n` creates a new paragraph, and consecutive cell blocks without `\n` are grouped inline.
- `spacing` parameter adds extra blank paragraphs after that block.

## Style Inheritance and Overrides

- All colors must be passed as hex strings (e.g. "FF0000").
- If `style` is set, it overrides the default Word paragraph style.
- Run-level styles affect specific text runs (e.g., bold, italic, font color).
- Paragraph-level styles affect alignment and global paragraph formatting.
- `bg_color` uses low-level XML manipulation on table cells.
- `max_width` and `max_height` must be valid Word measurement strings (e.g. "4in", "300px"); they are converted internally.
- For missing or empty content, fallback styles are applied from `DEFAULT_EMPTY_VALUE_STYLE` and `DEFAULT_EMPTY_VALUE_TEXT` in `constants.py`.
- All alignment is handled by the global `set_paragraph_alignment` utility for consistency.
- Table styling supports per-header, per-column, per-row, and per-cell overrides, as well as custom column and row sizing.

This guide will evolve as more style capabilities are added (e.g., underline, font size, line spacing).

For additional questions or suggestions, please open a GitHub issue or discussion.