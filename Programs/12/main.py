import random


def run():
    print("Create a list with 4 elements")
    print("")
    El1 = input("Element 1 -- ")
    El2 = input("Element 2 -- ")
    El3 = input("Element 3 -- ")
    El4 = input("Element 4 -- ")
    print("")
    print("The list will now change")
    List1 = [El1, El2, El3, El4]
    List1E = [El1, El2, El3, El4]
    print(List1)
    List1[0] = "Change?"
    print(List1)
    del List1[0]
    print(List1)
    List1.append("Change!")
    print(List1)
    Num = random.randint(0, 3)
    Num2 = random.randint(1, 3)
    Num3 = random.randint(0, 2)
    List2 = [List1E[Num], List1E[Num3], List1E[Num2]]
    List1 = List2 + List1
    print(List1)
    print('')
    for Cyc5 in List1:
        print(Cyc5)
