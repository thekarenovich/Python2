import tkinter as tk

def first():

    def say_hello():
        print("hello")

    def add_label():
        label=tk.Label(window, text="WOW", bg='red', fg='black')
        label.pack()

    def counter():
        global count
        count+=1
        print(count)
        
    window=tk.Tk()
    window.title("FIRST")
    window.geometry("500x650") 
    window.resizable(False, False)
    window.wm_attributes("-topmost", 1)
        
    button_1=tk.Button(window, text='Hello', command=say_hello, bg='white', fg='black',
                    activebackground='blue', activeforeground='red')
    button_1.pack()

    button_2=tk.Button(window, text='Add label', command=add_label)
    button_2.pack()

    button_3=tk.Button(window, text='Counter', command=counter)
    button_3.pack()
        
    window.mainloop()

if __name__=="__main__":
    count=0
    first()
