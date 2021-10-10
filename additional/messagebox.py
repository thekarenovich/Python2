import tkinter as tk
from tkinter import messagebox

def Error():
    messagebox.showerror("Ошибка", "Не могу открыть файл")
 
def Warn():
    messagebox.showwarning("Предупреждение", "Вызов устаревшей функции")
 
def Quest():
    messagebox.askquestion("Вопрос", "Вы уверены, что хотите выйти?")
 
def Info():
    messagebox.showinfo("Информация", "Скачивание завершено")
  
window = tk.Tk()
window.title("Уведомления")
window.geometry("300x70+300+300")


error = tk.Button(window, text="Ошибка", width=15, command=Error)
error.grid(padx=5, pady=5)
warning = tk.Button(window, text="Предупреждение", width=15, command=Warn)
warning.grid(row=1, column=0)
question = tk.Button(window, text="Вопрос", width=15, command=Quest)
question.grid(row=0, column=1)
inform = tk.Button(window, text="Информация", width=15, command=Info)
inform.grid(row=1, column=1)

window.mainloop()
