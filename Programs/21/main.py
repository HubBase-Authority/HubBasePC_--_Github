import tkinter as tkr


def run():
    global game_list, move
    move = 0
    game_list = {1: [0, [0, 0, 100, 100]], 2: [0, [110, 0, 210, 100]], 3: [0, [220, 0, 320, 100]],
                 4: [0, [0, 110, 100, 210]], 5: [0, [110, 110, 210, 210]], 6: [0, [220, 110, 320, 210]],
                 7: [0, [0, 220, 100, 320]], 8: [0, [110, 220, 210, 320]], 9: [0, [220, 220, 320, 320]]}
    x = []
    o = []
    tttwindow = tkr.Tk()
    tttcanvas = tkr.Canvas(tttwindow, bg="white", width=320, height=320)
    tttcanvas.pack()
    S1_id = tttcanvas.create_rectangle(*game_list[1][1], fill="black")
    S4_id = tttcanvas.create_rectangle(*game_list[4][1], fill="black")
    S7_id = tttcanvas.create_rectangle(*game_list[7][1], fill="black")
    S2_id = tttcanvas.create_rectangle(*game_list[2][1], fill="black")
    S5_id = tttcanvas.create_rectangle(*game_list[5][1], fill="black")
    S8_id = tttcanvas.create_rectangle(*game_list[8][1], fill="black")
    S3_id = tttcanvas.create_rectangle(*game_list[3][1], fill="black")
    S6_id = tttcanvas.create_rectangle(*game_list[6][1], fill="black")
    S9_id = tttcanvas.create_rectangle(*game_list[9][1], fill="black")

    def Render(game_list: dict, move: int):
        for square in game_list:
            square_data = game_list[square]
            if square_data[0] == 0:
                pass
            elif square_data[0] == 1:
                new_square_data = [square_data[1][2], square_data[1][1], square_data[1][0], square_data[1][3]]
                tttcanvas.create_line(*square_data[1], fill="red", width=3)
                tttcanvas.create_line(*new_square_data, fill="red", width=3)
                if not square in x:
                    x.append(square)
            elif square_data[0] == 2:
                tttcanvas.create_oval(*square_data[1], outline="blue", width=3)
                if not square in o:
                    o.append(square)
        if (((1 in x and 4 in x and 7 in x) or (1 in x and 2 in x and 3 in x) or (2 in x and 5 in x and 8 in x) or
             (4 in x and 5 in x and 6 in x) or (3 in x and 6 in x and 9 in x) or (7 in x and 8 in x and 9 in x)) or
            (1 in x and 5 in x and 9 in x)) or (3 in x and 5 in x and 7 in x):
            print("X`es have won!")
            tttwindow.destroy()
        elif (((1 in o and 4 in o and 7 in o) or (1 in o and 2 in o and 3 in o) or (2 in o and 5 in o and 8 in o) or
               (4 in o and 5 in o and 6 in o) or (3 in o and 6 in o and 9 in o) or (7 in o and 8 in o and 9 in o)) or
              (1 in o and 5 in o and 9 in o)) or (3 in o and 5 in o and 7 in o):
            print("Circles have won!")
            tttwindow.destroy()
        elif move == 9:
            print("Draw.")
            tttwindow.destroy()

    def Move(event):
        global move, game_list
        for key, x in game_list.items():
            if x[1][0] <= event.x <= x[1][2] and x[1][1] <= event.y <= x[1][3]:
                square = key
                break
        else:
            raise Exception("Click location not found")
        if move % 2 == 0:
            side = 1
        else:
            side = 2
        if game_list[square][0] == 0:
            game_list[square][0] = side
            move += 1
            Render(game_list, move)

    tttcanvas.tag_bind(S1_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S2_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S3_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S4_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S5_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S6_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S7_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S8_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S9_id, "<Button-1>", Move)
    Render(game_list, move)
    tttwindow.mainloop()
