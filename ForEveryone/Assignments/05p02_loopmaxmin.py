#5.2 Write a program that 
# repeatedly prompts a user for integer numbers 
# until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number 
#   catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
    userin = input("Enter a number: ")
    
    # Check if it num be converted to number
    try:
        num = float(userin)
        #if yes then....
        #Capture value using smallest and largest variable
        #print(f"{userin} is integer or float number")

            #largest number test
        if largest is None:
            largest = num
        elif num > largest:
             largest = num
                    
            #smallest number test
        if smallest is None:
            smallest = num
        elif num < smallest:
             smallest = num

    #if can't be converted to a number 
    except ValueError:
        #check if string is = to "Done" or "done" to break loop
        if  userin.lower() == "done":
                break
        print("Invalid input")
        # tell user to enter valid number
        # use try except error handling here

    #end loop response prompt
    #print(num)

#result prompt
if isinstance(largest, float):
     print(f"Maximum is {int(largest)}")
else:
     print("Maximum is ", largest)

if isinstance(smallest, float):
     print(f"Minimum is {int(smallest)}")
else:
     print("Minimum is ", smallest)