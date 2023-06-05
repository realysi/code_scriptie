import os
import glob
import shutil
import sys

def move(source_directory: str, agouti_or_deepsqueak: str, name: str):
    """
    Moves the files from the agouti opened zip to the data under a specified name
    """
    current_directory = os.getcwd()
    if agouti_or_deepsqueak != 'agouti' and agouti_or_deepsqueak != 'deepsqueak':
        raise Exception("the argument agouti_or_deepsqueak should either be: agouti or deepsqueak.")
    destination_directory = f"{current_directory}/data/{agouti_or_deepsqueak}/{name}"
    os.makedirs(destination_directory, exist_ok=True)
    files = glob.glob(f'{source_directory}/*')
    if len(files) == 0:
        raise Exception("This directory is either empty or couldn't be opened.\nTry moving the folder away from the downloads folder.")
    for file in files:
        file_destination = file.replace(source_directory, destination_directory)
        shutil.copyfile(file, file_destination)
    return destination_directory

"""
def move(source_directory: str, agouti_or_deepsqueak, name: str):

    current_directory = os.getcwd()
    destination_directory = f"{current_directory}/data/{agouti_or_deepsqueak}/{name}"
    
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory, exist_ok=True)
    else:
        raise Exception("Destination directory already exists.")
    
    files = glob.glob(f'{source_directory}/*')
    
    if len(files) == 0:
        raise Exception("This directory is either empty or couldn't be opened.\nTry moving the folder away from the downloads folder.")
    
    for file in files:
        file_name = os.path.basename(file)
        file_destination = os.path.join(destination_directory, file_name)
        shutil.copy(file, file_destination)
    
    return destination_directory
"""