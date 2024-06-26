# cleans ./tmp/logs/, ./tmp/retrieved_data folders.
from config import LOG_PATH, RETRIVED_DATA_STORAGE_PATH
import glob
import os


def remove_files(pattern):
    try:
        # Find files matching the pattern
        files = glob.glob(pattern)

        for file in files:
            os.remove(file)
            print(f"File '{file}' deleted successfully.")

        if not files:
            print(f"No files found matching the pattern '{pattern}'.")
    except Exception as e:
        print(f"An error occurred while deleting files: {e}")


def remove_directory(path):
    try:
        os.rmdir(path)
        print(f"Directory: {path} deleted.")
    except:
        print(f"No directories with such {path} found")


LOGS = f"{LOG_PATH}/*.log"
RETRIEVED_DATA = f"{RETRIVED_DATA_STORAGE_PATH}/*.json"
remove_files(LOGS)
remove_files(RETRIEVED_DATA)
