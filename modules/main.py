import tkinter as tk
import tkinter.ttk as ttk
import b_click, constants
from tkinter import messagebox as mb
import re

flag = False
is_download = False
is_view = False
is_saved = True
is_edit = False
test_mass = []

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

w_main = tk.Tk()
t_main = ttk.Treeview(columns=constants.t_col, show='headings')
main_menu = tk.Menu()
file_menu= tk.Menu(tearoff=0)

errmsg = tk.StringVar()

def valid_int(newval):
    return re.match("^\d{0,5}$", newval) is not None
check_int = (w_main.register(valid_int), "%P")

def valid_float(newval):
    return re.match("^(?:\d{1,8}(?:\.\d{0,2})?|\d{1,10})$", newval) is not None
check_float = (w_main.register(valid_float), "%P")

def valid_tarif_name(newval):
    return re.match("^[a-zA-Zа-яА-Я](?:[\d]|(?:[^a-zA-Zа-яА-Я]{0,2}[a-zA-Zа-яА-Я]?)){0,9}$", newval) is not None
check_tarif_name = (w_main.register(valid_tarif_name), "%P")

def download_data():
    global is_download
    global is_view
    global is_saved
    global is_edit
    global test_mass
    if is_download:
        return
    
    with open("./db/data.txt", "r") as db:
        if db == '':
            is_edit = False
            is_download = True
            is_view = False
            is_saved = True
            return
        mass = []
        lines = db.readlines()
        for line in lines:
            el = line.strip().split()
            el = [e for e in el]
            mass.append(el)
        test_mass = mass

    is_edit = False
    is_download = True
    is_view = False
    is_saved = True

def update_treeview(new_data):
    t_main.delete(*t_main.get_children())
    for el in new_data:
        t_main.insert('', "end", values=el)

def update_table():
    global is_download
    global is_view
    global is_saved
    global is_edit
    if is_download or is_edit:
        update_treeview(test_mass)
        is_download = True
        is_view = True
        is_edit = False
        is_saved = True
    else:
        mb.showerror('Ошибка', 'Загрузите данные')
        return

def delete_line():
    global is_saved
    global is_edit
    if t_main.focus() == '':
        mb.showerror('Ошибка', 'Выберите тариф')
        return
    is_edit = True
    is_saved = False
    selected_item = t_main.selection()[0]
    t_main.delete(selected_item)

def open_edit_window():
    global is_saved
    global is_edit
    global is_download
    if t_main.focus() == '':
        mb.showerror('Ошибка', 'Выберите тариф')
        return
    def on_entry_click(event, entry, el):
        if entry.get() == el:
            entry.delete(0, "end")
            entry.insert(0, '')


    def on_focusout(event, entry, el):
        if entry.get() == '':
            entry.insert(0, el)

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

        t_main.item(item_id, values=(name, subscr, mins_in, mins_out, price_roum, price_in , price_out,
                                     free_sms, free_mms, price_sms, price_mms, free_mb, price_mb))
        
    is_edit = True    
    is_saved = False
    is_download = False

    new_window = tk.Toplevel(w_main)
    new_window.title("Редактировать тариф")
    new_window.geometry('450x380+400+300')
    new_window.resizable(False, False)
    new_window.focus_set()
    new_window.attributes("-topmost", True)
    label = tk.Label(new_window, text="Введите характеристики тарифного плана:", font='Arial 14 bold')
    label.grid(column='0', row='0', columnspan='2', sticky='wn', padx='4')


    entry_name = tk.Entry(new_window, width='20', justify='right', validate='key', validatecommand=check_tarif_name)
    entry_name.bind('<FocusIn>', on_entry_click('', entry_name, values[0]))
    entry_name.bind('<FocusOut>', on_focusout('', entry_name, values[0]))
    entry_name.grid(column='1', row='1')
    label1 = tk.Label(new_window, text='Тариф')
    label1.grid(column='0', row='1', sticky='e')

    entry_subscr = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_subscr.grid(column='1', row='2')
    entry_subscr.bind('<FocusIn>', on_entry_click('', entry_subscr, values[1]))
    entry_subscr.bind('<FocusOut>', on_focusout('', entry_subscr, values[1]))
    label2 = tk.Label(new_window, text='Абонентская плата, руб.')
    label2.grid(column='0', row='2', sticky='e')

    entry_mins_in = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_mins_in.grid(column='1', row='3')
    entry_mins_in.bind('<FocusIn>', on_entry_click('', entry_mins_in, values[2]))
    entry_mins_in.bind('<FocusOut>', on_focusout('', entry_mins_in, values[2]))
    label3 = tk.Label(new_window, text='Минут внутри сети')
    label3.grid(column='0', row='3', sticky='e')

    entry_mins_out = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_mins_out.grid(column='1', row='4')
    entry_mins_out.bind('<FocusIn>', on_entry_click('', entry_mins_out, values[3]))
    entry_mins_out.bind('<FocusOut>', on_focusout('', entry_mins_out, values[3]))
    label4 = tk.Label(new_window, text='Минут в другие сети')
    label4.grid(column='0', row='4', sticky='e')

    entry_price_roum = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_roum.grid(column='1', row='5')
    entry_price_roum.bind('<FocusIn>', on_entry_click('', entry_price_roum, values[4]))
    entry_price_roum.bind('<FocusOut>', on_focusout('', entry_price_roum, values[4]))
    label5 = tk.Label(new_window, text='Стоимость роуминга, руб.')
    label5.grid(column='0', row='5', sticky='e')

    entry_price_in = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_in.grid(column='1', row='6')
    entry_price_in.bind('<FocusIn>', on_entry_click('', entry_price_in, values[5]))
    entry_price_in.bind('<FocusOut>', on_focusout('', entry_price_in, values[5]))
    label6 = tk.Label(new_window, text='Стоимость внутри сети, руб.')
    label6.grid(column='0', row='6', sticky='e')

    entry_price_out = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_out.grid(column='1', row='7')
    entry_price_out.bind('<FocusIn>', on_entry_click('', entry_price_out, values[6]))
    entry_price_out.bind('<FocusOut>', on_focusout('', entry_price_out, values[6]))
    label7 = tk.Label(new_window, text='Стоимость на другие сети, руб.')
    label7.grid(column='0', row='7', sticky='e')

    entry_free_sms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_free_sms.grid(column='1', row='8')
    entry_free_sms.bind('<FocusIn>', on_entry_click('', entry_free_sms, values[7]))
    entry_free_sms.bind('<FocusOut>', on_focusout('', entry_free_sms, values[7]))
    label8 = tk.Label(new_window, text='Количество СМС')
    label8.grid(column='0', row='8', sticky='e')

    entry_free_mms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_free_mms.grid(column='1', row='9')
    entry_free_mms.bind('<FocusIn>', on_entry_click('', entry_free_mms, values[8]))
    entry_free_mms.bind('<FocusOut>', on_focusout('', entry_free_mms, values[8]))
    label9 = tk.Label(new_window, text='Количество ММС')
    label9.grid(column='0', row='9', sticky='e')

    entry_price_sms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_sms.grid(column='1', row='10')
    entry_price_sms.bind('<FocusIn>', on_entry_click('', entry_price_sms, values[9]))
    entry_price_sms.bind('<FocusOut>', on_focusout('', entry_price_sms, values[9]))
    label10 = tk.Label(new_window, text='Стоимость СМС, руб.')
    label10.grid(column='0', row='10', sticky='e')

    entry_price_mms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_mms.grid(column='1', row='11')
    entry_price_mms.bind('<FocusIn>', on_entry_click('', entry_price_mms, values[10]))
    entry_price_mms.bind('<FocusOut>', on_focusout('', entry_price_mms, values[10]))
    label11 = tk.Label(new_window, text='Стоимость ММС, руб.')
    label11.grid(column='0', row='11', sticky='e')

    entry_free_mb = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_free_mb.grid(column='1', row='12')
    entry_free_mb.bind('<FocusIn>', on_entry_click('', entry_free_mb, values[11]))
    entry_free_mb.bind('<FocusOut>', on_focusout('', entry_free_mb, values[11]))
    label12 = tk.Label(new_window, text='Количество Мегабайт')
    label12.grid(column='0', row='12', sticky='e')

    entry_price_mb = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_mb.grid(column='1', row='13')
    entry_price_mb.bind('<FocusIn>', on_entry_click('', entry_price_mb, values[12]))
    entry_price_mb.bind('<FocusOut>', on_focusout('', entry_price_mb, values[12]))
    label13 = tk.Label(new_window, text='Стоимость Мегабайт, руб.')
    label13.grid(column='0', row='13', sticky='e') 
    
    button_add = tk.Button(new_window, text='Изменить', command=edit_row, width='10')
    button_exit = tk.Button(new_window, text='Выход', command=new_window.destroy, width='10')
    button_add.grid(column='0', row='14', pady='15', padx='10', sticky='e')
    button_exit.grid(column='1', row='14', pady='15', padx='10', sticky='w')

def open_fill_window():
    global is_edit
    if not is_view:
        mb.showerror('Ошибка', 'Выведите данные')
        return
    
    def show_modal_error():
        modal_error_window = tk.Toplevel(new_window)
        modal_error_window.geometry('200x100+400+300')
        modal_error_window.resizable(False, False)
        modal_error_window.title("Ошибка")
        modal_error_window.transient(new_window)
        modal_error_window.grab_set()
        def close_modal_error():
            modal_error_window.destroy()
        
        error_label = tk.Label(modal_error_window, text="Есть пустые поля")
        error_label.pack(padx=20, pady=10)

        ok_button = tk.Button(modal_error_window, text="OK", command=close_modal_error, width='10', height='2')
        ok_button.pack(pady=10)

        modal_error_window.wait_window()

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
        if (name=='' or subscr=='' or mins_in=='' or mins_out=='' or price_roum=='' or 
        price_in=='' or price_in=='' or price_out=='' or free_sms=='' or free_mms=='' or 
        price_sms=='' or price_mms=='' or free_mb=='' or price_mb==''):
            show_modal_error()
        else:
            t_main.insert('', 'end', text=str(len(t_main.get_children()) + 1), values=(name, subscr, mins_in, mins_out, price_roum,
                                                                               price_in, price_out, free_sms, free_mms, price_sms,
                                                                               price_mms, free_mb, price_mb))
            new_window.destroy()
        

    new_window = tk.Toplevel(w_main)
    new_window.title("Добавить тариф")
    new_window.geometry('570x380+200+100')
    new_window.resizable(False, False)
    new_window.focus_set()
    new_window.attributes("-topmost", True)
    label = tk.Label(new_window, text="Введите характеристики тарифного плана:", font='Arial 14 bold')
    label.grid(column='0', row='0', columnspan='2', sticky='wn', padx='4')

    entry_name = tk.Entry(new_window, width='20', justify='right', validate='key', validatecommand=check_tarif_name)
    entry_name.grid(column='1', row='1')
    label1 = tk.Label(new_window, text='Тариф')
    label1.grid(column='0', row='1', sticky='e')

    entry_subscr = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_subscr.grid(column='1', row='2')
    label2 = tk.Label(new_window, text='Абонентская плата, руб.')
    label2.grid(column='0', row='2', sticky='e')

    entry_mins_in = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_mins_in.grid(column='1', row='3')
    label3 = tk.Label(new_window, text='Мин внутри сети')
    label3.grid(column='0', row='3', sticky='e')
    
    entry_mins_out = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_mins_out.grid(column='1', row='4')
    label4 = tk.Label(new_window, text='Минут на другие сети')
    label4.grid(column='0', row='4', sticky='e')
    
    entry_price_roum = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_roum.grid(column='1', row='5')
    label5 = tk.Label(new_window, text='Стоимость роуминга, руб.')
    label5.grid(column='0', row='5', sticky='e')
    
    entry_price_in = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_in.grid(column='1', row='6')
    label6 = tk.Label(new_window, text='Стоимость внутри сети, руб.')
    label6.grid(column='0', row='6', sticky='e')
    
    entry_price_out = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_out.grid(column='1', row='7')
    label7 = tk.Label(new_window, text='Стоимость на другие сети, руб.')
    label7.grid(column='0', row='7', sticky='e')
    
    entry_free_sms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_free_sms.grid(column='1', row='8')
    label8 = tk.Label(new_window, text='Количество СМС')
    label8.grid(column='0', row='8', sticky='e')
    
    entry_free_mms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_free_mms.grid(column='1', row='9')
    label9 = tk.Label(new_window, text='Количество ММС')
    label9.grid(column='0', row='9', sticky='e')
    
    entry_price_sms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_sms.grid(column='1', row='10')
    label10 = tk.Label(new_window, text='Стоимость СМС, руб.')
    label10.grid(column='0', row='10', sticky='e')
    
    entry_price_mms = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_mms.grid(column='1', row='11')
    label11 = tk.Label(new_window, text='Стоимость ММС, руб.')
    label11.grid(column='0', row='11', sticky='e')
    
    entry_free_mb = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_int)
    entry_free_mb.grid(column='1', row='12')
    label12 = tk.Label(new_window, text='Количество Мегабайт')
    label12.grid(column='0', row='12', sticky='e')
    
    entry_price_mb = tk.Entry(new_window, width='20', justify='right', validate="key", validatecommand=check_float)
    entry_price_mb.grid(column='1', row='13')
    label13 = tk.Label(new_window, text='Стоимость Мегабайт, руб.')
    label13.grid(column='0', row='13', sticky='e')

    button_add = tk.Button(new_window, text='Добавить', command=add_row, width='10')
    button_exit = tk.Button(new_window, text='Выход', command=new_window.destroy, width='10')
    button_add.grid(column='0', row='14', pady='15', padx='10', sticky='e')
    button_exit.grid(column='1', row='14', pady='15', padx='10', sticky='w')
    is_edit = True

def add_data():
    global is_saved
    global is_download
    open_fill_window()
    is_saved = False

    is_download = False

def save_data():
    global is_view
    global is_saved
    global is_download
    global is_edit
    if not is_view:
        mb.showerror('Ошибка', 'Выведите данные')
        return
    else:
        is_download = False
        is_view = True
        is_saved = True
        is_edit = False
        def get_treeview_data(tree):
            data = []
            for child in tree.get_children():
                item = tree.item(child)
                values = item["values"]
                data.append(values)
            return data
        saved_data = get_treeview_data(t_main)
        with open("./db/data.txt", "w") as file:
            for line in saved_data:
                line_as_str = [str(item) for item in line] 
                file.write(' '.join(line_as_str) + '\n')

def remove_arrow(text):
    if "\u2191" in text:
        return text.replace("\u2191", "")
    if "\u2193" in text:
        return text.replace("\u2193", "")
    return text

def sort_int(col, reverse, name):
    arrow = "\u2191" if reverse else "\u2193"

    for col_id in t_main["columns"]:
        heading_text = t_main.heading(col_id)["text"]
        t_main.heading(col_id, text=remove_arrow(heading_text))

    t_main.heading(col, text=f"{name} {arrow}")
    
    data = [(int(t_main.set(k, col)), k) for k in t_main.get_children("")]
    data.sort(reverse=reverse)
    for index, (_, k) in enumerate(data):
        t_main.move(k, "", index)
    
    t_main.heading(col, command=lambda: sort_int(col, not reverse, name))
    
    data = [(int(t_main.set(k, col)), k) for k in t_main.get_children("")]
    data.sort(reverse=reverse)
    for index, (_, k) in enumerate(data):
        t_main.move(k, "", index)

    t_main.heading(col, command=lambda: sort_int(col, not reverse, name))

def sort_float(col, reverse, name):
    arrow = "\u2191" if reverse else "\u2193"

    for col_id in t_main["columns"]:
        heading_text = t_main.heading(col_id)["text"]
        t_main.heading(col_id, text=remove_arrow(heading_text))

    t_main.heading(col, text=f"{name} {arrow}")
    
    data = [(float(t_main.set(k, col)), k) for k in t_main.get_children("")]
    data.sort(reverse=reverse)
    for index, (_, k) in enumerate(data):
        t_main.move(k, "", index)

    t_main.heading(col, command=lambda: sort_float(col, not reverse, name))
    
    data = [(int(t_main.set(k, col)), k) for k in t_main.get_children("")]
    data.sort(reverse=reverse)
    for index, (_, k) in enumerate(data):
        t_main.move(k, "", index)

    t_main.heading(col, command=lambda: sort_float(col, not reverse, name))

def sort(col, reverse, name):
    arrow = "\u2191" if reverse else "\u2193"

    for col_id in t_main["columns"]:
        heading_text = t_main.heading(col_id)["text"]
        t_main.heading(col_id, text=remove_arrow(heading_text))

    t_main.heading(col, text=f"{name} {arrow}")
    
    data = [(t_main.set(k, col), k) for k in t_main.get_children("")]
    data.sort(reverse=reverse)
    for index, (_, k) in enumerate(data):
        t_main.move(k, "", index)

    t_main.heading(col, command=lambda: sort(col, not reverse, name))
    
    data = [(t_main.set(k, col), k) for k in t_main.get_children("")]
    data.sort(reverse=reverse)
    for index, (_, k) in enumerate(data):
        t_main.move(k, "", index)

    t_main.heading(col, command=lambda: sort(col, not reverse, name))

#MAIN WINDOW AREA
w_main.geometry('1330x400+100+150')
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
file_menu.add_command(label='Сохранить список тарифов', command=save_data)
file_menu.add_command(label='Удалить тариф', command=delete_line)
file_menu.add_separator()
file_menu.add_command(label="Выйти", command=quit)

w_main.config(menu=main_menu)

#TABLE AREA
t_main.heading('name', text='Тариф', command=lambda: sort(0, False, 'Тариф'))
t_main.heading('subscr', text='Абон. Пл.', command=lambda: sort_float(1, False, 'Абон. Пл.'))
t_main.heading('mins_in', text='Мин. Вн. С.', command=lambda: sort_int(2, False, 'Мин. Вн. С.'))
t_main.heading('mins_out', text='Мин. Др. С.', command=lambda: sort_int(3, False, 'Мин. Др. С.'))
t_main.heading('price_roum', text='Ст. Роум.', command=lambda: sort_float(4, False, 'Ст. Роум.'))
t_main.heading('price_in', text='Ст. Вн. С.', command=lambda: sort_float(5, False, 'Ст. Вн. С.'))
t_main.heading('price_out', text='Ст. Др. С.', command=lambda: sort_float(6, False, 'Ст. Др. С.'))
t_main.heading('free_sms', text='Кол. СМС', command=lambda: sort_int(7, False, 'Кол. СМС'))
t_main.heading('free_mms', text='Кол. ММС', command=lambda: sort_int(8, False, 'Кол. ММС'))
t_main.heading('price_sms', text='Ст. СМС', command=lambda: sort_float(9, False, 'Ст. СМС'))
t_main.heading('price_mms', text='Ст. ММС', command=lambda: sort_float(10, False, 'Ст. ММС'))
t_main.heading('free_mb', text='Кол. Мб', command=lambda: sort_int(11, False, 'Кол. Мб'))
t_main.heading('price_mb', text='Ст. Мб', command=lambda: sort_float(12, False, 'Ст. Мб'))

t_main.column('name', width='100', minwidth='100')
t_main.column('subscr', width='100', minwidth='50')
t_main.column('mins_in', width='100', minwidth='50')
t_main.column('mins_out', width='100', minwidth='50')
t_main.column('price_roum', width='100', minwidth='50')
t_main.column('price_in', width='100', minwidth='50')
t_main.column('price_out', width='100', minwidth='50')
t_main.column('free_sms', width='100', minwidth='50')
t_main.column('free_mms', width='100', minwidth='50')
t_main.column('price_sms', width='100', minwidth='50')
t_main.column('price_mms', width='100', minwidth='50')
t_main.column('free_mb', width='100', minwidth='50')
t_main.column('price_mb', width='100', minwidth='50')

t_main.grid(column='1', row='1', rowspan='3', sticky='esn', padx='4')

scrollbar = ttk.Scrollbar(orient='vertical', command=t_main.yview)
t_main.configure(yscroll=scrollbar.set)
scrollbar.grid(row='1', column='6', sticky="nsw",rowspan='3')
def prevent_resize(event):
    if t_main.identify_region(event.x, event.y) == "separator":
        return "break"
t_main.bind('<Button-1>', prevent_resize)
t_main.bind('<Motion>', prevent_resize)

w_main.mainloop()
