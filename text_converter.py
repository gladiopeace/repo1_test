def convert_to_custom_format(text):
    """
    Converts the sanitized text into the custom format.
    """
    lines = text.split('\n')
    custom_text = '\n'.join([f'  - "{line}"' for line in lines])
    return custom_text
