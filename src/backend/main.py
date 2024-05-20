import os, time
from decouple import config
from file_handler import process_files_data
from shared_utility import logger


def main():
    '''
    Entry point to the software.\n Invokes file handing and the binary to ASCII converter functionality.
    '''
    try:
        logger.info("Processing binary files started.")
        process_files_data()
    except Exception as e:
        logger.info(e)

if __name__=="__main__":
    start_time = time.time()
    main()
    logger.info("Total execution time in seconds \t:  "+str(time.time() -start_time))