import tkinter as tk
#from tkinter import *

w_main = tk.Tk()

#main window area
w_main.geometry('800x500+400+150')
w_main.title('КТСС')
w_main.resizable(False, False)
icon = tk.PhotoImage(file='./img/icon.png')
w_main.iconphoto(False, icon)

#label area
l_title = tk.Label(w_main, text='Калькулятор Тарифов Сотовой Связи', 
                   font=('Arial', 16, 'bold'), 
                   height='3',
                   bg='grey', fg='green')
l_title.pack()

#buttons area


#для дальнейшей работы
#w_main.config(bg='green')


w_main.mainloop()
