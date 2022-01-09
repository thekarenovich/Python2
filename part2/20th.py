from tkinter import *

window = Tk()
c = Canvas(width=200, height=200,
           bg='white')
c.pack()

rect = c.create_rectangle(
    80, 80, 120, 120, fill='lightgreen')

def focus(event):
    c.itemconfig(rect, fill='green', width=2) #меняет свойства фигуры
    c.coords(rect, 70, 70, 130, 130) #меняет координаты фигуры

c.bind('<FocusIn>', focus)

window.mainloop()
