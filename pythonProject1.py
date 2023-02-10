#pythonProject.py

"""
Title: Python Project
Author: Jenna Tran
Date Created: 2023-02-09
"""

import math

#---INPUT---#

print("""
Welcome to the Navy canon distance calculator. Find the distance a cannonball will travel given canon scenario:
    

    1. Horizontal to the water.

    2. Parabolic to a level boat.

    3. Parabolic to a smaller ship; too far for horizontal shot.
    
    """)

def getSpeed():
    """
    This function will retreive a speed from the user.
    """
    userinput = input("Insert speed: ")
    userinput = float(userinput)
    if userinput == False:
        return getSpeed()
    else:
        return userinput

def getHeight():
    """
    This function will retreive a speed from the user.
    """
    userinput = input("Insert height: ")
    userinput = float(userinput)
    if userinput == False:
        return getHeight()
    else:
        return userinput
    
def getAngle():
    """
    This function will retrieve an angle from the user.
    """
    userinput = input("Insert angle: ")
    userinput = float(userinput)
    if userinput == False:
        return getAngle()
    else:
        return userinput

def chooseSit():
    """
    This function will determine which scenario to analyze.
    """
    choice = input("Choose canon scenario: ")
    choice = int(choice)
    if choice > 0 and choice < 3:
        return choice
    else:
        print("Please choose a valid scenario.")
        return chooseSit()

#---PROCESSING---#

def time(userinput2):
    """
    This function will calculate time given height.
    """
    tim = math.sqrt((2 * userinput2)/9.81)
    return tim

def timePeak(vs):
    """
    This function will calculate peak time given vs.
    """
    tp = vs / 9.81
    return tp

def hortSpeed(userinput1):
    """
    This function will calculate the horizontal speed.
    """
    hs = math.cos(userinput3) * userinput1
    return hs

def vertSpeed(userinput1):
    """
    This function will calculate the vertical speed.
    """
    vs = math.sin(userinput3) * userinput1
    return vs

def sit1(userinput1, tim):
    """
    This function will calculate distance from scenario 1.
    """
    answer = userinput1 * tim
    return answer

    #speed x time

def sit2(hs, tp):
    """
    This function will calculate distance from scenario 2. REMINDER ABOUT OTHER METHOD.
    """
    answer = hs * (2 * tp)
    return answer



#---OUTPUT---#

def showAnswer(answer):
    """
    This function will show the answer.
    """
    print("The total distance the cannonball traveled is: ", answer)

#---MAIN PROGRAM CODE---#
while True:
    choice = chooseSit()
    userinput1 = getSpeed() 
    if choice == 1:
        userinput2 = getHeight()
        tim = time(userinput2)
        answer = sit1(userinput1, tim)
    if choice == 2:
        userinput3 = getAngle()
        vs = vertSpeed(userinput1)
        tp = timePeak(vs)
        hs = hortSpeed(userinput1)
        answer = sit2(hs, tp)
    showAnswer(answer)
    if choice == 3:
        userinput2 = getHeight()
        userinput3 = getAngle()
    