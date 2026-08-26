import random
from turtle import *


def run():
    def VShape(size):
        right(25)
        forward(size)
        backward(size)
        left(50)
        forward(size)
        backward(size)
        right(25)

    def SnowflakeArm(size):
        for Cyc8 in range(4):
            forward(size)
            VShape(size)
        backward(size * 4)

    def Snowflake(size):
        color(random.choice(colors))
        for Cyc7 in range(NoA):
            SnowflakeArm(size)
            right(Angle)

    colors = ["white", "blue", "cyan", "purple", "green", "white", "white"]
    goto(0, 0)
    shape("turtle")
    speed(10)
    pensize(6)
    Screen().bgcolor("turquoise")
    clear()
    NoA = int(input("How many arms do you want? -- "))
    NoS = int(input("How many snowflakes do you want? -- "))
    Angle = 360 / NoA
    for Cyc9 in range(NoS):
        size = random.randint(5, 30)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        penup()
        goto(x, y)
        pendown()
        Snowflake(size)
