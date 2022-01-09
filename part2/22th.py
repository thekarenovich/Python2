from tkinter import *


def motion():
    c.move(ball, 1, 0)
    # print(c.coords(ball))
    # прибавляется к оси Х единичка двум противоположным точкам фигуры
    if c.coords(ball)[2] < 300:
        root.after(10, motion)
        # осторожно, рекурсия тут )


root = Tk()
c = Canvas(root, width=300, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,fill='green')
motion()
root.mainloop()
