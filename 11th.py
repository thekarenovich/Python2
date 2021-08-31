import tkinter as tk
from tkinter import ttk #combox нет в tkinter

window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)

listt=("123", "321", "000", "21-2-1")#кортеж для значений выпадющего списка
combo = ttk.Combobox(
    #master=название окна 
    values=listt)
combo.current(0) #автоматически будет активирован нулевая по индексу строка
combo.pack()

print(combo.get())#получение выбранного значения из списка

window.mainloop()
