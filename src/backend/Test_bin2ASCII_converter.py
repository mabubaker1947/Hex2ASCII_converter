import unittest
from bin2ASCII_converter import extract_byte_data, convert_byte_to_int32


class TestMigration(unittest.TestCase):


    def test_extract_byte_data(self):
        # arrange
        expected_payload_header_value=27
        input_file_path="src/data/input/logi.bin"
        with open(input_file_path,'rb') as binary_file:
            # act
            actual_extracted_data=extract_byte_data(binary_file)
            #assert
            self.assertIsNotNone(actual_extracted_data)
            self.assertEqual(expected_payload_header_value, actual_extracted_data)

    def test_convert_byte_to_int32(self):
        # arrange
        binary_data=b'\x1b\x00\x00\x00'
        expected_payload_header_value=27
        # act
        actual_data=convert_byte_to_int32(binary_data)
        #assert
        self.assertIsNotNone(actual_data)
        self.assertEqual(expected_payload_header_value, actual_data)


if __name__=='__main__':
	unittest.main()