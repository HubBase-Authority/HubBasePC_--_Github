import time
import tkinter as tkr
from tkinter import messagebox


def run():
    def move_tennisObject(object):
        global batSpeed, bat, rightPressed, leftPressed, ball, canvas2, canvasWidth, ballMoveX, ballMoveY, setBatBottom, setBatTop, score, bounceCount
        if object == "bat":
            batMove = batSpeed * rightPressed - batSpeed * leftPressed
            (batLeft, batTop, batRight, batBottom) = canvas2.coords(bat)
            if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
                canvas2.move(bat, batMove, 0)
        elif object == "ball":
            (batLeft, batTop, batRight, batBottom) = canvas2.coords(bat)
            (ballLeft, ballTop, ballRight, ballBottom) = canvas2.coords(ball)
            if ballMoveX > 0 and ballRight > canvasWidth:
                ballMoveX = -ballMoveX
            if ballMoveX < 0 and ballLeft < 0:
                ballMoveX = -ballMoveX
            if ballMoveY < 0 and ballTop < 0:
                ballMoveY = -ballMoveY
            if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
                (batLeft, batTop, batRight, batBottom) = canvas2.coords(bat)
                if (ballMoveX > 0 and (ballRight + ballMoveX > batLeft and ballLeft < batRight) or ballMoveX < 0 and (
                        ballRight > batLeft and ballLeft + ballMoveX < batRight)):
                    ballMoveY = -ballMoveY
                    score += 1
                    bounceCount += 1
                    if bounceCount == 4:
                        bounceCount = 0
                        batSpeed += 1
                        if ballMoveX > 0:
                            ballMoveX += 1
                        else:
                            ballMoveX -= 1
                        ballMoveY -= 1
            canvas2.move(ball, ballMoveX, ballMoveY)
        else:
            print("Such object does not exist")

    def close():
        global windowOpen, window4
        windowOpen = False
        window4.destroy()

    def check_game_over():
        global canvasHeight
        (ballLeft, ballTop, ballRight, ballBottom) = canvas2.coords(ball)
        if ballTop > canvasHeight:
            print("Your score was: ", str(score))
            PlayAgain = tkr.messagebox.askyesno(message="Play again?")
            if PlayAgain:
                reset()
            else:
                close()

    def on_key_press(event):
        global rightPressed, leftPressed
        if event.keysym == "Left":
            leftPressed = 1
        if event.keysym == "Right":
            rightPressed = 1

    def on_key_release(event):
        global rightPressed, leftPressed
        if event.keysym == "Left":
            leftPressed = 0
        if event.keysym == "Right":
            rightPressed = 0

    def setup_Tennis():
        global bat, ball, windowOpen, batSpeed, rightPressed, leftPressed, canvas2, canvasWidth, canvasHeight, ballMoveX, ballMoveY, setBatBottom, setBatTop, window4, score, bounceCount
        canvasWidth = 750
        canvasHeight = 500
        window4 = tkr.Tk()
        canvas2 = tkr.Canvas(window4, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
        canvas2.pack()
        bat = canvas2.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
        ball = canvas2.create_oval(0, 0, 10, 10, fill="deep pink")
        windowOpen = True
        batSpeed = 6
        rightPressed = 0
        leftPressed = 0
        ballMoveX = 4
        ballMoveY = -4
        setBatTop = canvasHeight - 40
        setBatBottom = canvasHeight - 30
        score = 0
        bounceCount = 0
        window4.protocol("WM_DELETE_WINDOW", close)
        window4.bind("<KeyPress>", on_key_press)
        window4.bind("<KeyRelease>", on_key_release)
        canvas2.coords(bat, 10, setBatTop, 50, setBatBottom)
        canvas2.coords(ball, 20, setBatTop - 10, 30, setBatTop)

    def reset():
        global bat, ball, windowOpen, batSpeed, rightPressed, leftPressed, canvas2, canvasWidth, canvasHeight, ballMoveX, ballMoveY, setBatBottom, setBatTop, window4, score, bounceCount
        leftPressed = 0
        rightPressed = 0
        ballMoveX = 4
        ballMoveY = -4
        score = 0
        bounceCount = 0
        canvas2.coords(bat, 10, setBatTop, 50, setBatBottom)
        canvas2.coords(ball, 20, setBatTop - 10, 30, setBatTop)

    def play_Tennis():
        global windowOpen, window4
        while windowOpen:
            move_tennisObject("bat")
            move_tennisObject("ball")
            window4.update()
            time.sleep(0.02)
            if windowOpen:
                check_game_over()

    setup_Tennis()
    play_Tennis()
