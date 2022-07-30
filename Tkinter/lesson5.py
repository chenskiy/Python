import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(0, tk.END)

win = tk.Tk()
win.title('Графическое окно 5')        
win.geometry('500x600-10+10')  
name = tk.Entry(win)
name.grid(row=0,column=1)
tk.Label(win,text='Имя').grid(row=0,column=0,stick='w')

tk.Button(win,text='get',command=get_entry).grid(row=1,column=0,stick='we')
tk.Button(win,text='delete',command=delete_entry).grid(row=1,column=1,stick='we')


win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()