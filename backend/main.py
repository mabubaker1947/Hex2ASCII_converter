import os
from decouple import config


# retrieve environment variables from .env file
INPUT_DIRECTORY_PATH=config("INPUT_DIRECTORY_PATH")
INPUT_FILE=config("INPUT_FILE")
OUTPUT_DIRECTORY_PATH=config("OUTPUT_DIRECTORY_PATH")
OUTPUT_FILE=config("OUTPUT_FILE")
# chunk size for the bytes to read for int32=4 bytes
CHUNK_SIZE=int(config("CHUNK_SIZE"))


def main():
    '''
    Invokes binary to ASCII converter functionality
    '''
    try:
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


def extract_byte_data(file) -> int:
    '''
    Extracts byte data from the file against given chunk size.
    Retruns an integer value
    '''
    chunk_binary = file.read(CHUNK_SIZE)
    if not chunk_binary:
        return None
    print("Chunk binary:\t"+ str(chunk_binary))

    # try converting the chunk data to integers
    chunk_integer_value=convert_byte_to_int32(chunk_binary)
    print("Payload header value: \t"+str(chunk_integer_value))
    return chunk_integer_value


def convert_byte_to_int32(binary_data) -> int:
    '''
    Converts binary data to an integer value.
    Retruns an integer value if convertible otherwise None
    '''
    converted_integer_value = None
    try:
        # convert byte value to an integer with little endian format
        converted_integer_value=int.from_bytes(binary_data, byteorder='little')
    except:
        print("NOT an int32 convertible byte data")
    return converted_integer_value


if __name__=="__main__":
    main()

    # TODO:
    # add support to export in multiple files extensions
    # add logging capabilities
    # add unit tests