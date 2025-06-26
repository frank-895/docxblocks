# 🧶 docxblocks Style Guide

This document defines the supported styling options for each block type in the docxblocks system. It also documents how styles are applied, normalized, and rendered.

## 🎨 Shared Style Schema

All blocks that render text support a common style dictionary. This allows for consistent formatting across paragraphs, headings, bullet lists, tables, and more.

## ✅ Supported Style Keys

| Key           | Type    | Description                                      | Applies To                        | Applied On         |
|---------------|---------|--------------------------------------------------|-----------------------------------|--------------------|
| `bold`        | `bool`  | Renders text in bold                             | Text, Heading, Bullet, Table Cell | Run                |
| `italic`      | `bool`  | Renders text in italics                          | Text, Heading, Bullet, Table Cell | Run                |
| `font_color`  | `str`   | Hex color code (e.g. "FF0000")                   | Text, Heading, Bullet, Table Cell | Run (font color)   |
| `align`       | `str`   | Paragraph alignment (left, center, right)         | Text, Heading, Bullet, Table Cell | Paragraph          |
| `style`       | `str`   | Word paragraph style name (e.g. "Heading 1")      | Text, Heading, Bullet             | Paragraph          |
| `bg_color`    | `str`   | Table cell background color in hex                | Table headers, Table cells        | Cell XML           |
| `max_width`   | `str`   | Maximum image width (e.g. "4in", "300px")         | Image                             | Image size         |
| `max_height`  | `str`   | Maximum image height (e.g. "3in", "200px")        | Image                             | Image size         |

### Table-Specific Style Keys

| Key            | Type         | Description                                      | Applies To         |
|----------------|--------------|--------------------------------------------------|--------------------|
| `header_styles`| `dict`       | Styles for all header cells                      | Table              |
| `column_styles`| `dict`       | Styles for columns by index                      | Table              |
| `row_styles`   | `dict`       | Styles for rows by index                         | Table              |
| `cell_styles`  | `dict`       | Styles for specific cells by (row, col) tuple    | Table              |
| `column_widths`| `list[float]`| Width fractions for columns (sum ≤ 1.0)          | Table              |
| `row_widths`   | `list[float]`| Height fractions for rows (inches, EMUs)         | Table              |

## 📐 Alignment Options

- All alignment is set using the global utility `set_paragraph_alignment` from `docxblocks/utils/styles.py`.
- This ensures consistent alignment for all block types (text, heading, bullet, table cell, etc.).

| Value   | Meaning                |
|---------|------------------------|
| `left`  | Left-align paragraph   |
| `center`| Center-align paragraph |
| `right` | Right-align paragraph  |

## 📦 Example Style Usage

```python
{
  "type": "text",
  "text": "Summary of findings",
  "style": {
    "bold": true,
    "font_color": "444444",
    "align": "center",
    "style": "Normal"
  }
}

{
  "type": "table",
  "content": {
    "headers": ["Name", "Age", "City"],
    "rows": [
      ["Alice", "30", "London"],
      ["Bob", "25", "Paris"]
    ]
  },
  "style": {
    "header_styles": {"bold": True, "bg_color": "E0E0E0"},
    "column_styles": {0: {"bold": True}},
    "row_styles": {1: {"bg_color": "FFF8DC"}},
    "cell_styles": {(1, 2): {"font_color": "FF0000"}},
    "column_widths": [0.4, 0.3, 0.3],
    "row_widths": [0.5, 0.4, 0.4]
  }
}

{
  "type": "image",
  "path": "images/chart.png",
  "style": {
    "max_width": "4in",
    "max_height": "3in"
  }
}
```

## 🛠 Notes

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

## Paragraph and Inline Text Rules

- Consecutive text blocks are grouped inline by default (in the same paragraph).
- Any `\n` in a text block always starts a new paragraph (splits the text into multiple paragraphs).
- `new_paragraph: True` always starts a new paragraph (and resets inline grouping).
- After a new paragraph (from either `\n` or `new_paragraph: True`), the next inline block starts a new paragraph group.
- Table cells and headers behave the same way as text blocks: every `\n` creates a new paragraph, and consecutive cell blocks are grouped inline unless `\n` or `new_paragraph: True` is used.
- `spacing` parameter only applies to blocks with `new_paragraph: True` (adds extra blank paragraphs after that block). For inline text, spacing is ignored.