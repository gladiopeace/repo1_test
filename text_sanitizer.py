import re

def sanitize_input(text):
    """
    Sanitizes the input text by removing any harmful or unwanted characters.
    """
    sanitized_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return sanitized_text
