import os
import glob
import shutil
import sys

def clear_folders(directory: str):
    """
    Removes the generated results.
    """
    try:
        current_directory = os.getcwd()
        desired_directory = f"{current_directory}/{directory}"
        folders = glob.glob(f'{desired_directory}/*')
        for folder in folders:
            shutil.rmtree(folder)
        """for folder in folders:
            files = glob.glob(f'{folder}/*')
            for file in files:
                os.remove(file)"""
    except PermissionError:
        print("permissionError: Your terminal/IDE does not have the permission to delete files. You can change this in the settings of your operating system")



def move_data(source_directory: str, agouti_or_deepsqueak, name: str):
    """
    Moves the files from the agouti opened zip to the data under a specified name
    """
    current_directory = os.getcwd()
    destination_directory = f"{current_directory}/data/{agouti_or_deepsqueak}/{name}"
    os.makedirs(destination_directory, exist_ok=True)
    files = glob.glob(f'{source_directory}/*')
    if len(files) == 0:
        raise Exception("This directory is either empty or couldn't be opened.\nTry moving the folder away from the downloads folder.")
    for file in files:
        file_destination = file.replace(source_directory, destination_directory)
        shutil.copyfile(file, file_destination)
    return destination_directory


def results_directories(name, interval_agouti, interval_deepsqueak, inverval_overlap):
    """
    Creates the directories for the results, where csv will be written into later on.
    """
    current_directory = os.getcwd()
    directory_path = f"{current_directory}/results/{inverval_overlap}_{interval_agouti}_{interval_deepsqueak}_{name}"
    paths = [directory_path, f"{directory_path}/agouti", f"{directory_path}/deepsqueak", f"{directory_path}/data"]
    for path in paths:
        os.makedirs(path, exist_ok=True)
    return directory_path

def info():
    message = """
File: main.py

flags: 
-rr to remove the results generated in previous runs
-rd to remove the data used in previous runs
-info te gain acces to this info screen.

Usage program:
1. Fill in the path of where the agouti and deepsqueak folders (unzipped) are stored (problems could arise if this folder is in the downloads folder).
2. Fill in location and name of your dataset.
3. Determine what intervals you want to use for the agouti, deepsqueak and overlap between those two observations.
4. Run the program by python3 main.py --flag if wanted.
"""
    print(message)

def flags():
    commands =['-rr', '-rd', '-info']
    if len(sys.argv) > 4:
        print("Wrong Usage: No more possbilities than to use two flags at the same time (-rr, -rd, -info)")
        raise SystemExit
    else:
        commands_given = sys.argv[1:]
        for i in commands_given:
            if '-' not in i:
                raise SystemExit(f"Wrong usage: Use -{i} instead of {i} to indicate usage of flag. For more info, see -info.")
            if i not in commands:
                raise SystemExit(f"There is no flag called {i}. See -info for more information about flag uses.")      
        for i in commands_given:
            if i == '-rr':
              clear_folders('results')
              raise SystemExit
            elif i == '-rd':
                clear_folders('data')
                raise SystemExit
            elif i == '-info':
                info() 
                raise SystemExit


"""
original_string = "Hello, world!"
replacement = "universe"
new_string = original_string.replace("world", replacement)
print(new_string)


source_directory = '/path/to/source_directory'  # Replace with the actual source directory path
destination_directory = '/path/to/destination_directory'  # Replace with the actual destination directory path
file_name = 'example_file.txt'  # Replace with the actual file name

# Construct the source and destination file paths
source_file_path = os.path.join(source_directory, file_name)
destination_file_path = os.path.join(destination_directory, file_name)

# Move the file
shutil.move(source_file_path, destination_file_path)
"""