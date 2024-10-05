import tkinter as tk
from tkinter import filedialog

# Initialize global variables
folder_path = ""
newdirname = ""
file_extension = ""

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        label_folder.config(text=f"Selected Folder: {folder_path}")

def get_newdir_value():
    global newdirname
    newdirname = newdir.get()
    print(f"New directory name: {newdirname}")

def get_filebox_value():
    global file_extension
    file_extension = filebox.get()
    print(f"File extension: {file_extension}")

def show_frame(frame):
    frame.tkraise()

# Create the main window
root = tk.Tk()
root.title("Folder Selector")
root.geometry("400x400")

# Create a container frame to hold all other frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Create frames for each page
frame1 = tk.Frame(container)
frame2 = tk.Frame(container)
frame3 = tk.Frame(container)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Frame 1: Select Folder
label_folder = tk.Label(frame1, text="Select a folder", font=("Helvetica", 12))
label_folder.pack(pady=10)

button_folder = tk.Button(frame1, text="Select Folder", font=("Helvetica", 12), command=select_folder)
button_folder.pack(pady=10)

button_next1 = tk.Button(frame1, text="Next", font=("Helvetica", 12), command=lambda: show_frame(frame2))
button_next1.pack(pady=10)

# Frame 2: Name New Directory
label_newdir = tk.Label(frame2, text="New directory name:", font=("Helvetica", 12))
label_newdir.pack(pady=10)

newdir = tk.Entry(frame2, font=("Helvetica", 12), bg="lightgray")
newdir.pack(pady=10)

button_create = tk.Button(frame2, text="Create", font=("Helvetica", 12), command=get_newdir_value)
button_create.pack(pady=10)

button_next2 = tk.Button(frame2, text="Next", font=("Helvetica", 12), command=lambda: show_frame(frame3))
button_next2.pack(pady=10)

button_back2 = tk.Button(frame2, text="Back", font=("Helvetica", 12), command=lambda: show_frame(frame1))
button_back2.pack(pady=10)

# Frame 3: Enter File Type
label_filebox = tk.Label(frame3, text="Enter file extension:", font=("Helvetica", 12))
label_filebox.pack(pady=10)

filebox = tk.Entry(frame3, font=("Helvetica", 12), bg="lightgray")
filebox.pack(pady=10)

button_classify = tk.Button(frame3, text="Classify", font=("Helvetica", 12), command=get_filebox_value)
button_classify.pack(pady=10)

button_back3 = tk.Button(frame3, text="Back", font=("Helvetica", 12), command=lambda: show_frame(frame2))
button_back3.pack(pady=10)

# Show the first frame
show_frame(frame1)

# Run the application
root.mainloop()