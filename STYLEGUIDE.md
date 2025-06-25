# 🧶 docxblocks Style Guide

This document defines the supported styling options for each block type in the docxblocks system. It also documents how styles are applied, normalized, and rendered.

## 🎨 Shared Style Schema

All blocks that render text support a common style dictionary. This allows for consistent formatting across paragraphs, headings, bullet lists, tables, and more.

## ✅ Supported Style Keys

| Key | Type | Description | Applies To | Applied On |
|-----|------|-------------|------------|------------|
| `bold` | `bool` | Renders text in bold | Text, Heading, Bullet, Table Cell | Run |
| `italic` | `bool` | Renders text in italics | Text, Heading, Bullet, Table Cell | Run |
| `font_color` | `str` | Hex color code (e.g. "FF0000") | Text, Heading, Bullet, Table Cell | Run (font color) |
| `align` | `str` | Paragraph alignment (left, center, right) | Text, Heading, Bullet | Paragraph |
| `style` | `str` | Word paragraph style name (e.g. "Heading 1") | Text, Heading, Bullet | Paragraph |
| `bg_color` | `str` | Table cell background color in hex | Table headers, Table cells | Cell XML |
| `max_width` | `str` | Maximum image width (e.g. "4in", "300px") | Image | Image size |
| `max_height` | `str` | Maximum image height (e.g. "3in", "200px") | Image | Image size |

## 📐 Alignment Options

| Value | Meaning |
|-------|---------|
| `left` | Left-align paragraph |
| `center` | Center-align paragraph |
| `right` | Right-align paragraph |

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
  "type": "image",
  "path": "images/chart.png",
  "style": {
    "max_width": "4in",
    "max_height": "3in"
  }
}
```

## 🛠 Notes

- All colors must be passed as hex strings (e.g. "FF0000")
- If `style` is set, it overrides the default Word paragraph style
- Run-level styles affect specific text runs (e.g., bold, italic, font color)
- Paragraph-level styles affect alignment and global paragraph formatting
- `bg_color` uses low-level XML manipulation on table cells
- max_width and max_height must be valid Word measurement strings (e.g. "4in", "300px"); they are converted internally
- For missing or empty content, fallback styles are applied from `DEFAULT_EMPTY_VALUE_STYLE`

This guide will evolve as more style capabilities are added (e.g., underline, font size, line spacing).

For additional questions or suggestions, please open a GitHub issue or discussion.