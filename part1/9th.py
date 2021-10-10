import tkinter as tk
 
window = tk.Tk()
window.title("FIRST")

frame = tk.Frame(master=window, width=230, height=150)
frame.pack()
 
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)
 
label2 = tk.Label(master=frame, text="I'm at (0, 75)", bg="yellow")
label2.place(x=0, y=75)

label2 = tk.Label(master=frame, text="I'm at (115, 45)", bg="black", fg="white")
label2.place(x=115, y=45)
  
window.mainloop()

#Благодаря place() мы устанавливаем точное расположение лэйбла
# при place() не зависит от остальных виджетов, как было при pack()
# здесь виджеты могут пересечься,а там они стоят рядом
