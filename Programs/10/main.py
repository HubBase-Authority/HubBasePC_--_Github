def run():
    TTMN = int(input("What number to muitiply by -- "))
    TTEN = int(input("The final number -- ")) + 1
    for Cyc2 in range(1, TTEN):
        print(Cyc2, "x", TTMN, "=", Cyc2 * TTMN)
