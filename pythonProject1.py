#pythonProject.py

"""
Title: Python Project
Author: Jenna Tran
Date Created: 2023-02-09
"""

import math

#---INPUT---#

print("""
Welcome to the Navy canon distance calculator. Find the distance a cannonball will travel given canon situation:
    

    1. Horizontal to the water.

    2. Parabolic to a level boat.

    3. Parabolic to a smaller ship; too far for horizontal shot.
    
    """)

def getSpeed():
    """
    This function will retreive a speed from the user.
    """
    userinput = input("Insert speed:")
    userinput = float(userinput)
    if userinput == False:
        return getSpeed()
    else:
        return userinput

def getHeight():
    """
    This function will retreive a speed from the user.
    """
    userinput = input("Insert speed:")
    userinput = float(userinput)
    if userinput == False:
        return getSpeed()
    else:
        return userinput

def chooseSit():
    """
    This function will determine which situation to analyze.
    """
    choice = input("Choose canon situation:")
    choice = int(choice)
    if choice > 0 and choice < 3:
        return choice
    else:
        print("Please choose a valid situation.")
        return chooseSit()

#---PROCESSING---#

def sit1():
    """
    This function will calculate situation 1.
    """


    
    

#---OUTPUT---#



#---MAIN PROGRAM CODE---#
while True:
    choice = chooseSit()