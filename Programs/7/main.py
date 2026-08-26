import time


def run():
    aliens = 2
    APass = "ALIENS"
    print("Aliens are invading the earth!")
    print("Activate the defence platform!")
    print("")
    print("------------------------------------------")
    print("           The defence platform           ")
    print("------------------------------------------")
    time.sleep(1)
    print("")
    print("------------------------------------------")
    print("            Checking VipAccess            ")
    print("------------------------------------------")
    time.sleep(1)
    if VipAccess:
        print("VipAccess = True")
        print("--Access granted--")
        print("Password =", APass)
    else:
        print("VipAccess = False")
        APassGuess = input("Please enter the password -- ").upper()
        while APassGuess != APass:
            print("")
            print("INCORRECT PASSWORD")
            print("")
            aliens = aliens ** 2
            print("There are", aliens, "aliens now on earth")
            if aliens > 8000000000:
                break
            print("")
            print("Hint: The thing is attacking us.")
            print("")
            APassGuess = input("Please enter the password -- ").upper()
        if APassGuess == APass:
            print("We won! Hooray!")
        else:
            print("No! The aliens have out numbered us!")
