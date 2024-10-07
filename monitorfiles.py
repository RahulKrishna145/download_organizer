import os
import shutil
import time
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from watchdog.observers import Observer

# Initialize global variables
newdirname = input("Enter the new directory name: ")
classifytype = input("Enter the file extension to classify: ")
directory = "C:/Users/rahul/Downloads"
filetype = {}

# Create the new directory if it doesn't exist
newdirpath = os.path.join(directory, newdirname)
if not os.path.exists(newdirpath):
    try:
        os.mkdir(newdirpath)
        print(f"Directory '{newdirpath}' created.")
    except PermissionError:
        print(f"Permission denied to create '{newdirpath}'.")
    except Exception as e:
        print(f"Error creating directory '{newdirpath}': {e}")

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, newdirpath, classifytype):
        self.newdirpath = newdirpath
        self.classifytype = classifytype

    def on_created(self, event: FileCreatedEvent) -> None:
        if not event.is_directory:
            file = event.src_path.split('.')
            if len(file) > 1 and file[-1] == self.classifytype:
                sourcefile = event.src_path
                destinationdir = self.newdirpath
                # Add a small delay to ensure the file is fully written
                time.sleep(1)
                try:
                    if self.classifytype in filetype:
                        destinationdir = os.path.join(directory, filetype[self.classifytype])
                    else:
                        filetype[self.classifytype] = newdirname

                    destinationfile = os.path.join(destinationdir, os.path.basename(sourcefile))
                    
                    # Check if the destination file already exists
                    if os.path.exists(destinationfile):
                        base, extension = os.path.splitext(destinationfile)
                        counter = 1
                        new_destinationfile = f"{base}_{counter}{extension}"
                        while os.path.exists(new_destinationfile):
                            counter += 1
                            new_destinationfile = f"{base}_{counter}{extension}"
                        destinationfile = new_destinationfile

                    shutil.move(sourcefile, destinationfile)
                    print(f"Moved file: {sourcefile} to {destinationfile}")
                except FileNotFoundError:
                    print(f"File not found: {sourcefile}")
                except Exception as e:
                    print(f"Error moving file: {e}")

def main():
    event_handler = MyEventHandler(newdirpath, classifytype)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()