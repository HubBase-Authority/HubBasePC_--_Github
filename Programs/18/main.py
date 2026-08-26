import tkinter as tkr


def run():
    print("To draw, use LMB.")
    window2 = tkr.Tk()
    canvas1 = tkr.Canvas(window2, bg="white", width=750, height=500)
    canvas1.pack()
    global lastX, lastY
    lastX, lastY = 0, 0
    global Scolor
    Scolor = "black"
    width = int(input("How wide do you want your pencil? -- "))
    red_id = canvas1.create_rectangle(10, 10, 30, 30, fill="red")
    blue_id = canvas1.create_rectangle(10, 35, 30, 55, fill="blue")
    black_id = canvas1.create_rectangle(10, 60, 30, 80, fill="black")
    white_id = canvas1.create_rectangle(10, 85, 30, 105, fill="white")

    def StoreNewPos(event):
        global lastX, lastY
        lastX = event.x
        lastY = event.y

    def onClick(event):
        StoreNewPos(event)

    def onDrag(event):
        global Scolor
        canvas1.create_line(lastX, lastY, event.x, event.y, fill=Scolor, width=width)
        StoreNewPos(event)

    def CCTR(event):
        global Scolor
        Scolor = "red"

    def CCTB(event):
        global Scolor
        Scolor = "blue"

    def CCTb(event):
        global Scolor
        Scolor = "black"

    def CCTW(event):
        global Scolor
        Scolor = "white"

    canvas1.bind("<Button-1>", onClick)
    canvas1.bind("<B1-Motion>", onDrag)
    canvas1.tag_bind(red_id, "<Button-1>", CCTR)
    canvas1.tag_bind(blue_id, "<Button-1>", CCTB)
    canvas1.tag_bind(black_id, "<Button-1>", CCTb)
    canvas1.tag_bind(white_id, "<Button-1>", CCTW)
    window2.mainloop()
