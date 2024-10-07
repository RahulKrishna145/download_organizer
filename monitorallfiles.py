import os
import shutil
import time
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from watchdog.observers import Observer

# Initialize global variables
#classifytype = input("Enter the file extension to classify: ")
#newdirname = input("Enter the new directory name: ")
directory = "C:/Users/rahul/Downloads"
filetype = {}
destinationdir=""

# Create the new directory if it doesn't exist

class MyEventHandler(FileSystemEventHandler):
    def on_created(self, event: FileCreatedEvent) -> None:
        if not event.is_directory:
            file = event.src_path.split('.')
            if len(file) ==2:
                if file[-1] !="crdownload":
                    classifytype = file[-1]
                    sourcefile = event.src_path
                
                    # Add a small delay to ensure the file is fully written
                    time.sleep(1)
                    try:
                        if classifytype in filetype:
                            destinationdir = os.path.join(directory, filetype[classifytype])
                        else:
                            newdirname = input("Enter the new directory name: ")
                            newdirpath = os.path.join(directory, newdirname)
                            destinationdir = newdirpath
                            os.mkdir(newdirpath)
                            filetype[classifytype] = newdirname

                        destinationfile = os.path.join(destinationdir, os.path.basename(sourcefile))
                        
                        # Check if the destination file already exists
                            
                        shutil.move(sourcefile, destinationdir)
                        print(f"Moved file: {sourcefile} to {destinationdir}")
                    except FileNotFoundError:
                        print("file not found")
                    except Exception as e:
                        print()

def main():
    event_handler = MyEventHandler()
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
