import tkinter as tk

window = tk.Tk()
window.geometry("300x500")

label_1 = tk.Label(bg='red', width=20)
label_2 = tk.Label(bg='yellow', width=20)
label_3 = tk.Label(bg='blue', width=20)
label_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
label_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
label_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
window.mainloop()

# fill двигает лэйблы по осям Х или Y, или по обоим сразу
# fill имеет tk.X, tk.Y, tk.BOTH

# side решает на какой стороне лэйбл расположен:
# на левой, правой, нижней, верхней
# side имеет tk.LEFT, tk.RIGHT, tk.BOTTOM, tk.TOP
# по умолчанию side = tk.TOP

# если к fill=tk.BOTH добавить expand=True
# лэйблы будут максимально адаптированы под пользователя:
# поменя ширину и высоту окна, лэйбы также будут меняться по любой оси
# размерами высоты и ширины
