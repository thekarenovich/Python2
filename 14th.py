import tkinter as tk
from tkinter import ttk

def level():
    m=("  0", "  00", "  000")#Значения для combobox

    if(x.get()==1):
        var1=ttk.Combobox(values=m) 
        var1.current(1) #Для того, чтобы былр название в combox
        var1.place(x=100, y=10)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=60)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=110)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=160)


    elif(x.get()==2):
        var1=ttk.Combobox(values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.place(x=100, y=60)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=10)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=110)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=160)

        
    elif(x.get()==3):
        var1=ttk.Combobox(values=m)
        var1.current(1) #Для того, чтобы былр название в combox
        var1.place(x=100, y=110)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=60)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=10)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=160)

        
    elif(x.get()==4):
        var1=ttk.Combobox(values=m)
        var1.current(1) #Для того, чтобы былр название в combox
        var1.place(x=100, y=160)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=60)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=10)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.place(x=100, y=110)

window = tk.Tk()
window.title("")
window.geometry("400x200")
window.resizable(False, False)

x=tk.IntVar()
tk.Radiobutton(text="Неделя", variable=x, value=1, command=level).place(x=10, y=10)
tk.Radiobutton(text="Месяц", variable=x, value=2, command=level).place(x=10, y=60)
tk.Radiobutton(text="Квартал", variable=x, value=3, command=level).place(x=10, y=110)
tk.Radiobutton(text="Год", variable=x, value=4, command=level).place(x=10, y=160)

window.mainloop()
