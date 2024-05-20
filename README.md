# bin2ASCII_converter
The python script reads a hex/binary files and transforms into the relevant ASCII code and outputs in a CSV file. 
Input Format: Binary file data: PayloadHeader + Sequence Number + Message. 
Output format CSV file: PayloadHeader, Sequence Number, Message.


## Pre-requisits:
 - Install [python](https://www.python.org/downloads/) 3.9. Just FYI this project was built on python v3.9.10
 - Setup the working virtual environment to run the scripts as depicted in the section below.
 - See the below system requirements in order to run this script.
    - Processor: 1 Core 1.7 Ghz or better
    - Memory : 2 GB
    - Disk:  1 GB Free disk space minimum
    - System Type: 64 bit operating system preferred

## Create a virtual env to run this application
 1. Virtual environment provides a "light weight environment", each with their independent set of python packages installed in their local directories. More on venvs here(https://docs.python.org/3/library/venv.html).
 1. Create a `venv` to run this application so that it may not ammend your current `python3` environments.
 ```
  python3 -m venv /path/to/new/virtual/environment
 ```
 > Hint: You can just replace `/path/to/new/virtual/environment` with `env` and python will create a local env in your current directory.
 1. Activate the `venv` you just created (`<venv>` must be replaced by the path of the directory containing the virtual environment):
 ```
  source <venv>/bin/activate
 ```
 1. Insatll the dependencies with the command below

 ```
  pip install -r requirements.txt
 ```

 ## .env
 Create a `.env` file in this same directory where this `README.md` file is placed. Add the following environment variables into the file as they are needed to run the script.
 > Note: Please replace values e-g, secrets appropriately before running the script.
 ```
    LOG_LEVEL="DEBUG"
    DATA_FOLDER_LOCATION="src/data"
    INPUT_DIRECTORY_PATH="src/data/input"
    OUTPUT_DIRECTORY_PATH="src/data/output"
    FAILED_OUTPUT_DIRECTORY_PATH="src/data/failed"
    INPUT_FILE_EXTENSION=".bin"
    OUTPUT_FILE_EXTENSION=".csv"
    CHUNK_SIZE=4
 ```

 ## How to run the script
 Once all the pre-requisits above are satisfied. Run the command below to execute the scripts.
 > Note: Adjust the path to the main.py depending on your current working directory on terminal.

 Run back-end:
 ```
 python  src/backend/main.py
 ```

 ## How to run the Unit Tests
 Run the command below to execute the unit test scripts for the relevant files.
 > Note: Adjust the path to the <test_files>.py depending on your current working directory on terminal.

 Run tests:
 ```
 python  src/backend/Test_file_handler.py
 ```
 This should display results in the console as below.
 ```
   $ python src/backend/Test_file_handler.py 
   ......
   ----------------------------------------------------------------------
   Ran 6 tests in 0.004s

   OK
 ```

 ## Dockerised container for running as a crone job
 This script can run in a dockerised container on cloud and also could be scheduled to run at an internal via the crone jobs. The `Dockerfile` file provided along this repository could be used as is to spin up a container in any docker supported environments.