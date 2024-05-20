import unittest
from unittest.mock import patch, mock_open, MagicMock
from decouple import config

from file_handler import process_files_data, move_to_failed_files, process_binary_files_data

# retrieve environment variables from .env file
INPUT_DIRECTORY_PATH=config("INPUT_DIRECTORY_PATH")
OUTPUT_DIRECTORY_PATH=config("OUTPUT_DIRECTORY_PATH")
FAILED_OUTPUT_DIRECTORY_PATH=config("FAILED_OUTPUT_DIRECTORY_PATH")
OUTPUT_FILE_EXTENSION=config("OUTPUT_FILE_EXTENSION")
UNDERSCORE="_"
INPUT_FILE_EXTENSION=config("INPUT_FILE_EXTENSION")

# def process_binary_files_data(input_file_path, output_file_path):
#     # Dummy implementation for testing
#     pass

def extract_byte_data(binary_file):
    """Dummy implementation for testing purposes"""
    return binary_file.read(1)



class TestProcessFilesData(unittest.TestCase):
    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.walk")
    @patch("time.strftime")
    @patch("__main__.process_binary_files_data")
    def test_directory_does_not_exist(self, mock_process, mock_strftime, mock_walk, mock_exists, mock_isdir):
        #arrange
        mock_isdir.return_value = False
        mock_exists.return_value = False
        #act
        process_files_data()
        #assert
        mock_isdir.assert_called_once_with(INPUT_DIRECTORY_PATH)
        mock_walk.assert_not_called()
        mock_process.assert_not_called()

    def test_process_files_data_checksIfDirectoryExists_throwsException(self):
        #arrange
        imaginary_folder_path = "foo/bar"
        #act
        process_files_data()
        #assert
        self.assertRaises(Exception)

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.walk")
    @patch("time.strftime")
    @patch("__main__.process_binary_files_data")
    def test_no_files_to_process(self, mock_process, mock_strftime, mock_walk, mock_exists, mock_isdir):
        #arrange
        mock_isdir.return_value = True
        mock_exists.return_value = True
        mock_walk.return_value = [("folder", ["subfolder"], [])]
        #act
        process_files_data()
        #assert
        mock_isdir.assert_called_once_with(INPUT_DIRECTORY_PATH)
        mock_exists.assert_called_once_with(INPUT_DIRECTORY_PATH)
        mock_walk.assert_called_once_with(INPUT_DIRECTORY_PATH)
        mock_process.assert_not_called()

    @patch("os.path.isdir")
    @patch("os.path.exists")
    @patch("os.walk")
    @patch("time.strftime")
    @patch("__main__.process_binary_files_data")
    def test_process_bin_files(self, mock_process, mock_strftime, mock_walk, mock_exists, mock_isdir):
        #arrange
        mock_isdir.return_value = True
        mock_exists.return_value = True
        mock_walk.return_value = [("folder", ["subfolder"], ["file1.bin", "file2.txt"])]
        mock_strftime.return_value = "2024-05-20T12:00:00"
        #act
        process_files_data()
        #assert
        mock_isdir.assert_called_once_with(INPUT_DIRECTORY_PATH)
        mock_exists.assert_called_once_with(INPUT_DIRECTORY_PATH)
        mock_walk.assert_called_once_with(INPUT_DIRECTORY_PATH)

    @patch("builtins.open", new_callable=mock_open)
    @patch("shutil.move")
    @patch("__main__.extract_byte_data")
    def test_process_binary_files_data_whenSequenceNumberIsNone(self, mock_extract, mock_shutil, mock_open):
        # arrange
        # Set up the mock for reading binary data
        mock_in = mock_open(read_data=b'\x04\x01test').return_value
        mock_out = mock_open().return_value
        mock_open.side_effect = [mock_in, mock_out]
        mock_extract.side_effect = [b'\x04', None, None]  # Simulate reading bytes
        #act
        process_binary_files_data("input_file_path", "output_file_path")
        #assert
        mock_open.assert_any_call("input_file_path", 'rb')
        mock_open.assert_any_call("output_file_path", 'a')


    def test_move_to_failed_files_raises_exceptionWithInvalidFile(self):
        #arrange and act
        move_to_failed_files("input_file_path", "output_file_path")
        #act
        self.assertRaises(Exception)

if __name__ == "__main__":
    unittest.main()
