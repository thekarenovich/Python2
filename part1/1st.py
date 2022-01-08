import tkinter as tk

def first():
    
    window=tk.Tk()
    window.title("FIRST")
    window.geometry("500x300+400+250") 
    window.resizable(False, False)
    window.wm_attributes("-topmost", 1) #поверх других окон
    #window.minsize(300, 150)
    #window.maxsize(500, 300)

    window.mainloop()

if __name__=="__main__":
    first()
