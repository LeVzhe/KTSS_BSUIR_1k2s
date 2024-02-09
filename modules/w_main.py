import tkinter as tk
import tkinter.ttk as ttk
#from tkinter import *

w_main = tk.Tk()

#main window area
w_main.geometry('1020x500+400+150')
w_main.title('КТСС')
w_main.resizable(False, False)
icon = tk.PhotoImage(file='./img/icon.png')
w_main.iconphoto(False, icon)

#label area
l_title = tk.Label(w_main, text='Калькулятор Тарифов Сотовой Связи', 
                   font=('Arial', 16, 'bold'), 
                   height='3', fg='green')
l_title.grid(columnspan='2', row=0)

#buttons area
def test():
    print('test')

#--buttons   
for r in range(4):
    for c in range(2):
        btn = tk.Button(w_main, text=f"({r},{c})", 
                        height='4', width='25',
                        command=test)
        btn.grid(row=r+1, column=c, 
                 padx='10',pady='5', 
                 sticky='wn')

#table area
t_col = ("text", "digits", "mail")
t_data = [('text 11', 11, '11@mail'),
          ('text 22', 22, '22@mail'),
          ('text 33', 33, '33@mail'),
          ('text 11', 11, '11@mail'),
          ('text 22', 22, '22@mail'),
          ('text 33', 33, '33@mail'),
          ('text 11', 11, '11@mail'),
          ('text 22', 22, '22@mail'),
          ('text 33', 33, '33@mail'),
          ('text 11', 11, '11@mail'),
          ('text 22', 22, '22@mail'),
          ('text 33', 33, '33@mail'),
          ('text 11', 11, '11@mail'),
          ('text 22', 22, '22@mail'),
          ('text 33', 33, '33@mail'),]

t_main = ttk.Treeview(columns=t_col, show='headings')
t_main.grid(column='2', row='1', rowspan='4', columnspan='4', sticky='esn')

t_main.heading('text', text='Text')
t_main.column('text', width='150')
t_main.heading('digits', text='Digit')
t_main.column('digits')
t_main.heading('mail', text='Mail')
t_main.column('mail', stretch=False, )

for el in t_data:
    t_main.insert("", 'end', values=el)

scrollbar = ttk.Scrollbar(orient='vertical', command=t_main.yview)
t_main.configure(yscroll=scrollbar.set)
scrollbar.grid(row='1', column='6', sticky="nsw",rowspan='4')
#scrollbar.place(height=1000)
#для дальнейшей работы
#w_main.config(bg='green')


w_main.mainloop()
