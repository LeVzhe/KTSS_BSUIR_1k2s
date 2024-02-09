import tkinter as tk
#from tkinter import *

w_main = tk.Tk()


w_main.geometry('800x500+400+150')
w_main.title('КТСС')
w_main.resizable(False, False)
icon = tk.PhotoImage(file='./img/icon.png')
w_main.iconphoto(False, icon)

#для дальнейшей работы
#w_main.config(bg='green')


w_main.mainloop()
