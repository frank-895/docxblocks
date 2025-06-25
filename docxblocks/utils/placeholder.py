def find_placeholder_paragraph(doc, placeholder):
    """
    Find a paragraph in the document that exactly matches a given placeholder string.

    Args:
        doc: A python-docx Document object.
        placeholder: A string like "{{main}}" to locate.

    Returns:
        The matching paragraph, or None if not found.
    """
    for paragraph in doc.paragraphs:
        if paragraph.text.strip() == placeholder:
            return paragraph
    return None
