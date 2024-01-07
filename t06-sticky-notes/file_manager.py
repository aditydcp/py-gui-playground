import os

directory = "notes/"

def _create_file():
    with open('notes/note 1.txt', 'w+') as f:
        f.write("New text file")

def create_file(filename, content):
    try:
        with open(directory + filename + ".txt", 'w+') as f:
            f.write(content)
    except:
        print("Error saving")

def read_file(filename):
    with open(directory + filename + ".txt", "r") as f:
        return f.readlines()

def delete_file(filename):
    os.remove(directory + filename + ".txt")

def scan_files():
    files = os.listdir(directory)
    print(files)
    notes = []
    for file in files:
        if file.split(".")[-1] == "txt":
            notes.append(file)
    return notes

def set_directory(dir_path):
    global directory
    print(dir_path)
    directory = dir_path + "\\"