def isUpper(str):
    for i in str:
        if i.isupper():
            return True
        else:
            continue
    return False
def isLower(str):
    for i in str:
        if i.islower():
            return True
        else:
            continue
    return False
def checkLen(str):
    if len(str)>=8:
        return True
    else:
        return False
def isNumeric(str):
    for i in str:
        if i.isnumeric():
            return True
        else:
            continue
    return False
def isGood(str):
    if isUpper(str) and isLower(str) and checkLen(str) and isNumeric(str):
        return True
    else:
        return False



str = input("Enter Your Password...")
if isGood(str):
    print("Good Password....")
else:
    print("Not Good Password....")