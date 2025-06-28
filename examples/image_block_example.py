"""
Image Block Example

This example demonstrates image block functionality including:
- Basic image insertion
- Image resizing (downscaling and upscaling)
- Placeholder handling for missing images
- Different size constraints
- Text wrapping modes and positioning
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
        
        # Additional images for text wrapping examples
        square_image = os.path.join(temp_dir, "square_image.png")
        create_test_image(square_image, 200, 200, 'purple')
        
        rect_image = os.path.join(temp_dir, "rect_image.png")
        create_test_image(rect_image, 300, 150, 'orange')
        
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
            
            # Text Wrapping Examples
            {
                "type": "heading",
                "text": "Text Wrapping Examples",
                "level": 1
            },
            {
                "type": "text",
                "text": "The following examples demonstrate different text wrapping modes:",
            },
            
            # Example 5: Square wrapping
            {
                "type": "heading",
                "text": "Square Text Wrapping",
                "level": 2
            },
            {
                "type": "text",
                "text": "Square wrapping creates a rectangular boundary around the image, and text flows around this boundary. This is useful for creating clean, structured layouts where you want text to flow around the image in a predictable way. ",
            },
            {
                "type": "image",
                "path": square_image,
                "style": {
                    "max_width": "2in",
                    "wrap_text": "square",
                    "horizontal_align": "left"
                }
            },
            {
                "type": "text",
                "text": "With square wrapping, the text flows around a rectangular boundary that encompasses the entire image. This creates a clean, structured appearance where the text maintains consistent margins around the image. The text will wrap around the image on all sides, creating a professional layout that's easy to read and visually appealing.",
            },
            
            # Example 6: Tight wrapping
            {
                "type": "heading",
                "text": "Tight Text Wrapping",
                "level": 2
            },
            {
                "type": "text",
                "text": "Tight wrapping follows the actual shape of the image more closely, allowing text to flow around the image's contours. This is particularly effective with images that have transparent backgrounds or irregular shapes. ",
            },
            {
                "type": "image",
                "path": rect_image,
                "style": {
                    "max_width": "2.5in",
                    "wrap_text": "tight",
                    "horizontal_align": "right"
                }
            },
            {
                "type": "text",
                "text": "Tight wrapping creates a more organic flow around the image, following its actual boundaries rather than a rectangular box. This can create more interesting and dynamic layouts, especially when combined with proper positioning. The text flows more naturally around the image's actual shape.",
            },
            
            # Example 7: Top and bottom wrapping
            {
                "type": "heading",
                "text": "Top and Bottom Wrapping",
                "level": 2
            },
            {
                "type": "text",
                "text": "Top and bottom wrapping places the image between paragraphs, with no text flowing to the sides. This is useful for creating clear visual breaks in the content.",
            },
            {
                "type": "image",
                "path": large_image,
                "style": {
                    "max_width": "3in",
                    "wrap_text": "top_and_bottom",
                    "horizontal_align": "center"
                }
            },
            {
                "type": "text",
                "text": "This wrapping mode is perfect for images that serve as visual dividers or when you want to ensure the image gets full attention without competing text on the sides. It creates a clean, focused presentation of the image.",
            },
            
            # Example 8: Distance from text
            {
                "type": "heading",
                "text": "Distance from Text",
                "level": 2
            },
            {
                "type": "text",
                "text": "You can control the distance between the image and the surrounding text using the distance_from_text property. This creates breathing room around the image.",
            },
            {
                "type": "image",
                "path": square_image,
                "style": {
                    "max_width": "1.5in",
                    "wrap_text": "square",
                    "horizontal_align": "left",
                    "distance_from_text": "0.2in"
                }
            },
            {
                "type": "text",
                "text": "Notice the increased spacing around this image. The distance_from_text property adds margin space between the image and the surrounding text, creating a more comfortable reading experience. This is especially useful for images that need visual separation from the text content.",
            },
            
            # Summary
            {
                "type": "heading",
                "text": "Summary",
                "level": 2
            },
            {
                "type": "text",
                "text": "Summary:\n\n• Small images can be upscaled to meet size constraints\n• Large images are scaled down to fit within constraints\n• Images that fit within constraints are left unchanged\n• Missing images show placeholder text\n• Aspect ratio is always preserved\n\nText Wrapping Options:\n• inline: Image flows with text (default)\n• square: Text wraps around rectangular boundary\n• tight: Text follows image contours\n• through: Text flows through image areas\n• top_and_bottom: Image between paragraphs\n• behind: Image behind text\n• in_front: Image in front of text\n\nAdditional positioning options:\n• horizontal_align: left, center, right\n• vertical_align: top, middle, bottom\n• distance_from_text: Controls spacing around image",
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
    print("- Square text wrapping with left alignment")
    print("- Tight text wrapping with right alignment")
    print("- Top and bottom wrapping with center alignment")
    print("- Distance from text control")
    print("- Professional document layouts with proper image-text interaction")

if __name__ == "__main__":
    main() 