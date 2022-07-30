import tkinter as tk

def say_hello():
    print('hello')

def add_label():
    label = tk.Label(win,text='new')
    label.pack()

def counter():
    global count
    count+=1
    btn4['text'] = f'Счетчик: {count}'
count = 0

win = tk.Tk()
win.title('Графическое окно 3')
win.geometry('500x600-10+10')

btn1 = tk.Button(win,text='Hello',
                command=say_hello)  # наделяет кнопку силой

btn2 = tk.Button(win,text='Add new label',
                command=add_label)

btn3 = tk.Button(win,text='Add new label lambda',
                command=lambda:tk.Label(win,text='new lambda').pack())

btn4 = tk.Button(win,text=f'Счетчик: {count}',
                command=counter,
                activebackground='blue',
                bg='red',
                state=tk.DISABLED)


btn1.pack()       #Метод pack выносит на экран      
btn2.pack()
btn3.pack() 
btn4.pack()
win.mainloop()