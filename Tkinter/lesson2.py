import tkinter as tk

win = tk.Tk()
win.title('Графическое окно 2')
win.geometry('500x600-10+10')

label_1 = tk.Label(win, text='''Hello!
world''',           
                    bg='red',                        #Цвет фона
                    fg='white',                      #Цвет шрифта
                    font=('Ariak',  15, 'bold'),      # Шрифт, размер, (обычный,жирный,наклонный и тд.)
                    padx=20,                         #Отступ по X
                    pady = 40,                        #Отступ по Y
                    width=20,                         # Ширина и высоста лейбла по кол-ву знаков
                    height=10,
                    anchor = 'sw',                      #Место текста на лейбле (стороны света)
                    relief=tk.RAISED,                   #Позволяет увидеть границы лейбла 
                    bd = 10,                             # Ширина границ
                    justify=tk.RIGHT               #Отвтечает за выравнивание значения (Левая часть, центр, правая)
                    )            
label_1.pack()


win.mainloop()