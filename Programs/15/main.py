from turtle import *


def run():
    color("blue")
    shape("turtle")
    speed(10)
    pensize(4)
    NoA = int(input("How many sides do you want? -- "))
    Angle = 360 / NoA
    for Cyc7 in range(NoA):
        forward(50)
        right(Angle)
