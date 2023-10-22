import os
import codecs

class FileHandler:
    @staticmethod
    def read_file(file_path):
        """
        Reads the contents of a given text file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        with codecs.open(file_path, 'r', 'utf-8') as file:
            contents = file.read()
        return contents

    @staticmethod
    def write_file(file_path, content):
        """
        Writes the given content to a specified file.
        """
        with codecs.open(file_path, 'w', 'utf-8') as file:
            file.write(content)
