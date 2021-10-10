import tkinter as tk
from tkinter.ttk import Notebook

window = tk.Tk()
window.title("")
window.resizable(False, False)

note = Notebook(window)

window_1=tk.Frame(window, relief=tk.FLAT, height=100)
window_2=tk.Frame(window, relief=tk.FLAT, height=100)
window_3=tk.Frame(window, relief=tk.FLAT, height=100)

note.add(window_1, text="Окно 1")
note.add(window_2, text="Окно 2")
note.add(window_3, text="Окно 3")
note.pack()

label1 = tk.Label(master=window_1, text="ОКНО 1")
label1.place(x=77, y=35)
label2 = tk.Label(master=window_2, text="ОКНО 2")
label2.place(x=77, y=35)
label3 = tk.Label(master=window_3, text="ОКНО 3")
label3.place(x=77, y=35)

window.mainloop()
