# docxblocks

🧱 High-level, block-based abstraction for `python-docx`.

## 🚀 Why docxblocks?

Unlike templating libraries like `docxtpl`, `docxblocks` keeps **all logic in Python**, not in `.docx` files. Build dynamic Word reports from structured block objects inside your codebase.

## ✨ Key Features

- Block types: `text`, `heading`, `table`, `bullets`, `image`
- Style control via consistent `style` dictionaries
- Graceful fallback for missing data
- Declarative, testable, version-controlled
- No logic inside Word templates

## 📦 Installation

```bash
pip install docxblocks
```

📘 **See the [Style Guide](STYLE_GUIDE.md)** for all supported style keys, color formats, and alignment options.

## 🧱 Block-Based API (Core Concept)

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

Block types:

| Type      | Required Keys     |
|-----------|-------------------|
| `text`    | `text`            | 
| `heading` | `text`, `level`   |
| `table`   | `content`         | 
| `image`   | `path`            |
| `bullets` | `items` (list)    |

## 🧪 Example

```python
from docxblocks import DocxBuilder

builder = DocxBuilder("template.docx")
builder.insert("{{main}}", [
    {"type": "heading", "text": "Summary", "level": 2},
    {"type": "text", "text": "This report provides status."},
    {
        "type": "table",
        "content": {
            "headers": ["Service", "Status"],
            "rows": [["API", "OK"], ["DB", "OK"]]
        },
        "style": {
            "header_styles": {"bold": True, "bg_color": "f2f2f2"},
            "column_widths": [0.5, 0.5]
        }
    },
    {"type": "image", "path": "chart.png", "style": {"max_width": "4in"}}
])
builder.save("output.docx")
```

## 🛠️ Philosophy

> Keep the logic in your code — not in your Word template.

- Fully programmatic document generation
- No fragile embedded logic (`{{ if x }}`) in `.docx`
- Declarative, JSON-like format ideal for automation and templating
- Built for dynamic, testable, repeatable reports

## 🧪 Development

### Setup

```bash
# Clone the repository
git clone https://github.com/frank-895/docxblocks.git
cd docxblocks

# Run the development setup script
./scripts/setup_dev.sh
```

### Testing

```bash
# Run all tests
PYTHONPATH=. pytest tests

# Run tests with verbose output
PYTHONPATH=. pytest tests -v

# Run specific test file
PYTHONPATH=. pytest tests/test_text_block.py
```

### Examples

```bash
# Run individual examples
cd examples
python text_block_example.py
python table_block_example.py
python image_block_example.py
python combined_example.py
```

### Continuous Integration

GitHub Actions automatically runs tests on:
- Every push to `main` and `develop` branches
- Every pull request to `main`
- Multiple Python versions (3.9, 3.10, 3.11)

**Note:** Tests run automatically in CI, so you can push your changes and see the results on GitHub.

## 📄 License
MIT - [LICENSE](LICENSE) 