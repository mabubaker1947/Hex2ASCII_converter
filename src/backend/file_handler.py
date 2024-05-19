
import os
from decouple import config
from bin2ASCII_converter import extract_byte_data


INPUT_DIRECTORY_PATH=config("INPUT_DIRECTORY_PATH")
INPUT_FILE=config("INPUT_FILE")
OUTPUT_DIRECTORY_PATH=config("OUTPUT_DIRECTORY_PATH")
OUTPUT_FILE=config("OUTPUT_FILE")


def process_binary_files_data():
    try:
        if os.path.exists(INPUT_DIRECTORY_PATH):
            print("pathe exists")
            
        
        # open two files. one for reading binary data and other for output
        with open(os.path.join(INPUT_DIRECTORY_PATH, INPUT_FILE),'rb') as binary_file, \
            open(os.path.join(OUTPUT_DIRECTORY_PATH, OUTPUT_FILE),'w') as output_file:

            # add header to the output file
            output_file.write(str("Payload Header" +","+ "Sequence Number" +","+ "Message")+"\n")

            while True:
                # extract all data w.r.t given requirements of Payload header, sequence and message
                payload_header=extract_byte_data(binary_file)
                if payload_header is None: break
                sequence_number=extract_byte_data(binary_file)
                if sequence_number is None: break

                # try reading the message chunk now with the payload_header size value
                if payload_header:
                    message_chunk = binary_file.read(payload_header)
                    print(message_chunk)

                # finally print out one message at a time to the output file to avoid overhead on memory
                message=(str(payload_header) +","+ str(sequence_number) +", \""+ str(message_chunk.decode())+" \"\n")
                output_file.write(message)

    except Exception as e:
        print(e)