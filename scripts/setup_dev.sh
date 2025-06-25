#!/bin/bash

# Development setup script for docxblocks
echo "Setting up development environment for docxblocks..."

# Install the package in editable mode
echo "Installing docxblocks in editable mode..."
pip install -e .

# Run tests to ensure everything works
echo "Running tests..."
PYTHONPATH=. pytest tests -v

# Run examples
echo "Running examples..."
cd examples
python text_block_example.py
python table_block_example.py
python image_block_example.py
python combined_example.py
cd ..

echo "Development setup complete!"
echo ""
echo "To run tests: PYTHONPATH=. pytest tests"
echo "To run examples: cd examples && python <example_name>.py"
echo ""
echo "Note: Tests will run automatically on GitHub when you push or create PRs." 