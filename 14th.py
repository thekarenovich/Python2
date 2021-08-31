import tkinter as tk
from tkinter import ttk

def level():
    m=(" ", " ", " ")

    if(x.get()==1):
        var1=ttk.Combobox(values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=1, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=2, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=3, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=4, column=2, padx=5, pady=5)


    elif(x.get()==2):
        var1=ttk.Combobox(values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=2, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=1, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=3, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=4, column=2, padx=5, pady=5)

        
    elif(x.get()==3):
        var1=ttk.Combobox(values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=3, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=2, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=1, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=4, column=2, padx=5, pady=5)

        
    elif(x.get()==4):
        var1=ttk.Combobox(values=m)
        var1.current(1) #Для того, чтобы былр название в comboxe
        var1.grid(row=4, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=2, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=3, column=2, padx=5, pady=5)

        var = tk.Label(
        text="  ",
        foreground="white", 
        background="white",  
        width=27, 
        height=2 )
        var.grid(row=1, column=2, padx=5, pady=5)

window = tk.Tk()
window.title("")
window.geometry("400x200")
window.resizable(False, False)

x=tk.IntVar()

tk.Radiobutton(text="Неделя", variable=x, value=1, command=level).grid(row=1, column=1, padx=5, pady=5)
tk.Radiobutton(text="Месяц", variable=x, value=2, command=level).grid(row=2, column=1, padx=5, pady=5)
tk.Radiobutton(text="Квартал", variable=x, value=3, command=level).grid(row=3, column=1, padx=5, pady=5)
tk.Radiobutton(text="Год", variable=x, value=4, command=level).grid(row=4, column=1, padx=5, pady=5)

window.mainloop()
