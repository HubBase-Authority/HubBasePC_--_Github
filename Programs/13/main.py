def run():
    print("Create a list with 2 elements and 2 keys")
    print("")
    El1 = input("Element 1 -- ")
    El2 = input("Element 2 -- ")
    Key1 = input("Key 1 -- ")
    Key2 = input("Key 2 -- ")
    print("")
    print("The list will now change")
    List1 = {Key1: El1, Key2: El2}
    List1E = {Key1: El1, Key2: El2}
    print(List1)
    List1["Change?"] = "Change!"
    print(List1)
    del List1[Key1]
    print(List1)
    List1[Key2] = "Changeful!"
    print(List1)
    print('')
    for Cyc6 in List1:
        print(Cyc6)
