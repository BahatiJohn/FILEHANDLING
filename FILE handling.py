# File Handling Assignment: file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("12345\n")
            file.write("Python is awesome!\n")
        print("File 'my_file.txt' created successfully.")
    except IOError:
        print("Error creating the file.")

def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nFile Contents:\n" + content)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending new line 1\n")
            file.write("Appending new line 2\n")
            file.write("Appending new line 3\n")
        print("\nFile 'my_file.txt' updated with additional lines.")
    except PermissionError:
        print("Permission denied. Cannot append to the file.")

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()