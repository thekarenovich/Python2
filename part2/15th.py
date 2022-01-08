from tkinter import *

window = Tk()
window.title("canvas1")

c = Canvas(window, width=200, height=200, bg='white')
c.pack()

c.create_line(10, 10, 190, 50)
#первые два параметра - координаты конца линии
#другие два - другого конца

c.create_line(100, 180, 100, 60,
              fill='green',
              width=5,
              arrow=LAST,
              dash=(10, 5), #первый параметр увеличивает количество полос; второй - толщина расстояния между полос
              activefill='lightgreen',
              arrowshape="10 20 10" #вид стрелки
              )

window.mainloop()
