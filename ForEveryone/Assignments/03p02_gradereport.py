# 3.3 Write a program to 
# prompt for a score between 0.0 and 1.0. 
# If the score is out of range, 
# print an error. 
# If the score is between 0.0 and 1.0, 
# print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, 
# print a suitable error message and exit. 
# For the test, enter a score of 0.85.

#adding import sys to top of code so that if input is out of range, code exits
import sys
score = input("Enter Score: ")
s_in = float(score)

if s_in < 0.0 or s_in > 1.0: 
    print("Error, score is outside 0.0 and 1.0")
    sys.exit()
elif s_in >= 0.0 and s_in <= 1.0:
    if s_in < 0.6:
        print("F")
    if s_in >= 0.6 and s_in <0.7:
        print("D")
    if s_in >= 0.7 and s_in <0.8: 
        print("C")
    if s_in >= 0.8 and s_in <0.9: 
        print("B")
    if s_in >= 0.9 and s_in <= 1.0: 
        print("A")