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

### Images
```python
{
    "type": "image",
    "path": "path/to/image.jpg",
    "style": {
        "max_width": "4in",
        "max_height": "300px"
    }
}
```

### Page Breaks
```python
{
    "type": "page_break"
}
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