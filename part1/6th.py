import tkinter as tk

window = tk.Tk()
window.title('FIRST')
window.geometry("500x650")
window.resizable(False, False)

frame_1 = tk.Frame(master=window)
label_1 = tk.Label(master=frame_1, text="HELLO!!!", width=10, height=15, bg='yellow')
label_1.pack()
frame_1.pack()

frame_2 = tk.Frame(master=window)
label_2 = tk.Label(master=frame_2, text="HELLO!!!", bg='blue', width=20, fg='white')
label_2.pack()
frame_2.pack()

frame_3 = tk.Frame(master=window)
label_3 = tk.Label(master=frame_3, text="HELLO!!!", bg='red')
label_3.pack()
frame_3.pack()

window.mainloop()

# Frame - что-то вроде окна в окне FIRST
# В него мы также помещаем виджеты, указывая название рамки через master
# В Frame не пишем параметры, пишем в его виджетах
