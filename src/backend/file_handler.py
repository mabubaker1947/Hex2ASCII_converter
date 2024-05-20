import os, time, shutil
from decouple import config
from bin2ASCII_converter import extract_byte_data
from shared_utility import logger

# retrieve environment variables from .env file
INPUT_DIRECTORY_PATH=config("INPUT_DIRECTORY_PATH")
OUTPUT_DIRECTORY_PATH=config("OUTPUT_DIRECTORY_PATH")
FAILED_OUTPUT_DIRECTORY_PATH=config("FAILED_OUTPUT_DIRECTORY_PATH")
OUTPUT_FILE_EXTENSION=config("OUTPUT_FILE_EXTENSION")
UNDERSCORE="_"
INPUT_FILE_EXTENSION=config("INPUT_FILE_EXTENSION")

def process_files_data():
    """Iterates through all the files in the folder and the sub folder
    """
    try:    
        if os.path.isdir(INPUT_DIRECTORY_PATH) and os.path.exists(INPUT_DIRECTORY_PATH):
            # iterate through folders and sub folders for input files
            for folder, subs, files in os.walk(INPUT_DIRECTORY_PATH):
                for file in files:
                    # only process .bin ext files for now. 
                    if file.endswith(INPUT_FILE_EXTENSION):
                        # generate a new timestamp for each file processed
                        CURRENT_TIMESTAMP=time.strftime("%Y-%m-%dT%H:%M:%S")

                        # suffix the processed file name with the timestamp for identification/validations
                        output_file = CURRENT_TIMESTAMP+UNDERSCORE+file.removesuffix(INPUT_FILE_EXTENSION)+OUTPUT_FILE_EXTENSION

                        # open two files. one for reading binary data and other for output
                        input_file_path=os.path.join(folder, file)
                        output_file_path=os.path.join(OUTPUT_DIRECTORY_PATH, output_file)
                        process_binary_files_data(input_file_path, output_file_path)
                        
    except Exception as e:
        logger.error(e)

def process_binary_files_data(input_file_path, output_file_path):
    """Processes the binary files data and efficiently writes to the output file.
    """
    try:
        with open(input_file_path,'rb') as binary_file, \
            open(output_file_path,'a') as output_file:

            # add header to the output file. e-g:- .csv file
            output_file.write(str("Payload Header" +", "+ "Sequence Number" +", "+ "Message")+"\n")

            while True:
                # NOTE: I could have created a data class here to hold these three properties 
                #       However, as I didn't know where this class be used so I kept it simple,
                #       by NOT creating the class to hold the data and simply exporting them to output file.

                # extract all data w.r.t given requirements of Payload header, sequence and message
                payload_header=extract_byte_data(binary_file)
                if payload_header is None: break
                sequence_number=extract_byte_data(binary_file)
                if sequence_number is None: break

                # try reading the message chunk now with the payload_header size value
                if payload_header:
                    message_chunk = binary_file.read(payload_header)
                    logger.debug(message_chunk)

                # finally print out one message at a time to the output file to avoid memory overhead
                message=(str(payload_header) +","+ str(sequence_number) +", \""+ str(message_chunk.decode())+" \"\n")
                output_file.write(message)
    except Exception as e:
        logger.error(e)
        move_to_failed_files(input_file_path, output_file_path)

def move_to_failed_files(input_file_path, output_file_path):
    """ Moves the files to the FAILED directory on error
    """
    try:
        logger.info(input_file_path+" File cannot be processed. Moving to FAILED files directory.")
        # remove the file from input directory to the failed directory
        os.rename(input_file_path, output_file_path)
        os.replace(input_file_path, output_file_path)
        shutil.move(input_file_path, output_file_path)
    except Exception as e:
        logger.error(input_file_path+" File cannot be Moved.\t"+str(e))