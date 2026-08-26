import random


def run():
    GNum = str(random.randint(1, 20))
    if VipAccess:
        GPstate = input("Learn correct answer(skips programm)[Y/N] -- ").upper()
        if GPstate != "Y":
            GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
            while GGuess != GNum:
                if int(GGuess) < int(GNum):
                    print("Too low")
                else:
                    print("Too high")
                GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
            print("Correct!")
        else:
            print("The number is", GNum)
    else:
        GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
        while GGuess != GNum:
            if int(GGuess) < int(GNum):
                print("Too low")
            else:
                print("Too high")
            GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
        print("Correct!")
