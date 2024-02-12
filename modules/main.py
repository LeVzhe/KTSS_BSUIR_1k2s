import tkinter as tk
import tkinter.ttk as ttk
import b_click, constants

is_download = False

w_main = tk.Tk()
t_main = ttk.Treeview(columns=constants.t_col, show='headings')
main_menu = tk.Menu()
file_menu= tk.Menu(tearoff=0)

def update_treeview(new_data):
    t_main.delete(*t_main.get_children())
    for el in new_data:
        t_main.insert("", "end", values=el)

def update_table():
    update_treeview(b_click.data_mass)

#MAIN WINDOW AREA
w_main.geometry('720x500+400+150')
w_main.title('КТСС')
w_main.resizable(False, False)
icon = tk.PhotoImage(file='./img/icon.png')
w_main.iconphoto(False, icon)
w_main.config(background='lightgrey')

w_main.option_add("*tearOff", False)

#LABEL AREA
l_title = tk.Label(w_main, text='Калькулятор Тарифов Сотовой Связи', 
                   font=('Arial', 16, 'bold'), 
                   height='3', fg='green', bg='lightgrey')
l_title.grid(columnspan='2', row=0)

#MAIN MENU AREA
main_menu.add_cascade(label="Инструменты", menu=file_menu)
file_menu.add_command(label='Загрузить данные', command=b_click.download_on_click(is_download))
file_menu.add_command(label='Вывести данные', command=update_table)
file_menu.add_separator()
file_menu.add_command(label="Выйти", command=quit)



w_main.config(menu=main_menu)

#TABLE AREA
t_main.heading('name', text='Тариф')
t_main.heading('mins_in', text='Мин.Вн.С.')
t_main.heading('mins_out', text='Мин.Др.С.')
t_main.heading('price_roum', text='Ст.Роум.')
t_main.heading('price_in', text='Ст.Вн.с')
t_main.heading('free_sms', text='Кол.СМС')
t_main.heading('free_mms', text='Кол.ММС')
t_main.heading('price_sms', text='Ст.СМС')
t_main.heading('Price_mms', text='Ст.ММС')
t_main.heading('free_mb', text='Кол.Мб')
t_main.heading('price_mb', text='Ст.Мб')
t_main.heading('price_out', text='Ст.Др.с')
t_main.heading('subscr', text='Абон.Пл.')

t_main.column('name', width='100', minwidth='100')
t_main.column('subscr', width='50', minwidth='50')
t_main.column('mins_in', width='50', minwidth='50')
t_main.column('mins_out', width='50', minwidth='50')
t_main.column('price_roum', width='50', minwidth='50')
t_main.column('price_in', width='50', minwidth='50')
t_main.column('price_out', width='50', minwidth='50')
t_main.column('free_sms', width='50', minwidth='50')
t_main.column('free_mms', width='50', minwidth='50')
t_main.column('price_sms', width='50', minwidth='50')
t_main.column('Price_mms', width='50', minwidth='50')
t_main.column('free_mb', width='50', minwidth='50')
t_main.column('price_mb', width='50', minwidth='50')

t_main.grid(column='1', row='1', rowspan='3', sticky='esn')

#####
scrollbar = ttk.Scrollbar(orient='vertical', command=t_main.yview)
t_main.configure(yscroll=scrollbar.set)
scrollbar.grid(row='1', column='6', sticky="nsw",rowspan='3')
def prevent_resize(event):
    if t_main.identify_region(event.x, event.y) == "separator":
        return "break"
t_main.bind('<Button-1>', prevent_resize)
t_main.bind('<Motion>', prevent_resize)
##№№№


w_main.mainloop()
