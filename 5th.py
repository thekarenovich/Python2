import tkinter as tk

def first():
    
    def get():
        s=text_box.get("1.0", tk.END)
        # в get() обязательно нужно писать хотя бы один индекс
        # иначе будет ошибка
        # тут нужно указать в виде строки
        # 1 - номер строки
        # 0 - индекс символа строки
        if s:
            print(s)
        else:
            print('Empty')

    def delete():
        # s=text_box.delete("1.0", "2.2")
        ss=text_box.delete("1.0", tk.END)

    def insert():
        s=text_box.insert("5.4","DUDE")

    window=tk.Tk()
    window.title("FIRST")
    window.geometry("500x650") 
    window.resizable(False, False)

    text_box = tk.Text(bg='black', fg='white', font=(20))
    text_box.pack()
    #Text() отличается от Entry() тем,что вмещает в себя больше одной строки

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


    #Кнопка вставки текста DUDE
    button_3=tk.Button(window, text="INSERT DUDE",
                activebackground='white',
                activeforeground='red',
                command=insert)
    button_3.pack()

    window.mainloop()

if __name__=="__main__":
    first()
