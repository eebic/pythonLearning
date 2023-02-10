"""
def chooseSit():
    """
    #This function will determine which situation to analyze.
"""
    choice = input("Choose canon situation:")
    choice == isSit(choice)
    choice = int(choice)
    if choice > 0 and choice < 3:
        return choice
    else:
        print("Please choose a valid situation.")
        return chooseSit()

#---PROCESSING---#

def isSit(choice):
    """
    #This function will check if user input is valid.
"""
    try:
        choice = int(choice)
        return choice
    except:
        print("Please choose a valid situation.")
        return chooseSit()
    
    

#---OUTPUT---#



#---MAIN PROGRAM CODE---#

while True:
    choice = chooseSit()
"""

userinput = input("Insert speed:")
userinput = float(userinput)
if userinput == False:
    print("invalid") 
else:
    print("cool") 