import os
from decouple import config
from file_handler import process_binary_files_data



def main():
    '''
    Entry point to the software. Invokes binary to ASCII converter functionality
    '''
    try:
        process_binary_files_data()
    except Exception as e:
        print(e)



if __name__=="__main__":
    main()

    # TODO:
    # add support to export in multiple files extensions
    # add logging capabilities
    # add unit tests