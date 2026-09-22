import os

def get_current_working_directory():
    """Returns the current working directory."""
    return os.getcwd()

def list_files_in_directory(directory):
    """Returns a list of files in the specified directory."""
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return f"Directory '{directory}' not found."
    except PermissionError:
        return f"Permission denied to access '{directory}'."

#call the function to get current working directory
current_directory = get_current_working_directory()
print(f"Current Working Directory: {current_directory}")

#call the function to list files in current working directory
files_in_directory = list_files_in_directory(current_directory)
print(f"\n Files in Directory: {files_in_directory}")

import sys
print(sys.version) #printing the python version
print(sys.argv)