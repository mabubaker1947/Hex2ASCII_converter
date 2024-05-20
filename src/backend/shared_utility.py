from decouple import config
import logging,os

DATA_FOLDER_LOCATION =config('DATA_FOLDER_LOCATION')
LOG_LEVEL=config("LOG_LEVEL", default="INFO")


# setup migration tool output folder paths
logPath = DATA_FOLDER_LOCATION+ os.sep + "logs" + os.sep
os.makedirs(logPath, exist_ok=True)

# setup logger
logFormat = "%(asctime)s|%(levelname)s|%(message)s"
logging.basicConfig(
    filename=logPath + "bin2ASCII_converter.log", level=LOG_LEVEL, format=logFormat
)
logger = logging.getLogger()