import tkinter as tk

def first():
    
    def get():
        s=entry.get()
        print(s)

    def delete():
        s=entry.delete(0, 2)
        ss=entry.delete(0, tk.END)
        # 0, 2 - индексы символов
        # tk.END - до конца строки

    def insert():
        s=entry.insert(0,"LOOOL")
        # 0 - индекс символа

    window=tk.Tk()
    window.title("FIRST")
    window.geometry("500x650") 
    window.resizable(False, False)
        
    label=tk.Label(window, text='Name',
                       font=("Arial", 20),
                       bg='white',
                       fg='black')
    label.pack()

    #Ввод
    entry=tk.Entry(fg="white", bg="black", width=100)
    entry.pack()


    #Кнопка получения введённого текста 
    button_1=tk.Button(window, text="GET",
                     activebackground='white',
                     activeforeground='red',
                     command=get)
    button_1.pack()



    #Кнопка удаления введённого текста 
    button_2=tk.Button(window, text="DELETE",
                    activebackground='white',
                    activeforeground='red',
                    command=delete)
    button_2.pack()


    #Кнопка вставки
    button_3=tk.Button(window, text="INSERT",
                activebackground='white',
                activeforeground='red',
                command=insert)
    button_3.pack()



    window.mainloop()

if __name__=="__main__":
    first()
