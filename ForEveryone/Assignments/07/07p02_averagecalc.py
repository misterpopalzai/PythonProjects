#7.2 Write a program that prompts for a file name,
# then opens that file  
# reads through the file, 
# looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines an
#compute the average of those values 
#produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

#temporarily updating the CWD
import os
os.chdir(r"C:\Users\manso\Documents\PythonProjects\ForEveryone\Assignments\07")
linecount = 0
excount = 0

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        else:
            text = line
            startpos = text.find("0")
            count = 0
                #print(startpos)
            for lastpos in text:
                        count = count + 1

            lastpos = count
                #print(count)

            extract = text[startpos : lastpos]
            xn = (float(extract))
            #print(xn)
            excount = float(excount) + xn
            linecount = linecount + 1
            

        #print(line)
except ValueError:
        print("File not found")
#print(exsum, linecount)
print("Average spam confidence:", float(excount) / linecount)
#print("Done")