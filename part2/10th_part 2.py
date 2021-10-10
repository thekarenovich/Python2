import tkinter as tk
 
window = tk.Tk()
window.minsize(250,147)
 
for i in range(3):
    window.columnconfigure(i, weight=1#,
                           #minsize=75
                           )
    window.rowconfigure(i, weight=1#,
                        #minsize=50
                        )
 
    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
 
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)
 
window.mainloop()

#Индекс столбца или строки сетки, которого нужно настроить

# minsize, который устанавливает минимальный размер высоты строки или ширины столбца в пикселях.

#Аргумент weight по умолчанию равен 0 .
#Это означает, что столбец или строка не расширяются при изменении размера окна.
#Если каждому столбцу и строке присвоен weight=1, то все они будут меняться одинаково.
