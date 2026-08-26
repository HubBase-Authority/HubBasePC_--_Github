def run():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = alphabet * 2
    STE = input("The string that you want to encrypt -- ").upper()
    Key = int(input("Enter a number between -25 and 25 -- "))
    ES = ""
    for x in STE:
        pos = alphabet.find(x)
        NewPos = pos + Key
        if x in alphabet:
            ES = ES + alphabet[NewPos]
        else:
            ES = ES + x
    print("The message is:", ES)
