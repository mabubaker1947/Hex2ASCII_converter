

import os
from decouple import config


# chunk size for the bytes to read for int32=4 bytes
CHUNK_SIZE=int(config("CHUNK_SIZE"))


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

