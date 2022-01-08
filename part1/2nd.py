import tkinter as tk

def first():
    window=tk.Tk()
    window.title("FIRST")
    window.geometry("500x650") 
    window.resizable(False, False)
    window.wm_attributes("-topmost", 1)
    window.config(bg='blue')
    label_1 = tk.Label(window,
text='''Hello
HIIIIII
SQL is cool!!!
Here we go''',
                       
bg='red',
fg='black', 
font=('Times New Roman', 20, 'bold'), 
width=30, 
height=10, 
anchor='nw',
padx=40,
pady=100, 
relief=tk.RAISED, 
bd=25,
justify=tk.LEFT  )                    

    label_1.pack()

    window.mainloop()

if __name__=="__main__":
    first()
