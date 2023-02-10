
def chooseSit():
    userinput = input("Choose canon situation:")
    userinput = isSit(userinput)
    return userinput
    
def isSit():
    try:
        userinput = int(userinput)
        if userinput > 0 and userinput < 3:
            return userinput
    except:
        print("Please pick a valid number.")
        return False