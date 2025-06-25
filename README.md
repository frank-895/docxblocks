# docxblocks

🧱 High-level, block-based abstraction for `python-docx`.

## 🚀 Why docxblocks?

Unlike templating libraries like `docxtpl`, `docxblocks` keeps **all logic in Python**, not in `.docx` files. Build dynamic Word reports from JSON-style blocks.

## ✨ Features

- Block types: `text`, `heading`, `table`, `bullets`, `image`
- Style control via simple `style` dictionaries
- Graceful fallback for missing data
- Programmatic, testable, version-controlled

## 📦 Installation

```bash
pip install docxblocks
```

## 🧪 Example

```python
from docxblocks import DocxBuilder

builder = DocxBuilder("template.docx")
builder.insert("{{main}}", [
    {"type": "heading", "text": "Summary", "level": 2},
    {"type": "text", "text": "This report shows insights."}
])
builder.save("output.docx")
```

## 📄 License
MIT - [LICENSE](LICENSE) 