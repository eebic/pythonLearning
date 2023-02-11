#pythonProject.py

"""
Title: Python Project
Author: Jenna Tran
Date Created: 2023-02-09
Date Finished: 2023-02-011
"""

import math

#---INPUT---#

def chooseSit():
    """
    This function will determine which scenario to analyze.
    """
    choice = input("Choose canon scenario: ")
    choice = int(choice)
    if choice > 0 and choice < 5:
        return choice
    else:
        print("Please choose a valid scenario.")
        return chooseSit()

def getSpeed():
    """
    This function will retreive a speed from the user.
    """
    userinput1 = input("Insert speed (m/s): ")
    userinput1 = float(userinput1)
    if userinput1 == False:
        return getSpeed()
    else:
        return userinput1

def getHeight():
    """
    This function will retreive a speed from the user.
    """
    userinput2 = input("Insert height (ft): ")
    userinput2 = float(userinput2)
    if userinput2 == False:
        return getHeight()
    else:
        return userinput2
    
def getAngle():
    """
    This function will retrieve an angle from the user.
    """
    userinput3 = input("Insert angle (degrees): ")
    userinput3 = float(userinput3)
    if userinput3 == False:
        return getAngle()
    else:
        return userinput3
    
def calcAgain():
    """
    This function asks if the user wants to calculate again
    """
    tryagain = input("Would you like to calculate again? y/n ")
    if tryagain == "y":
        return True
    elif tryagain == "n":
        print("Thank you for using this calculator!")
        tryagain == False
        return False
    else:
        print("Please insert valid option.")
        return calcAgain

#---PROCESSING---#

def A2R(userinput3):
    """
    This function will change angle to radian.
    """
    rad = math.radians(userinput3)
    return rad
    
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

def totTime(tim, tp):
    """
    This function calculates total time in scenario 3.
    """
    tt = tim + tp
    return tt

def disPeak(vs):
    """
    This funtion will calculate the maximum/peak height of the cannonball from scenario 3.
    """
    dp = ((vs) ** 2)/ (2 * 9.81)
    return dp

def totHeight(dp):
    """
    cmax height of cannonball + 15 = total height
    """
    th = dp + 15
    return th

def cos(rad):
    coss = math.cos(rad)
    return coss

def hortSpeed(userinput1, coss):
    """
    This function will calculate the horizontal speed.
    """
    hs = userinput1 * coss
    return hs

def sin(rad):
    sins = math.sin(rad)
    return sins

def vertSpeed(userinput1, sins):
    """
    This function will calculate the vertical speed.
    """
    vs = userinput1 * sins
    return vs

def sit1n3(userinput1, tim):
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

tryagain = True

while tryagain == True:
    
    print("""
Welcome to the Navy canon distance calculator. Find the distance a cannonball will travel given canon scenario:
    

    1. Horizontal to the water.

    2. Parabolic to a level boat.

    3. Parabolic to a smaller ship; too far for horizontal shot.
    
    """) 
    
    choice = chooseSit() 
    if choice == 1:
        userinput1 = getSpeed()
        userinput2 = getHeight()
        tim = time(userinput2)
        answer = sit1n3(userinput1, tim)
        showAnswer(answer)
    if choice == 2:
        userinput1 = getSpeed()
        userinput3 = getAngle()
        rad = A2R(userinput3)
        sins = sin(rad)
        vs = vertSpeed(sins, userinput1)
        coss = cos(rad)
        hs = hortSpeed(coss, userinput1)
        tp = timePeak(vs)
        answer = sit2(hs, tp)
        showAnswer(answer)
    if choice == 3:
        userinput1 = getSpeed()
        userinput2 = getHeight()
        userinput3 = getAngle()
        rad = A2R(userinput3)
        sins = sin(rad)
        vs = vertSpeed(sins, userinput1)
        coss = cos(rad)
        hs = hortSpeed(coss, userinput1)
        tp = timePeak(vs)
        dp = disPeak(vs)
        th = totHeight(dp)
        tim = time(th)
        tt = totTime(tim, tp)
        answer = sit1n3(hs, tt)
        showAnswer(answer)
        
    tryagain = calcAgain()

    