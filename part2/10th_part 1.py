import tkinter as tk
 
window = tk.Tk()
 
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED, # тип границы рамки
            borderwidth=3 # толщина границы рамки
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(
            padx=5,
            pady=5
            )

# Помним, что padx и pady - отступы от виджета
# Те, что в самом виджете через pack(), отсосятся исключительно к нему
# Они меняют его внутреннюю среду
# А те, что к рамке,определяют отступы самой рамки, следовательно
# Взаимное расположение всех рамок


window.mainloop()
