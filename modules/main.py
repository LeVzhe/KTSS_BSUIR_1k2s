import tkinter as tk
import tkinter.ttk as ttk
import b_click, constants

is_download = False

def on_click(event):
    
    item_id = t_main.identify_row(event.y)
    t_main.selection_set(item_id)
    t_main.focus(item_id)

    t_main.item(item_id, values=("New value 1", "New value 2"))
    t_main.bind('<Return>', save_edit)

def save_edit(event):
    item_id = t_main.focus() 
    values = [t_main.set(item_id, column) for column in t_main['columns']]
    print('Saved values:', values)

w_main = tk.Tk()
t_main = ttk.Treeview(columns=constants.t_col, show='headings')
main_menu = tk.Menu()
file_menu= tk.Menu(tearoff=0)



def download_data():
    global is_download
    if is_download:
        return
    b_click.download_on_click()
    is_download = True

def update_treeview(new_data):
    t_main.delete(*t_main.get_children())
    for el in new_data:
        t_main.insert("", "end", values=el)

def update_table():
    update_treeview(b_click.data_mass)

def delete_line():
    if t_main.focus() == '':
        return
    selected_item = t_main.selection()[0]
    t_main.delete(selected_item)

def open_edit_window():

    if t_main.focus() == '':
        return
    
    item_id = t_main.focus() 

    values = [t_main.set(item_id, column) for column in t_main['columns']]

    def edit_row():
        name = entry_name.get() or values[0]
        subscr = entry_subscr.get() or values[1]
        mins_in = entry_mins_in.get() or values[2]
        mins_out = entry_mins_out.get() or values[3]
        price_roum = entry_price_roum.get() or values[4]
        price_in = entry_price_in.get() or values[5]
        price_out = entry_price_out.get() or values[6]
        free_sms = entry_free_sms.get() or values[7]
        free_mms = entry_free_mms.get() or values[8]
        price_sms = entry_price_sms.get() or values[9]
        price_mms = entry_price_mms.get() or values[10]
        free_mb = entry_free_mb.get() or values[11]
        price_mb = entry_price_mb.get() or values[12]        
        
        t_main.item(item_id, values=(name, subscr, mins_in, mins_out, price_roum, price_in, price_out,
                                     free_sms, free_mms, price_sms, price_mms, free_mb, price_mb))
        new_window.destroy()   

    new_window = tk.Toplevel(w_main)
    new_window.title("Добавить тариф")
    new_window.geometry('750x120+400+300')
    new_window.resizable(False, False)
    new_window.focus_set()
    new_window.attributes("-topmost", True)
    label = tk.Label(new_window, text="Введите характеристики тарифного плана")
    label.grid(column='0', row='0', columnspan='13', sticky='wn', padx='4')

    entry_name = tk.Entry(new_window, width='19')
    entry_name.grid(column='1', row='2')
    label1 = tk.Label(new_window, text='Тариф')
    label1.grid(column='1', row='1')
    entry_subscr = tk.Entry(new_window, width='8')
    entry_subscr.grid(column='2', row='2')
    label2 = tk.Label(new_window, text='Аб.Пл')
    label2.grid(column='2', row='1')
    entry_mins_in = tk.Entry(new_window, width='8')
    entry_mins_in.grid(column='3', row='2')
    label3 = tk.Label(new_window, text='Мин.В')
    label3.grid(column='3', row='1')
    entry_mins_out = tk.Entry(new_window, width='8')
    entry_mins_out.grid(column='4', row='2')
    label4 = tk.Label(new_window, text='Мин.Др')
    label4.grid(column='4', row='1')
    entry_price_roum = tk.Entry(new_window, width='8')
    entry_price_roum.grid(column='5', row='2')
    label5 = tk.Label(new_window, text='Ст.Роу')
    label5.grid(column='5', row='1')
    entry_price_in = tk.Entry(new_window, width='8')
    entry_price_in.grid(column='6', row='2')
    label6 = tk.Label(new_window, text='Ст.Вн.с')
    label6.grid(column='6', row='1')
    entry_price_out = tk.Entry(new_window, width='8')
    entry_price_out.grid(column='7', row='2')
    label7 = tk.Label(new_window, text='Ст.Др.с')
    label7.grid(column='7', row='1')
    entry_free_sms = tk.Entry(new_window, width='8')
    entry_free_sms.grid(column='8', row='2')
    label8 = tk.Label(new_window, text='К.СМС')
    label8.grid(column='8', row='1')
    entry_free_mms = tk.Entry(new_window, width='8')
    entry_free_mms.grid(column='9', row='2')
    label9 = tk.Label(new_window, text='К.ММС')
    label9.grid(column='9', row='1')
    entry_price_sms = tk.Entry(new_window, width='8')
    entry_price_sms.grid(column='10', row='2')
    label10 = tk.Label(new_window, text='Ст.СМС')
    label10.grid(column='10', row='1')
    entry_price_mms = tk.Entry(new_window, width='8')
    entry_price_mms.grid(column='11', row='2')
    label11 = tk.Label(new_window, text='Ст.ММС')
    label11.grid(column='11', row='1')
    entry_free_mb = tk.Entry(new_window, width='9')
    entry_free_mb.grid(column='12', row='2')
    label12 = tk.Label(new_window, text='Кол.Мб')
    label12.grid(column='12', row='1')
    entry_price_mb = tk.Entry(new_window, width='8')
    entry_price_mb.grid(column='13', row='2')
    label13 = tk.Label(new_window, text='Ст.Мб')
    label13.grid(column='13', row='1') 
    
    button_add = tk.Button(new_window, text='Добавить', command=edit_row, width='10')
    button_exit = tk.Button(new_window, text='Выход', command=new_window.destroy, width='10')
    button_add.grid(column='10', row='3', pady='15', padx='10', columnspan='2', sticky='e')
    button_exit.grid(column='12', row='3', pady='15', padx='10', columnspan='2', sticky='w')

 


def open_fill_window():
    def add_row():
        name = entry_name.get()
        subscr = entry_subscr.get()
        mins_in = entry_mins_in.get()
        mins_out = entry_mins_out.get()
        price_roum = entry_price_roum.get()
        price_in = entry_price_in.get()
        price_out = entry_price_out.get()
        free_sms = entry_free_sms.get()
        free_mms = entry_free_mms.get()
        price_sms = entry_price_sms.get()
        price_mms = entry_price_mms.get()
        free_mb = entry_free_mb.get()
        price_mb = entry_price_mb.get()
        t_main.insert('', 'end', text=str(len(t_main.get_children()) + 1), values=(name, subscr, mins_in, mins_out, price_roum,
                                                                               price_in, price_out, free_sms, free_mms, price_sms,
                                                                               price_mms, free_mb, price_mb))
        new_window.destroy()
        

    new_window = tk.Toplevel(w_main)
    new_window.title("Добавить тариф")
    new_window.geometry('750x120+400+300')
    new_window.resizable(False, False)
    new_window.focus_set()
    new_window.attributes("-topmost", True)
    label = tk.Label(new_window, text="Введите характеристики тарифного плана")
    label.grid(column='0', row='0', columnspan='13', sticky='wn', padx='4')

    entry_name = tk.Entry(new_window, width='19')
    entry_name.grid(column='1', row='2')
    label1 = tk.Label(new_window, text='Тариф')
    label1.grid(column='1', row='1')
    entry_subscr = tk.Entry(new_window, width='8')
    entry_subscr.grid(column='2', row='2')
    label2 = tk.Label(new_window, text='Аб.Пл')
    label2.grid(column='2', row='1')
    entry_mins_in = tk.Entry(new_window, width='8')
    entry_mins_in.grid(column='3', row='2')
    label3 = tk.Label(new_window, text='Мин.В')
    label3.grid(column='3', row='1')
    entry_mins_out = tk.Entry(new_window, width='8')
    entry_mins_out.grid(column='4', row='2')
    label4 = tk.Label(new_window, text='Мин.Др')
    label4.grid(column='4', row='1')
    entry_price_roum = tk.Entry(new_window, width='8')
    entry_price_roum.grid(column='5', row='2')
    label5 = tk.Label(new_window, text='Ст.Роу')
    label5.grid(column='5', row='1')
    entry_price_in = tk.Entry(new_window, width='8')
    entry_price_in.grid(column='6', row='2')
    label6 = tk.Label(new_window, text='Ст.Вн.с')
    label6.grid(column='6', row='1')
    entry_price_out = tk.Entry(new_window, width='8')
    entry_price_out.grid(column='7', row='2')
    label7 = tk.Label(new_window, text='Ст.Др.с')
    label7.grid(column='7', row='1')
    entry_free_sms = tk.Entry(new_window, width='8')
    entry_free_sms.grid(column='8', row='2')
    label8 = tk.Label(new_window, text='К.СМС')
    label8.grid(column='8', row='1')
    entry_free_mms = tk.Entry(new_window, width='8')
    entry_free_mms.grid(column='9', row='2')
    label9 = tk.Label(new_window, text='К.ММС')
    label9.grid(column='9', row='1')
    entry_price_sms = tk.Entry(new_window, width='8')
    entry_price_sms.grid(column='10', row='2')
    label10 = tk.Label(new_window, text='Ст.СМС')
    label10.grid(column='10', row='1')
    entry_price_mms = tk.Entry(new_window, width='8')
    entry_price_mms.grid(column='11', row='2')
    label11 = tk.Label(new_window, text='Ст.ММС')
    label11.grid(column='11', row='1')
    entry_free_mb = tk.Entry(new_window, width='9')
    entry_free_mb.grid(column='12', row='2')
    label12 = tk.Label(new_window, text='Кол.Мб')
    label12.grid(column='12', row='1')
    entry_price_mb = tk.Entry(new_window, width='8')
    entry_price_mb.grid(column='13', row='2')
    label13 = tk.Label(new_window, text='Ст.Мб')
    label13.grid(column='13', row='1')

    button_add = tk.Button(new_window, text='Добавить', command=add_row, width='10')
    button_exit = tk.Button(new_window, text='Выход', command=new_window.destroy, width='10')
    button_add.grid(column='10', row='3', pady='15', padx='10', columnspan='2', sticky='e')
    button_exit.grid(column='12', row='3', pady='15', padx='10', columnspan='2', sticky='w')

def add_data():
    open_fill_window()

#MAIN WINDOW AREA
w_main.geometry('730x400+400+150')
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
file_menu.add_command(label='Загрузить список тарифов', command=download_data)
file_menu.add_command(label='Вывести список тарифов', command=update_table)
file_menu.add_command(label='Добавить тариф в список', command=add_data)
file_menu.add_command(label='Редактировать тариф', command=open_edit_window)
file_menu.add_command(label='Удалить тариф', command=delete_line)
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
t_main.heading('price_mms', text='Ст.ММС')
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
t_main.column('price_mms', width='50', minwidth='50')
t_main.column('free_mb', width='50', minwidth='50')
t_main.column('price_mb', width='50', minwidth='50')



t_main.grid(column='1', row='1', rowspan='3', sticky='esn', padx='4')

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
