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


'''
# Можно совместно менять качества объектов через tag:

def color(event):
     c.itemconfig('group1', width=3,
                  fill="red")
 
 
root = Tk()
c = Canvas(width=460, height=150, 
           bg='white')
c.pack()
oval = c.create_oval(30, 10, 130, 80, 
                     tag="group1")
c.create_line(10, 100, 450, 100, 
              tag="group1")
c.bind('<Right>', color)'''
