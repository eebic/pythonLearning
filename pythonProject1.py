#pythonProject.py

"""
Title: Python Project
Author: Jenna Tran
Date Created: 2023-02-09
"""


#---INPUT---#

print("""Welcome to the Navy canon distance calculator. Find the distance a cannonball will travel given canon situation:
    
    1. Horizontal to the water.

    2. Parabolic to a level boat.

    3. Parabolic to a smaller ship; too far for horizontal shot.""")


def chooseSit():
    """
    This function will determine which situation to analyze.
    """
    userinput = input("Choose canon situation:")
    userinput = isSit(userinput)
    if userinput > 0 and userinput < 3:
        return userinput
    else:
        print("Please choose a valid situation.")
        return chooseSit()

#---PROCESSING---#

def isSit(userinput):
    """
    This function will check if user input is valid.
    """
    try:
        userinput = int(userinput)
        return userinput
    except:
        print("Please choose a valid situation.")
        return chooseSit()
    
    

#---OUTPUT---#



#---MAIN PROGRAM CODE---#