from file_handler import FileHandler
from text_sanitizer import sanitize_input
from text_converter import convert_to_custom_format

def main():
    # Read the text file
    file_path = 'input.txt'
    text = FileHandler.read_file(file_path)

    # Sanitize the input
    sanitized_text = sanitize_input(text)

    # Convert to custom format
    custom_text = convert_to_custom_format(sanitized_text)

    # Write to a new file
    output_file_path = 'output.txt'
    FileHandler.write_file(output_file_path, custom_text)

if __name__ == "__main__":
    main()
