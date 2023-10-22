import unittest
from textfileconverter import FileHandler, sanitize_input, convert_to_custom_format

class TestTextFileConverter(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler()
        self.test_file_path = 'test_file.txt'
        self.test_content = 'Hello\nWorld'
        self.sanitized_content = 'Hello\nWorld'
        self.custom_format_content = '  - "Hello"\n  - "World"'

    def test_read_file(self):
        with open(self.test_file_path, 'w') as f:
            f.write(self.test_content)
        content = self.file_handler.read_file(self.test_file_path)
        self.assertEqual(content, self.test_content)

    def test_read_file_non_existent(self):
        with self.assertRaises(Exception):
            self.file_handler.read_file('non_existent_file.txt')

    def test_write_file(self):
        self.file_handler.write_file(self.test_file_path, self.test_content)
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, self.test_content)

    def test_sanitize_input(self):
        sanitized_text = sanitize_input(self.test_content)
        self.assertEqual(sanitized_text, self.sanitized_content)

    def test_convert_to_custom_format(self):
        custom_text = convert_to_custom_format(self.sanitized_content)
        self.assertEqual(custom_text, self.custom_format_content)

    def tearDown(self):
        try:
            os.remove(self.test_file_path)
        except:
            pass

if __name__ == '__main__':
    unittest.main()
