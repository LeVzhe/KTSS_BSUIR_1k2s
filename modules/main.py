import tkinter as tk
import tkinter.ttk as ttk
import b_click

w_main = tk.Tk()

#MAIN WINDOW AREA
w_main.geometry('1020x500+400+150')
w_main.title('КТСС')
w_main.resizable(False, False)
icon = tk.PhotoImage(file='./img/icon.png')
w_main.iconphoto(False, icon)

#LABEL AREA
l_title = tk.Label(w_main, text='Калькулятор Тарифов Сотовой Связи', 
                   font=('Arial', 16, 'bold'), 
                   height='3', fg='green')
l_title.grid(columnspan='2', row=0)


#BUTTONS AREA
#--left-side-buttons
b_download = tk.Button(w_main, text='Загрузка данных', 
                       height='4', width='25', font=('arial', 12), 
                       command=b_click.download_on_click)
b_download.grid(row=1, column=0, padx='10',pady='5', sticky='wn')

b_open_list = tk.Button(w_main, text='Открыть список', 
                        height='4', width='25', font=('arial', 12), 
                        command=b_click.opn_l_on_click)
b_open_list.grid(row=1, column=1, padx='10',pady='5', sticky='wn')

b_sort = tk.Button(w_main, text='Сортировать тариф', 
                   height='4', width='25', font=('arial', 12), 
                   command=b_click.sort_on_click)
b_sort.grid(row=2, column=0, padx='10',pady='5', sticky='wn')

b_search = tk.Button(w_main, text='Найти тариф', 
                     height='4', width='25', font=('arial', 12), 
                     command=b_click.search_on_click)
b_search.grid(row=2, column=1, padx='10',pady='5', sticky='wn')

b_edit = tk.Button(w_main, text='Редактировать тариф', 
                   height='4', width='25', font=('arial', 12), 
                   command=b_click.edit_on_click)
b_edit.grid(row=3, column=0, padx='10',pady='5', sticky='wn')

b_add = tk.Button(w_main, text='Добавить тариф', 
                  height='4', width='25', font=('arial', 12), 
                  command=b_click.add_on_click)
b_add.grid(row=3, column=1, padx='10',pady='5', sticky='wn')

b_delete = tk.Button(w_main, text='Удалить тариф', 
                     height='4', width='25', 
                     bg='red', fg='white', font=('arial', 12), 
                     command=b_click.delete_on_click)
b_delete.grid(row=4, column=0, padx='10',pady='5', sticky='wn')

b_save = tk.Button(w_main, text='Сохранить', 
                   height='4', width='25', 
                   bg='lightgreen', font=('arial', 12), 
                   command=b_click.save_on_click)
b_save.grid(row=4, column=1, padx='10',pady='5', sticky='wn')

#--under-table-buttons
b_add_in_list = tk.Button(w_main, text='Добавить', 
                   height='4', width='13', 
                   bg='lightgreen', font=('arial', 12), 
                   command=b_click.add_in_list_on_click)
b_add_in_list.grid(row=4, column=2, padx='5',pady='5', sticky='wn')
b_add_in_list.config(state='disabled')

b_edit_in_list = tk.Button(w_main, text='Редактировать', 
                   height='4', width='13', 
                   bg='lightgreen', font=('arial', 12), 
                   command=b_click.edit_in_list_on_click)
b_edit_in_list.grid(row=4, column=3, padx='5',pady='5', sticky='wn')
b_edit_in_list.config(state='disabled')

b_delete_in_list = tk.Button(w_main, text='Удалить', 
                   height='4', width='13', 
                   bg='lightgreen', font=('arial', 12), 
                   command=b_click.delete_in_list_on_click)
b_delete_in_list.grid(row=4, column=4, padx='5',pady='5', sticky='wn')
b_delete_in_list.config(state='disabled')

b_help = tk.Button(w_main, text='=?=', 
                   height='3', width='5', 
                   bg='lightgreen', font=('arial', 12), 
                   command=b_click.help_on_click)
b_help.grid(row=4, column=5, padx='5',pady='5', sticky='wn')


#TABLE AREA
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
t_main.grid(column='2', row='1', rowspan='3', columnspan='4', sticky='esn')

t_main.heading('text', text='Text')
t_main.column('text', width='80')
t_main.heading('digits', text='Digit')
t_main.column('digits')
t_main.heading('mail', text='Mail')
t_main.column('mail', stretch=False, )

for el in t_data:
    t_main.insert("", 'end', values=el)

scrollbar = ttk.Scrollbar(orient='vertical', command=t_main.yview)
t_main.configure(yscroll=scrollbar.set)
scrollbar.grid(row='1', column='6', sticky="nsw",rowspan='3')

w_main.mainloop()
