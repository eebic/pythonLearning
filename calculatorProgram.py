#calculatorProgram.py

"""
Title: Calculator Program
Author: Jenna Tran
Date Created: 2023-02-08
"""

#---INPUT---#
def getNumber():
    """
    This function will retreive a number from the user
    """
    userinput = input("insert number:")
    userinput = isNumeric(userinput)
    if userinput == False:
        return getNumber()
    else:
        return userinput

def operationChoice():
    """
    user picks which operation to use
    """
    print('''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    ''')
    choice = input("> ")
    choice = isNumeric(choice)
    if choice > 0 and choice < 5:
        return choice
    else:
        return operationChoice()
            


#---PROCESSING---#

def isNumeric(userinput):
    """
    This function will check if user input is valid.
    """

    try:
        userinput = int(userinput)
        return userinput
    except:
        print("Please pick a valid number.")
        return False
    

def addition(number1, number2):
    """
    this function will add two variables
    """
    answer = number1 + number2
    return answer
        


#---OUTPUT---#

def displayAnswer(answer):
    """
    function will display answer to the user
    """
    print("The solution to your calculation is : ", answer)




#---MAIN PROGRAM CODE---#

while True:
    input1 = getNumber()
    input2 = getNumber()
    choice = operationChoice()
    if choice == 1:
        answer = addition(input1, input2)
    displayAnswer(answer)