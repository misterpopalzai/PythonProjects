# 	Write a program to 
# prompt the user for hours  
# prompt the user for rate per hour using input 
# compute gross pay. 
# Pay the hourly rate for the hours up to 40 
# 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours 
# rate of 10.50 per hour 
# (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.

hrs= input("Enter Hours")
#print( int(hrs))
rate = input("Enter Rate:")
#print(float(rate))
h = float(hrs)
r = float(rate)
#print(r, h)

if h <=40:
    #print('Less than 40')
    grosspay = r * h
elif h > 40: 
    #print("Greater than 40")
    grosspay = (r*1.5)*(h-40) + (r*40)

print(float(grosspay))