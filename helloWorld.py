#helloworld.py

"""
Title: Hello World Program
Author: Jenna Tran
Date Created: 2023-02-07


#this is a print function

print("Hello, World!")


#variable types

x = 5
y = 7
#integer

float1 = 8.5
float2 = 5.3
#floats


print(type(x))
print(type(float1))

string1 = "Hello, World!"
string2 = 8
#string

true = True
false = False
#booleans


addition = +
substraction = -
multiple = *
divide = /


print(x + y)
print(x - y)
print(x * y)
print(x / y)

print("x + y is equal to:", x + y)


while True:
    userinput = input("please insert a number:")
    try:
        userinput = int(userinput)
        print("your number plus 10 is:", userinput + 10)
        tryagain = input("would you like to input another number y/n")
        if tryagain == "y":
            pass
        elif tryagain == "n":
            break
        else:
            print("did not insert valid option, restarting program.")
            pass            
    except:
        print("please input an integer")
        pass
"""

while True:
    userinput = input("please insert your first number:")
    try:
        userinput1 = int(userinput)
        userinput = input("please insert your second number:")
        userinput2 = int(userinput)
        userinput = input("would you like to add or subtract the numbers? +/-")
        if userinput == "+":
            print("the sum of your numbers is equal to:", userinput1+userinput2)
            tryagain = input("would you like to calculate again? y/n")
            if tryagain == "y":
                pass
            elif tryagain == "n":
                break
            else:
                print("did not insert valid option, restarting program.")
                pass
        elif userinput == "-":
            print("the difference of your numbers is equal to:", userinput1-userinput2)
            tryagain = input("would you like to calculate again? y/n")
            if tryagain == "y":
                pass
            elif tryagain == "n":
                break
            else:
                print("did not insert valid option, restarting program.")
                pass
        else:
            print("did not insert valid option, fsjdomkl")
            pass

    except:
        print("please input an integer")
        pass





       
   

