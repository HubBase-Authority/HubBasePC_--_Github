import random


def run():
    print("You are in a castle of a dragon.")
    DoorChoice = input("There are four doors. Which one do you enter? -- ")
    if DoorChoice == "1":
        print("You found a treasure")
        VipTreasure = random.randint(1, 100)
        if VipTreasure > 95:
            print("A Vip password was in it")
            print("It is 5-2-8-0")
        print("You win!")
    elif DoorChoice == "2":
        print("You are quickly attacked by an angry ogre.")
        print("You lose!")
    elif DoorChoice == "3":
        print("You see a sleeping dragon.")
        print("You can...")
        print("...1)Try to steal gold")
        print("...2)Try to escape")
        DragonChoice = input("1 or 2 -- ")
        if DragonChoice == "2":
            print("You were able to escape!")
            print("You win!")
        else:
            print("The dragon wakes up and eats you.")
            print("You lose!")
    elif DoorChoice == "4":
        print("You see a sphinx.")
        SPass = str(random.randint(1, 10))
        SGuess = input("Can you guess my number.It is inbetween 1 to 10 -- ")
        if SGuess == SPass:
            print("You are freed.")
            print("You win!")
        else:
            print("The sphinx traps you.")
            print("You lose!")
