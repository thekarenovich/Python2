import tkinter as tk
from tkinter import filedialog

def onOpen():
    ftypes = [('Python файлы', '*.py'), ('Все файлы', '*')]
    dlg = filedialog.Open(filetypes = ftypes)
    fl = dlg.show()
 
    if fl != '':
        text = readFile(fl)
        txt.insert(tk.END, text)
 
def readFile(filename):
    with open(filename, "r") as f:
        text = f.read()
 
    return text
 
window=tk.Tk()
window.title("Окно для выбора файла")
window.geometry("300x250+300+300")
menubar = tk.Menu()
window.config(menu=menubar)
fileMenu = tk.Menu(menubar)
menubar.add_cascade(label="Файл", menu=fileMenu)
fileMenu.add_command(label="Открыть", command=onOpen)
txt = tk.Text()
txt.pack(fill=tk.BOTH, expand=1)
 
 

window.mainloop()
