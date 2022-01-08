from tkinter import *

window = Tk()
window.title("canvas2")

c = Canvas(window, width=200, height=200, bg='white')
c.pack()

c.create_rectangle(10, 10, 190, 60)
#Первые координаты – верхний левый угол, вторые – правый нижний.

c.create_rectangle(60, 80, 140, 190,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

window.mainloop()
