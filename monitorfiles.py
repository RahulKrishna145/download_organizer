import os
import shutil
import interface

# Ensure the variables are set in interface.py
try:
    directory = interface.folder_path
    classifytype = interface.file_extension
    newdirname = interface.newdirname
except AttributeError as e:
    print(f"Error: {e}")
    exit(1)

# Ensure directory and newdirname are not empty
monitorlog = {}

if not directory or not newdirname:
    print("Directory or new directory name is not set.")
    exit(1)



# Create the new directory if it doesn't exist
if classifytype in monitorlog:
    newdirname = monitorlog[classifytype]
    newdirpath = os.path.join(directory, newdirname)
    

else:
    monitorlog[classifytype] = newdirname
    newdirpath = os.path.join(directory, newdirname)
    try:
        os.mkdir(newdirpath)
    except FileExistsError:
        print(f"The directory '{newdirpath}' already exists.")
    except PermissionError:
        print(f"Permission denied to create '{newdirpath}'.")
        exit(1)




# List all files and directories in the specified directory
try:
    files = os.listdir(directory)
    for item in files:
        if os.path.isfile(os.path.join(directory, item)):
            file = item.split('.')
            if len(file) > 1 and file[1] == classifytype:
                sourcefile = os.path.join(directory, item)
                destinationdir = newdirpath
                shutil.move(sourcefile, destinationdir)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")