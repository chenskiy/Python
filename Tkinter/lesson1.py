import tkinter as tk

win = tk.Tk()
win.title('Графическое окно 1')          # Имя окна
win.geometry('500x600-10+10')            # Размер и Отступы
photo = tk.PhotoImage(file='Calc.png')   
win.iconphoto(False, photo) 
# win.config(bg='red')
win.minsize(300,400)
win.maxsize(700,800)
win.resizable(True,True)                  
win.mainloop()
