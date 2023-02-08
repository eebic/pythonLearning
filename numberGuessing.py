#numberGuessing.py
"""
Title: Number Guessing Program
Author: Jenna Tran
Date Created: 2023-02-07
"""




import random

newnumber = True

while True:
    if newnumber == True:
        x = random.randint (1,10)
        newnumber = False
        
    try:
        userinput1 = input("Guess a number between 1 and 10.")
        userinput1 = int(userinput1)
        if userinput1 > x:
            print("Your number is greater than the target number.")
        elif userinput1 < x:
            print("Your number is lower than the target number. Try again.")
        elif userinput1 == x:
            print("CONGRATULATIONS! YOU WON THE GAME!")
            newnumber = True
        else:
            print("Did not insert valid option.")
        pass
    except:
        print("Invalid input.")