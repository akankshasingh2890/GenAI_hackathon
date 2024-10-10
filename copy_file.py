import shutil
import os

def file_exists(file_path):
    """Checks if a file exist at given file_path."""
    return os.path.exists(file_path)

def copy_file():
    source_file = "path/to/source/file.txt"

    if file_exists(source_file):

        print(f"The file '{source_file}' exists. Start copying...")
        destination_folder = "path/to/destination/folder"
        print(f"destination folder is : {destination_folder}")
        shutil.copy(source_file, destination_folder)

    else
        print(f"The file '{source_file}' does not exist.")

