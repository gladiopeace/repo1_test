import sys
from file_handler import FileHandler
from text_sanitizer import sanitize_input
from text_converter import convert_to_custom_format

def main(input_file_path):
    # Check if the file path ends with .txt
    if not input_file_path.endswith('.txt'):
        print("Please provide a valid .txt file path.")
        return

    # Read the text file
    text = FileHandler.read_file(input_file_path)

    # Sanitize the input
    sanitized_text = sanitize_input(text)

    # Convert to custom format
    custom_text = convert_to_custom_format(sanitized_text)

    # Generate output filename
    output_file_path = input_file_path[:-4] + '.yaml'  # Removes .txt and appends .yaml

    # Write to the new file
    FileHandler.write_file(output_file_path, custom_text)

    print(f"Output saved to: {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py input.txt")
    else:
        main(sys.argv[1])
