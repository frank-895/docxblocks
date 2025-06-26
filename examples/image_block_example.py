"""
Image Block Example

This example demonstrates image block functionality including:
- Basic image insertion
- Image resizing (downscaling and upscaling)
- Placeholder handling for missing images
- Different size constraints
"""

from docx import Document
from docxblocks import DocxBuilder
from PIL import Image
import tempfile
import os

def create_test_image(path, width, height, color='red'):
    """Create a test image with specified dimensions"""
    img = Image.new('RGB', (width, height), color=color)
    img.save(path, dpi=(96, 96))
    return path

def main():
    # Create a simple template
    doc = Document()
    doc.add_paragraph("{{main}}")
    doc.save("image_block_template.docx")
    
    # Create temporary test images
    with tempfile.TemporaryDirectory() as temp_dir:
        # Small image (1x1 inch at 96 DPI) - will be upscaled
        small_image = os.path.join(temp_dir, "small_image.png")
        create_test_image(small_image, 96, 96, 'red')
        
        # Large image (8x6 inch at 96 DPI) - will be downscaled
        large_image = os.path.join(temp_dir, "large_image.png")
        create_test_image(large_image, 768, 576, 'blue')
        
        # Medium image (4x3 inch at 96 DPI) - will stay the same
        medium_image = os.path.join(temp_dir, "medium_image.png")
        create_test_image(medium_image, 384, 288, 'green')
        
        blocks = [
            {
                "type": "heading",
                "text": "Image Block Examples",
                "level": 1
            },
            {
                "type": "text",
                "text": "This document demonstrates various image sizing scenarios:",
            },
            
            # Example 1: Upscaling small image
            {
                "type": "heading",
                "text": "Upscaling Small Image",
                "level": 2
            },
            {
                "type": "text",
                "text": "Original: 1x1 inch → Scaled to: 3x3 inches",
            },
            {
                "type": "image",
                "path": small_image,
                "style": {"max_width": "3in"}
            },
            
            # Example 2: Downscaling large image
            {
                "type": "heading",
                "text": "Downscaling Large Image",
                "level": 2
            },
            {
                "type": "text",
                "text": "Original: 8x6 inch → Scaled to: 4x3 inches",
            },
            {
                "type": "image",
                "path": large_image,
                "style": {
                    "max_width": "4in",
                    "max_height": "3in"
                }
            },
            
            # Example 3: No scaling needed
            {
                "type": "heading",
                "text": "No Scaling Required",
                "level": 2
            },
            {
                "type": "text",
                "text": "Original: 4x3 inch → No change needed",
            },
            {
                "type": "image",
                "path": medium_image,
                "style": {
                    "max_width": "5in",
                    "max_height": "4in"
                }
            },
            
            # Example 4: Missing image (placeholder)
            {
                "type": "heading",
                "text": "Missing Image (Placeholder)",
                "level": 2
            },
            {
                "type": "text",
                "text": "This demonstrates graceful handling of missing images:",
            },
            {
                "type": "image",
                "path": "nonexistent_image.png",
                "style": {
                    "max_width": "3in",
                    "max_height": "2in"
                }
            },
            
            # Summary
            {
                "type": "text",
                "text": "Summary:\n\n• Small images can be upscaled to meet size constraints\n• Large images are scaled down to fit within constraints\n• Images that fit within constraints are left unchanged\n• Missing images show placeholder text\n• Aspect ratio is always preserved",
            },
        ]
        
        # Build the document
        builder = DocxBuilder("image_block_template.docx")
        builder.insert("{{main}}", blocks)
        builder.save("image_block_output.docx")
    
    print("Image block example completed!")
    print("Check 'image_block_output.docx' to see the result.")
    print("\nFeatures demonstrated:")
    print("- Image upscaling (small images scaled up)")
    print("- Image downscaling (large images scaled down)")
    print("- No scaling when not needed")
    print("- Placeholder handling for missing images")
    print("- Aspect ratio preservation")

if __name__ == "__main__":
    main() 