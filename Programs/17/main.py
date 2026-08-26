import time
import tkinter as tkr


def run():
    window1 = tkr.Tk()
    button1 = tkr.Button(window1, text="Do not press this button", width=40)
    button1.pack(padx=10, pady=10)
    global clicks1
    clicks1 = 0

    def onClick(event):
        global clicks1
        clicks1 = clicks1 + 1
        if clicks1 == 1:
            button1.configure(text="Seriously? Do. Not. Press. It.")
        elif clicks1 == 2:
            button1.configure(text="Gah! Next next time no-no-no more butt-utt-on-on")
        elif clicks1 == 3:
            time.sleep(1.0)
            button1.configure(text="Opps. I said 'Next next time'")
        else:
            button1.pack_forget()

    button1.bind("<ButtonRelease-1>", onClick)
    window1.mainloop()
