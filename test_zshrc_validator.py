import unittest
import subprocess
from pathlib import Path
import os

# Create a test case class inheriting from unittest.TestCase
class TestZshrcValidatorMethods(unittest.TestCase):

    # Test method for calling the script with a valid .*rc file.
    def test_valid_rc_file(self):
        # Create a temp .*rc file
        file_path = 'temp_rc_file'
        with open(file_path, 'w') as f:
            f.write('This is a temp file.')

        response = subprocess.check_output(['python3', 'zshrc_validator.py', file_path]).decode()
        self.assertTrue('Passed file' in response)

        # Clean up the tmp file
        os.remove(file_path)

    # Test method for calling the script with a non-existent file.
    def test_non_existent_rc_file(self):
        response = subprocess.check_output(['python3', 'zshrc_validator.py', 'non_existent_file']).decode()
        self.assertTrue('Error: The file non_existent_file does not exist.' in response)

    # Test method for calling the script without any arguments.
    def test_no_arguments(self):
        try:
            response = subprocess.check_output(['python3', 'zshrc_validator.py'])
        except subprocess.CalledProcessError as e:
            response = e.output.decode()
        self.assertTrue('usage: zshrc_validator.py [-h] [-c] rc_file_path' in response)

# Run the tests
unittest.main()
