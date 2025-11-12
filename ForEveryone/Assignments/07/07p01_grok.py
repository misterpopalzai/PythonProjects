#temporarily updating the CWD
import os
os.chdir(r"C:\Users\manso\Documents\PythonProjects\ForEveryone\Assignments\07")

fname = input("Enter file name: ")
try:
    fh = open(fname)
    for line in fh:
        print(line.strip().upper())  # Processes as per assignment
    fh.close()  # Good habit to close files
except FileNotFoundError:
    print(f"Error: File '{fname}' not found in current directory.")