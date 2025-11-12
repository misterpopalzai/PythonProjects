#7.1 Write a program that prompts for a file name, 
# then opens that file and 
# reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

#temporarily updating the CWD
import os
os.chdir(r"C:\Users\manso\Documents\PythonProjects\ForEveryone\Assignments\07")

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)

    #read through the file
    #inp = fh.read()
    for line in fh:
        print(line.strip().upper())
    #print file contents
    #print in uppercase
    #print(len(inp))
    #line = line.rstrip()
        #print(line.rstrip)

except ValueError:
    print("File not found in directory")