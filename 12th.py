import tkinter as tk

def onExit():
    quit() # функция закрытия компилятора

def count1():
    print(1+1)

def count2():
    print(2+2)

def count3():
    print(3+3)

def count4():
    print(4+4)

    
window = tk.Tk()
window.title("Simple Menu")
window.resizable(False,False)

menubar = tk.Menu(window) # создание меню
window.config(menu=menubar) # настраивание окна, добавлением меню
# под меню имеется в виду поверхность экрана со вкладками

# создание меню в меню или просто вкладки (filemenu) в меню (Menuu)
filemenu = tk.Menu(menubar)
filemenu2 = tk.Menu(menubar)
filemenu3 = tk.Menu(menubar)

# распредление всех меню(вкладок) или добавление команд во вкладки
menubar.add_cascade(label="File", menu=filemenu) # добавление в меню вкладки filemenu с названием "File"
menubar.add_cascade(label="File2", menu=filemenu2)
filemenu.add_command(label="Exit", command=onExit) # вкладки во вкладке или попроще строки с командой
filemenu2.add_cascade(label="File3", menu=filemenu3)
filemenu3.add_command(label="Count 1+1", command=count1)
filemenu3.add_separator() 
filemenu3.add_command(label="Count 2+2", command=count2)
filemenu3.add_separator() 
filemenu3.add_command(label="Count 3+3", command=count3)
filemenu3.add_separator() 
filemenu3.add_command(label="Count 4+4", command=count4)
filemenu2.add_cascade(label="File4")

 
window.mainloop()
