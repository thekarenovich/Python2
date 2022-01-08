from tkinter import *

window = Tk()
window.title("canvas3")

c = Canvas(window, width=200, height=200, bg='white')
c.pack()

c.create_polygon(100, 10, 20, 90, 180, 90)
#три точки - треугольник: указаны координаты каждой

c.create_polygon(40, 110, 160, 110,
                 190, 180, 10, 180,
                 fill='orange', #цвет оболочки
                 outline='black' #цвет границ фигуры
                 )
#четыре точки - четырёхугольник(трапеция): указаны координаты каждой

window.mainloop()
