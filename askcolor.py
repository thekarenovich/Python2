import tkinter as tk
from tkinter import colorchooser

def onChoose():
    (rgb, hx) = colorchooser.askcolor() #ф-ция задания цвета
    frame.config(bg=hx) #настраиваем цвет нашей рамки frame
    #print(rgb, hx)

window=tk.Tk()
window.title("Цветовая палитра")
window.geometry("300x150+300+300")

btn = tk.Button(window, text="Выберите цвет", command=onChoose)
btn.place(x=20, y=30)

frame = tk.Frame(
    border=6,
    relief=tk.SUNKEN,
    width=120, height=100)
frame.place(x=160, y=30)

window.mainloop()

