# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2025-01-27

### Fixed
- **Inline Text After New Paragraph**: Fixed a bug where a text block following a block with `"new_paragraph": True` would incorrectly start a new paragraph. Now, inline text after a new paragraph block is correctly added to the same paragraph, as expected.
- Added a test to ensure this behavior remains correct.

---

## [1.2.0] - 2025-01-27

### Added
- **Page Break Blocks**: New `page_break` block type for creating multi-page documents
  - Simple `{"type": "page_break"}` syntax
  - Creates proper Word page breaks using `WD_BREAK.PAGE`
  - Works seamlessly with all other block types
  - Perfect for reports, manuals, and multi-page documents

### Technical Improvements
- **PageBreakBuilder**: New builder class for handling page break blocks
- **Enhanced RichTextBuilder**: Added support for page break validation and rendering
- **Comprehensive Testing**: Added test suite for page break functionality including inline text integration

### Documentation
- Updated README with page break examples and documentation
- Added new example script (`page_break_example.py`) demonstrating multi-page document creation
- Updated block type table to include `page_break` type

---

## [1.1.0] - 2025-06-25

### Added
- **Inline Text by Default**: Text blocks now stay on the same line by default
  - Consecutive text blocks are automatically inline (no new paragraphs)
  - Use `"new_paragraph": true` to force a new paragraph when needed
  - Perfect for building complex text with mixed styling (e.g., "Name: **John** (ID: `12345`)")
  - Maintains backward compatibility with existing code
- **Image Resizing Tests**: Comprehensive tests for image resizing (inches and pixels) and placeholder behavior are now integrated into the main image test file.

### Technical Improvements
- **Enhanced TextBuilder**: Added support for inline text runs within paragraphs
- **Smart Paragraph Management**: Automatic paragraph creation and management for inline text
- **RichTextBuilder Coordination**: Improved coordination between different block types
- **Comprehensive Testing**: All image-related tests (including resizing and placeholder) are now in `tests/test_image_block.py` for clarity

### Documentation
- **README Improvements**:
  - Fixed the Style Guide link (now `[Style Guide](STYLEGUIDE.md)`)
  - Added a new section on creating Word templates, including the crucial rule that each placeholder must be in its own paragraph, with correct/incorrect examples and step-by-step instructions
  - Clarified inline text behavior and updated block type documentation
- Added new example script (`inline_text_example.py`) demonstrating inline text features
- Updated block type table to include optional `new_paragraph` field

### Quality
- All tests pass, including new and integrated image tests, inline text, and template handling

---

## [1.0.5] - 2025-06-25

### Fixed
- **Integer Values in Table Cells**: Fixed `.strip()` AttributeError when using integer values in table cells
  - Convert values to strings before calling `.strip()` to handle non-string types
  - Fixes both header and cell value processing in TableBuilder
  - Maintains backward compatibility with existing string values
  - Added comprehensive test coverage for integer values in tables

### Technical Improvements
- **Robust Type Handling**: Enhanced table cell processing to handle mixed data types
- **Test Coverage**: Added `test_table_block_with_integers()` to verify fix works correctly
- **Error Prevention**: Eliminates AttributeError when integer values are used in table data

---

## [1.0.4] - 2025-06-25

### Fixed
- **Integer Values in Table Cells**: Fixed `.strip()` AttributeError when using integer values in table cells
  - Convert values to strings before calling `.strip()` to handle non-string types
  - Fixes both header and cell value processing in TableBuilder
  - Maintains backward compatibility with existing string values
  - Added comprehensive test coverage for integer values in tables

### Technical Improvements
- **Robust Type Handling**: Enhanced table cell processing to handle mixed data types
- **Test Coverage**: Added `test_table_block_with_integers()` to verify fix works correctly
- **Error Prevention**: Eliminates AttributeError when integer values are used in table data

---

## [1.0.3] - 2025-06-25

### Fixed
- Updated tests to support new bullet point implementation (Word-native bullet formatting)
- Ensured all tests pass for v1.0.2+ bullet improvements

---

## [1.0.2] - 2025-06-25

### Fixed
- **Bullet Point Reliability**: Completely rewrote bullet point implementation to use Word's native bullet formatting
  - Replaced manual bullet character insertion with proper Word bullet styles
  - Added multi-layer fallback system for maximum compatibility
  - No longer requires users to add custom styles to their Word templates
  - Works consistently across different Word versions and environments

### Technical Improvements
- **Robust Bullet Builder**: Implemented three-tier fallback strategy:
  1. Primary: Uses Word's built-in "List Bullet" style
  2. Fallback: Creates custom bullet style programmatically with proper indentation
  3. Final: Manual bullet character insertion if all else fails
- **Self-Contained Library**: Eliminated dependency on external Word template styles
- **Cross-Platform Compatibility**: Enhanced reliability across different Word environments

---

## [1.0.0] - 2025-06-25

### Added
- **Core Block System**: Implemented modular block-based architecture for Word document generation
  - `TextBlock`: Multi-line text with styling support
  - `HeadingBlock`: Headings with configurable levels (1-6)
  - `BulletBlock`: Bullet point lists with custom styling
  - `TableBlock`: Advanced tables with headers, rows, and comprehensive styling
  - `ImageBlock`: Image insertion with automatic sizing and DPI calculation

- **Comprehensive Styling System**:
  - Text styling: bold, italic, font color, alignment
  - Table styling: header styles, column styles, row styles, cell-specific styles
  - Column and row width customization
  - Background colors and font colors for tables
  - Image size constraints (max_width, max_height)

- **Robust Error Handling**:
  - Consistent placeholder system for missing/empty values
  - Graceful fallback for invalid image paths
  - Pydantic validation for all block types
  - Empty value handling with "VALUE NOT FOUND" placeholders

- **Developer Experience**:
  - Complete test suite with pytest
  - GitHub Actions CI/CD pipeline
  - Development setup script (`./scripts/setup_dev.sh`)
  - Comprehensive examples for all block types
  - Detailed documentation and style guide

- **Documentation**:
  - Complete README with installation, usage, and development instructions
  - Comprehensive style guide with all supported options
  - Example scripts demonstrating all features
  - API documentation and best practices

### Technical Features
- **Modular Architecture**: Separate builders for each block type
- **Pydantic Validation**: Type-safe block definitions and validation
- **Global Utilities**: Shared styling and alignment functions
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Python Compatibility**: Supports Python 3.9, 3.10, and 3.11

### Dependencies
- python-docx >= 0.8.11
- Pillow >= 10.0.0
- pydantic >= 2.0.0

---

## [Unreleased]

### Planned
- Additional block types (charts, page breaks, etc.)
- More styling options (underline, strikethrough, etc.)
- Template inheritance and composition
- Performance optimizations for large documents 