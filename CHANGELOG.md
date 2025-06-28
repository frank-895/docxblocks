# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.6.5] - 2025-06-28

### Fixed
- **Rollback to stable functionality**: Reverted problematic text wrapping implementation that was causing Word document corruption
- **Restored clean image handling**: Removed complex XML manipulation that was causing file corruption issues
- **Stable document generation**: All generated .docx files now open correctly in Microsoft Word without corruption

### Removed
- **Text wrapping functionality**: Removed `wrap_text`, `horizontal_align`, `vertical_align`, and `distance_from_text` properties
- **Complex XML manipulation**: Removed error-prone inline-to-floating image conversion code
- **Problematic features**: Removed features that were causing Word to report file corruption

### Technical
- **Clean codebase**: Back to stable v1.6.1 functionality with only `max_width` and `max_height` for images
- **All tests passing**: 57/57 tests passing with clean, reliable functionality
- **Backward compatibility**: All existing functionality preserved (text, tables, headers/footers, rich cells, etc.)

**Note**: This version provides a stable, reliable base. Text wrapping functionality may be re-implemented in future versions using a more robust approach.

---

## [1.6.1] - 2024-06-27
### Fixed
- Robust and predictable styling for rich content in table cells. Cell/row/column/table styles are now merged correctly with block styles, preventing unwanted bold/italic/color bleed.

---

## [1.6.0] - 2025-06-27
### Added
- **Rich Content in Table Cells**: Table cells now support rich content including text, images, bullets, and headings
  - Table cells can contain either plain text (string) or rich content (list of block dictionaries)
  - **Supported Content Types**: Text blocks with styling, images with sizing constraints, bullet lists, headings (levels 1-6)
  - **Mixed Content**: Combine multiple block types in a single cell for complex layouts
  - **Backward Compatibility**: All existing plain text cells continue to work exactly as before
  - **Seamless Integration**: Rich content uses the same block system and styling as main document content

### Enhanced
- **TableBuilder**: Extended to detect and handle rich content in cells automatically
  - Automatically detects whether a cell contains plain text or rich content
  - Renders rich content using the existing RichTextBuilder for consistency
  - Maintains all existing table styling and formatting capabilities
  - Preserves table cell behavior (newlines, inline grouping) for rich content

### Technical Improvements
- **Content Detection**: Smart detection of cell content type without breaking existing functionality
- **RichTextBuilder Integration**: Reuses existing rich content rendering system for consistency
- **Comprehensive Testing**: Added tests for rich content in cells including text, images, bullets, headings, and mixed content
- **Example Documentation**: Updated table example to demonstrate rich content capabilities

### Documentation
- **Updated README**: Added comprehensive section on rich content in table cells with examples
- **Updated STYLEGUIDE**: Added documentation for rich content in table cells
- **Example Enhancement**: Updated table example to showcase rich content features

---

## [1.5.1] - 2025-06-27
### Fixed
- **Images in Headers and Footers**: Fixed critical issue where images would not display in headers and footers
  - Images now properly embed and display in both headers and footers using direct header/footer methods
  - Replaced problematic `parent.insert()` approach with direct `header.add_paragraph()` and `footer.add_paragraph()` methods
  - Fixed invalid `placeholder=None` parameter in `ImageBuilder.build()` calls that was causing silent failures
  - Images are now embedded using file objects to ensure proper embedding in headers/footers
  - Added comprehensive error handling and placeholder text for missing or invalid images

### Enhanced
- **HeaderFooterBuilder**: Completely refactored to handle images and other content directly using header/footer methods
  - Added direct support for text, images, headings, and other block types in headers/footers
  - Implemented proper styling support (alignment, bold, italic, font color) for header/footer content
  - Added image sizing and scaling support with `max_width` and `max_height` constraints
  - Enhanced error handling with graceful fallbacks for missing images or invalid content

### Technical Improvements
- **Image Embedding**: Updated `ImageBuilder` to use file objects for image embedding, ensuring compatibility with headers/footers
- **Parent Method Detection**: Added fallback logic to use parent's `add_paragraph()` method when available
- **Comprehensive Testing**: Added dedicated tests for images in headers and footers to prevent regression
- **Example Documentation**: Updated header/footer example to demonstrate image functionality

### Documentation
- **Updated Examples**: Added third example in `header_footer_example.py` demonstrating images in headers and footers
- **Test Coverage**: Added `test_header_with_image()` and `test_footer_with_image()` to ensure functionality remains working
- **Backward Compatibility**: All existing header/footer functionality preserved; only image display issue resolved

---

## [1.5.0] - 2025-06-26
### Added
- **Customizable Headers and Footers**: Complete header and footer system supporting all block types
  - New `header` and `footer` block types with configurable page application
  - Support for page-specific headers/footers: `"all"`, `"first"`, `"odd"`, `"even"`, `"all_except_first"`
  - **Cover Page Support**: New `"all_except_first"` option perfect for clean cover pages with headers/footers on content pages
  - Headers and footers can contain any combination of supported block types (text, tables, images, etc.)
  - Automatic handling of odd/even page settings and first page differentiation
  - Full integration with existing block validation and rendering system

### Enhanced
- **RichTextBuilder**: Extended to handle header and footer block validation and rendering
- **HeaderFooterBuilder**: New specialized builder for configuring document headers and footers
- **Schema System**: Added `HeaderBlock` and `FooterBlock` to the block type union with proper validation
- **Template Integration**: Headers and footers work seamlessly with existing template-based workflow

### Technical Improvements
- **Page Layout Control**: Automatic configuration of Word document section settings for different header/footer types
- **Content Reuse**: Headers and footers use the same rich content system as main document body
- **Error Handling**: Graceful handling of invalid header/footer configurations
- **Comprehensive Testing**: Added 10 comprehensive tests covering all header/footer scenarios including cover page functionality
- **Example Documentation**: Three complete examples demonstrating basic, advanced, and cover page header/footer usage

### Documentation
- **Updated README**: Added comprehensive headers and footers section with examples and cover page documentation
- **Block Type Table**: Updated to include new `header` and `footer` block types
- **Usage Examples**: Detailed examples showing page-specific headers, complex content, cover page layouts, and styling options

---

## [1.4.0] - 2025-06-26
### Added
- **Complete Justify Alignment Support**: Added full support for text justification across all block types
  - Added `"justify"` as a new alignment option alongside `"left"`, `"center"`, and `"right"`
  - Works with text blocks, headings, bullet lists, table headers, table columns, table rows, and individual table cells
  - Supports multi-line content alignment in both text blocks and table cells
  - Comprehensive alignment example (`examples/alignment_example.py`) demonstrating all scenarios

### Enhanced
- **Universal Alignment System**: Improved alignment functionality across the entire codebase
  - Fixed alignment support in table cell text processing to ensure consistent behavior
  - Enhanced text builder to properly handle alignment changes between text blocks
  - Improved newline processing to preserve alignment settings across paragraph breaks
  - All four alignment options now work consistently across every block type

### Technical Improvements
- **Enhanced Schema**: Updated `TextStyle` schema to include `"justify"` as a valid alignment option
- **Improved Text Processing**: Enhanced `process_text_with_newlines()` utility to apply alignment to all paragraphs
- **Smart Alignment Detection**: Text builder now detects alignment changes and creates new paragraphs when needed while preserving inline text grouping
- **Comprehensive Testing**: Added 9 comprehensive alignment tests covering all block types and scenarios
- **Backward Compatibility**: All existing functionality preserved; existing code continues to work unchanged

### Documentation
- **Updated Style Guide**: Enhanced documentation with complete justify alignment examples
- **Comprehensive Examples**: New alignment example showcasing all alignment options across all block types
- **Test Coverage**: Full test suite ensuring alignment works correctly in all scenarios including edge cases

---

## [1.3.7] - 2024-06-26
### Fixed
- **Leading Newlines Issue**: Fixed a bug where leading newlines (`\n\n` at the start of text) created extra blank paragraphs. Now `\n\n` consistently creates exactly 1 blank paragraph regardless of position (start, middle, or end).
- **Regex-Based Newline Processing**: Replaced naive `split('\n')` logic with proper regex parsing to handle consecutive newlines correctly.

### Removed
- **Deprecated Parameters**: Removed deprecated `spacing` parameter from `TextBlock` schema and all related logic.
- **Deprecated Tests**: Removed obsolete spacing functionality tests.

### Changed
- **Single Source of Truth**: `\n` is now the only way to create new paragraphs - clean, consistent, and intuitive.
- **Unified Logic**: All newline handling now follows the same pattern: n newlines = (n-1) blank paragraphs between content.

---

## [1.3.6] - 2024-06-26
### Changed
- Newline handling is now strictly:
  - Every single `\n` creates a new paragraph (no extra blank).
  - Double `\n\n` creates a blank paragraph.
  - Inline grouping is preserved unless a `\n` is present (separate text blocks are grouped inline).
- All tests updated and passing for this logic.

---

## [1.3.5] - 2024-06-26
### Changed
- Unified and corrected newline handling for both text blocks and table cells:
  - Every single `\n` starts a new paragraph (no extra blank).
  - Double or more newlines create the correct number of blank paragraphs.
  - Inline text grouping and styling are preserved.
- All tests updated to expect and verify this behavior.

---

## [1.3.4] - 2024-06-26

### Changed
- Major simplification of text block and newline handling:
  - Every `\n` starts a new paragraph
  - Consecutive text blocks without `\n` are grouped inline
  - Empty text gets placeholder text
- Removed complex state tracking from TextBuilder
- All tests, documentation, and examples updated to match new logic
- Improved maintainability and clarity throughout the codebase

## [1.3.3] - 2025-06-26

### Changed
- Finalized paragraph and inline grouping rules: consecutive text blocks are grouped inline by default, but any `\n` or `new_paragraph: True` always starts a new paragraph and resets grouping.
- After a new paragraph, the next inline block starts a new paragraph group.
- Table cells and headers behave the same way as text blocks.
- `spacing` parameter only applies to blocks with `new_paragraph: True`.

### Fixed
- All tests and documentation updated to match the final rules.

---

## [1.3.2] - 2025-06-26

### Added
- Generic newline handling: every `\n` creates a new paragraph everywhere (text blocks, inline text, table cells, table headers).
- `spacing` parameter is supported for text blocks, adding extra blank paragraphs after the block.

### Changed
- All text is now consistent inside and outside tables. No more grouping of inline text blocks; each block is its own paragraph.
- Table cells and headers treat every `\n` as a new paragraph, including empty ones for `\n\n`.

### Fixed
- All tests updated to match the new behavior.

---

## [1.3.1] - 2025-06-26

### Fixed
- **Block Order Preservation**: Blocks are now rendered in the exact order provided to `DocxBuilder.insert()`. The previous logic could result in blocks appearing out of order due to ambiguous validation; this is now resolved.
- **Validation Logic**: Block validation now uses the `type` field to select the correct schema, preventing accidental misclassification and ensuring robust, predictable rendering.
- **Test Suite Cleanup**: Tests are now logically grouped, redundant code and files have been removed, and the suite is easier to maintain and extend.

--- 

## [1.3.0] - 2025-06-26

### Added
- **Smart Newline Handling**: Text blocks now intelligently handle newline characters
  - Single `\n` characters remain as literal newlines (inline text)
  - Double `\n\n` creates a new paragraph with a blank line before it
  - Mixed usage of single and double newlines works seamlessly
  - Perfect for creating structured text with proper paragraph spacing
- **Table Cell Newline Support**: Table cells now support the same intelligent newline handling
  - `\n\n` in table headers creates new paragraphs with blank lines
  - `\n\n` in table data cells creates new paragraphs with blank lines
  - Single `\n` characters remain as literal newlines within cells
  - Works with all existing table styling options
- **Image Upscaling**: Images can now be scaled up to meet size constraints
  - Small images can be upscaled to meet `max_width` and/or `max_height` constraints
  - Large images are still scaled down as before
  - Aspect ratio is always preserved
  - Works with both single and dual dimension constraints
- **Shared Text Processing**: New utility module for consistent newline handling across block types
- **Comprehensive Testing**: Added test suite for newline functionality including edge cases
- **Example Documentation**: New example scripts demonstrating double newline features in text and tables

### Technical Improvements
- **Enhanced TextBuilder**: Added logic to detect and handle `\n\n` patterns
- **Enhanced TableBuilder**: Integrated shared text processing for consistent newline handling
- **Enhanced ImageBuilder**: Modified scaling logic to support upscaling of small images
- **Backward Compatibility**: All existing functionality remains unchanged
- **Documentation Updates**: Updated README with newline behavior documentation for both text and table blocks

---

## [1.2.2] - 2025-06-25

### Fixed
- **Inline Text After New Paragraph**: Fixed a bug where a text block following a block with `"new_paragraph": True` would incorrectly start a new paragraph. Now, inline text after a new paragraph block is correctly added to the same paragraph, as expected.
- Added comprehensive test coverage to ensure this behavior remains correct.
- Updated test expectations to match the correct inline text behavior.

---

## [1.2.1] - 2025-01-27

### Fixed
- **Inline Text After New Paragraph**: Fixed a bug where a text block following a block with `"new_paragraph": True` would incorrectly start a new paragraph. Now, inline text after a new paragraph block is correctly added to the same paragraph, as expected.
- Added a test to ensure this behavior remains correct.

---

## [1.2.0] - 2024-06-18

### Changed
- Major simplification of text block and newline handling:
  - Every `\n` starts a new paragraph
  - Consecutive text blocks without `\n` are grouped inline
  - Empty text gets placeholder text
- Removed complex state tracking from TextBuilder
- All tests, documentation, and examples updated to match new logic
- Improved maintainability and clarity throughout the codebase

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

## [Unreleased]

### Planned
- Additional block types (charts, page breaks, etc.)
- More styling options (underline, strikethrough, etc.)
- Template inheritance and composition
- Performance optimizations for large documents 