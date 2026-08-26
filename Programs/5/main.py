def run():
    User_reply = input("Do you like robots? -- ").upper()
    if User_reply == "YES":
        User_reply = "Y"
    elif User_reply == "NO":
        User_reply = "N"
    elif User_reply == "MAYBE":
        User_reply = "M"
    if User_reply == "Y":
        print("Beep Boop!")
    elif User_reply == "N":
        print("Well, robots don't like you either")
        global VipAccess
        if VipAccess:
            print("--Vip level access taken--")
        VipAccess = False
    elif User_reply == "M":
        print("Make up your mind, human")
    else:
        print("Print('input(something sensible)')")
