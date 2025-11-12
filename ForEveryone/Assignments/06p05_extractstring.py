#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
startpos = text.find("0")
count = 0
#print(startpos)
for lastpos in text:
        count = count + 1

lastpos = count
#print(count)

extract = text[startpos : lastpos]
print(float(extract))
