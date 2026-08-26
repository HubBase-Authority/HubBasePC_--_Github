import random
import tkinter as tkr


def run():
    def Setup_minesweeper():
        global gameOver, score, squaresLeft, minefield
        gameOver = False
        score = 0
        squaresLeft = 0
        minefield = []

    def printfield(minefield):
        for rowList in minefield:
            print(rowList)

    def create_minefield(minefield, window):

        def generate_minefield(minefield):
            global squaresLeft
            for row in range(10):
                rowList = []
                for column in range(10):
                    BombRN = random.randint(1, 100)
                    if BombRN <= 20:
                        rowList.append(1)
                    else:
                        rowList.append(0)
                        squaresLeft = squaresLeft + 1
                minefield.append(rowList)

        def set_Flag(event):
            global score, squaresLeft, gameOver, minefield, PFQ
            square = event.widget
            currentText = square.cget("text")
            if currentText == "    ":
                square.config(bg="yellow", text="" + "B" + "")
            if currentText == "B":
                square.config(bg="green", text="    ")

        def check_Bombs(event):
            global score, squaresLeft, gameOver, minefield, PFQ
            square = event.widget
            row = int(square.grid_info()["row"])
            column = int(square.grid_info()["column"])
            currentText = square.cget("text")
            if gameOver == False:
                if minefield[row][column] == 1:
                    gameOver = True
                    square.config(bg="red")
                    print("Game over! You hit a bomb!")
                    print("Your score was: ", score)
                    if VipAccess:
                        if PFQ == "Y":
                            print("**Even with a cheat!!!**")
                    print("Your score was:", score)
                elif currentText == "    ":
                    square.config(bg="brown")
                    totalBombs = 0
                    if row < 9:
                        if minefield[row + 1][column] == 1:
                            totalBombs = totalBombs + 1
                    if row > 0:
                        if minefield[row - 1][column] == 1:
                            totalBombs = totalBombs + 1
                    if column > 0:
                        if minefield[row][column - 1] == 1:
                            totalBombs = totalBombs + 1
                    if column < 9:
                        if minefield[row][column + 1] == 1:
                            totalBombs = totalBombs + 1
                    if row > 0 and column > 0:
                        if minefield[row - 1][column - 1] == 1:
                            totalBombs = totalBombs + 1
                    if row < 9 and column < 9:
                        if minefield[row + 1][column + 1] == 1:
                            totalBombs = totalBombs + 1
                    if row > 0 and column < 9:
                        if minefield[row - 1][column + 1] == 1:
                            totalBombs = totalBombs + 1
                    if row < 9 and column > 0:
                        if minefield[row + 1][column - 1] == 1:
                            totalBombs = totalBombs + 1
                    square.config(text=" " + str(totalBombs) + " ")
                    score += 1
                    squaresLeft -= 1
                    if squaresLeft == 0:
                        gameOver = True
                        print("Well done!")
                        print("Your score was: ", score)

        def layout_minefield(window, minefield):
            global VipAccess
            for rowNumber, rowList in enumerate(minefield):
                for columnNumber, columnEntry in enumerate(rowList):
                    RSC = random.randint(1, 100)
                    if RSC < 25:
                        square = tkr.Label(window, text="    ", bg="darkgreen")
                    elif RSC > 75:
                        square = tkr.Label(window, text="    ", bg="seagreen")
                    else:
                        square = tkr.Label(window, text="    ", bg="green")
                    square.grid(row=rowNumber, column=columnNumber)
                    square.bind("<Button-1>", check_Bombs)
                    square.bind("<Button-3>", set_Flag)

        generate_minefield(minefield)
        layout_minefield(window, minefield)

    def Play_minesweeper():
        global VipAccess, minefield, PFQ
        window3 = tkr.Tk()
        create_minefield(minefield, window3)
        if VipAccess:
            PFQ = input("Do you want a cheat?[Y/N] -- ").upper()
            if PFQ == "Y":
                printfield(minefield)
        window3.mainloop()

    Setup_minesweeper()
    Play_minesweeper()
