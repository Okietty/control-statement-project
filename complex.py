passworkChecker = input("Input in a password to be verified if it's usuable: ")

if len(passworkChecker) == 8:

    illegalChar = False
    capLetter = False
    lowerLetter = False
    numInPass = False

    for i in '{}<>?/\|`~':
        if i in passworkChecker:
            print("Ths password contains illegal characters used: {}<>?/\|`~")
            illegalChar = True

    if illegalChar == False:
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i in passworkChecker:
                capLetter = True

    if capLetter == False:
        print("This password is invalid, please try a different password.")

    if capLetter == True:
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if i in passworkChecker:
                lowerLetter = True

    if lowerLetter == False:
        print("This password is invalid, please try a different password.")

    if lowerLetter == True:
        for i in '1234567890':
            if i in passworkChecker:
                numInPass = True

    if numInPass == True:
        print("This password is valid.")

    if numInPass == False:
        print("This password is invalid, please try a different password.")


else:
    print("The password is not 8 cahracters long.")