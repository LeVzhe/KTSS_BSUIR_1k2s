import tkinter as tk
import tkinter.ttk as ttk
import b_click, constants
from tkinter import messagebox as mb

flag = False
is_download = False

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
        if len(name) > 10:
            name = values[0]
            open_edit_window()
        subscr = entry_subscr.get() or values[1]
        if (len(subscr) > 5) or (not is_number(subscr)):
            subscr = values[1]
            open_edit_window()
        mins_in = entry_mins_in.get() or values[2]
        if (len(mins_in) > 5) or (not is_int(mins_in)):
            mins_in = values[2]
            open_edit_window()
        mins_out = entry_mins_out.get() or values[3]
        if (len(mins_out) > 5) or (not is_int(mins_out)):
            mins_out = values[3]
            open_edit_window()
        price_roum = entry_price_roum.get() or values[4]
        if (len(price_roum) > 5) or (not is_number(price_roum)):
            price_roum = values[4]
            open_edit_window()
        price_in = entry_price_in.get() or values[5]
        if (len(price_in) > 5) or (not is_number(price_in)):
            price_in = values[5]
            open_edit_window()
        price_out = entry_price_out.get() or values[6]
        if (len(price_out) > 5) or (not is_number(price_out)):
            price_out = values[6]
            open_edit_window()
        free_sms = entry_free_sms.get() or values[7]
        if (len(free_sms) > 5) or (not is_int(free_sms)):
            free_sms = values[7]
            open_edit_window()
        free_mms = entry_free_mms.get() or values[8]
        if (len(free_mms) > 5) or (not is_int(free_mms)):
            free_mms = values[8]
            open_edit_window()
        price_sms = entry_price_sms.get() or values[9]
        if (len(price_sms) > 5) or (not is_number(price_sms)):
            price_sms = values[9]
            open_edit_window()
        price_mms = entry_price_mms.get() or values[10]
        if (len(price_mms) > 5) or (not is_number(price_mms)):
            price_mms = values[10]
            open_edit_window()
        free_mb = entry_free_mb.get() or values[11]
        if (len(free_mb) > 5) or (not is_int(free_mb)):
            free_mb = values[11]
            open_edit_window()
        price_mb = entry_price_mb.get() or values[12]
        if (len(price_mb) > 5) or (not is_number(price_mb)):
            price_mb = values[12]
            open_edit_window()
        
        t_main.item(item_id, values=(name, subscr, mins_in, mins_out, price_roum, price_in , price_out,
                                     free_sms, free_mms, price_sms, price_mms, free_mb, price_mb))
           

    new_window = tk.Toplevel(w_main)
    new_window.title("Редактировать тариф")
    new_window.geometry('450x380+400+300')
    new_window.resizable(False, False)
    new_window.focus_set()
    new_window.attributes("-topmost", True)
    label = tk.Label(new_window, text="Введите характеристики тарифного плана:", font='Arial 14 bold')
    label.grid(column='0', row='0', columnspan='2', sticky='wn', padx='4')


    entry_name = tk.Entry(new_window, width='20', justify='right')
    entry_name.bind('<FocusIn>', on_entry_click('', entry_name, values[0]))
    entry_name.bind('<FocusOut>', on_focusout('', entry_name, values[0]))
    entry_name.grid(column='1', row='1')
    label1 = tk.Label(new_window, text='Тариф')
    label1.grid(column='0', row='1', sticky='e')
    entry_subscr = tk.Entry(new_window, width='20', justify='right')
    entry_subscr.grid(column='1', row='2')
    entry_subscr.bind('<FocusIn>', on_entry_click('', entry_subscr, values[1]))
    entry_subscr.bind('<FocusOut>', on_focusout('', entry_subscr, values[1]))
    label2 = tk.Label(new_window, text='Абонентская плата, руб.')
    label2.grid(column='0', row='2', sticky='e')
    entry_mins_in = tk.Entry(new_window, width='20', justify='right')
    entry_mins_in.grid(column='1', row='3')
    entry_mins_in.bind('<FocusIn>', on_entry_click('', entry_mins_in, values[2]))
    entry_mins_in.bind('<FocusOut>', on_focusout('', entry_mins_in, values[2]))
    label3 = tk.Label(new_window, text='Минут внутри сети')
    label3.grid(column='0', row='3', sticky='e')
    entry_mins_out = tk.Entry(new_window, width='20', justify='right')
    entry_mins_out.grid(column='1', row='4')
    entry_mins_out.bind('<FocusIn>', on_entry_click('', entry_mins_out, values[3]))
    entry_mins_out.bind('<FocusOut>', on_focusout('', entry_mins_out, values[3]))
    label4 = tk.Label(new_window, text='Минут в другие сети')
    label4.grid(column='0', row='4', sticky='e')
    entry_price_roum = tk.Entry(new_window, width='20', justify='right')
    entry_price_roum.grid(column='1', row='5')
    entry_price_roum.bind('<FocusIn>', on_entry_click('', entry_price_roum, values[4]))
    entry_price_roum.bind('<FocusOut>', on_focusout('', entry_price_roum, values[4]))
    label5 = tk.Label(new_window, text='Стоимость роуминга, руб.')
    label5.grid(column='0', row='5', sticky='e')
    entry_price_in = tk.Entry(new_window, width='20', justify='right')
    entry_price_in.grid(column='1', row='6')
    entry_price_in.bind('<FocusIn>', on_entry_click('', entry_price_in, values[5]))
    entry_price_in.bind('<FocusOut>', on_focusout('', entry_price_in, values[5]))
    label6 = tk.Label(new_window, text='Стоимость внутри сети, руб.')
    label6.grid(column='0', row='6', sticky='e')
    entry_price_out = tk.Entry(new_window, width='20', justify='right')
    entry_price_out.grid(column='1', row='7')
    entry_price_out.bind('<FocusIn>', on_entry_click('', entry_price_out, values[6]))
    entry_price_out.bind('<FocusOut>', on_focusout('', entry_price_out, values[6]))
    label7 = tk.Label(new_window, text='Стоимость на другие сети, руб.')
    label7.grid(column='0', row='7', sticky='e')
    entry_free_sms = tk.Entry(new_window, width='20', justify='right')
    entry_free_sms.grid(column='1', row='8')
    entry_free_sms.bind('<FocusIn>', on_entry_click('', entry_free_sms, values[7]))
    entry_free_sms.bind('<FocusOut>', on_focusout('', entry_free_sms, values[7]))
    label8 = tk.Label(new_window, text='Количество СМС')
    label8.grid(column='0', row='8', sticky='e')
    entry_free_mms = tk.Entry(new_window, width='20', justify='right')
    entry_free_mms.grid(column='1', row='9')
    entry_free_mms.bind('<FocusIn>', on_entry_click('', entry_free_mms, values[8]))
    entry_free_mms.bind('<FocusOut>', on_focusout('', entry_free_mms, values[8]))
    label9 = tk.Label(new_window, text='Количество ММС')
    label9.grid(column='0', row='9', sticky='e')
    entry_price_sms = tk.Entry(new_window, width='20', justify='right')
    entry_price_sms.grid(column='1', row='10')
    entry_price_sms.bind('<FocusIn>', on_entry_click('', entry_price_sms, values[9]))
    entry_price_sms.bind('<FocusOut>', on_focusout('', entry_price_sms, values[9]))
    label10 = tk.Label(new_window, text='Стоимость СМС, руб.')
    label10.grid(column='0', row='10', sticky='e')
    entry_price_mms = tk.Entry(new_window, width='20', justify='right')
    entry_price_mms.grid(column='1', row='11')
    entry_price_mms.bind('<FocusIn>', on_entry_click('', entry_price_mms, values[10]))
    entry_price_mms.bind('<FocusOut>', on_focusout('', entry_price_mms, values[10]))
    label11 = tk.Label(new_window, text='Стоимость ММС, руб.')
    label11.grid(column='0', row='11', sticky='e')
    entry_free_mb = tk.Entry(new_window, width='20', justify='right')
    entry_free_mb.grid(column='1', row='12')
    entry_free_mb.bind('<FocusIn>', on_entry_click('', entry_free_mb, values[11]))
    entry_free_mb.bind('<FocusOut>', on_focusout('', entry_free_mb, values[11]))
    label12 = tk.Label(new_window, text='Количество Мегабайт')
    label12.grid(column='0', row='12', sticky='e')
    entry_price_mb = tk.Entry(new_window, width='20', justify='right')
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

    def add_row():
        name = entry_name.get()
        if len(name) > 10 or len(name) <= 0:
            #mb.showerror("Ошибка", "Неверно имя")
            name = ''
        subscr = entry_subscr.get()
        if len(subscr) > 5 or len(subscr) <= 0 or not is_number(subscr):
            #mb.showerror('Ошибка', 'Неверно абон. плата')
            subscr = ''
        mins_in = entry_mins_in.get()
        if len(mins_in) > 5 or len(mins_in) <= 0 or not is_int(mins_in):
            #mb.showerror('Ошибка', 'Неверно мин. вн. с.')
            mins_in = ''
        mins_out = entry_mins_out.get()
        if len(mins_out) > 5 or len(mins_out) <= 0 or not is_int(mins_out):
            #mb.showerror('Ошибка', 'Неверно мин. др. с.')
            mins_out = ''
        price_roum = entry_price_roum.get()
        if len(price_roum) > 5 or len(price_roum) <= 0 or not is_number(price_roum):
            #mb.showerror('Ошибка', 'Неверно ст. роум.')
            price_roum = ''
        price_in = entry_price_in.get()
        if len(price_in) > 5 or len(price_in) <= 0 or not is_number(price_in):
            #mb.showerror('Ошибка', 'Неверная ст. мин. вн. с.')
            price_in = ''
        price_out = entry_price_out.get()
        if len(price_out) > 5 or len(price_out) <= 0 or not is_number(price_out):
            #mb.showerror('Ошибка', 'Неверная ст. мин. др. с.')
            price_out = ''
        free_sms = entry_free_sms.get()
        if len(free_sms) > 5 or len(free_sms) <= 0 or not is_int(free_sms):
            #mb.showerror('Ошибка', 'Неверная кол. смс')
            free_sms = ''
        free_mms = entry_free_mms.get()
        if len(free_mms) > 5 or len(free_mms) <= 0 or not is_int(free_mms):
            #mb.showerror('Ошибка', 'Неверная кол. ммс')
            free_mms = ''
        price_sms = entry_price_sms.get()
        if len(price_sms) > 5 or len(price_sms) <= 0 or not is_number(price_sms):
            #mb.showerror('Ошибка', 'Неверная ст. смс')
            price_sms = ''
        price_mms = entry_price_mms.get()
        if len(price_mms) > 5 or len(price_mms) <= 0 or not is_number(price_mms):
            #mb.showerror('Ошибка', 'Неверная ст. ммс')
            price_mms = ''
        free_mb = entry_free_mb.get()
        if len(free_mb) > 5 or len(free_mb) <= 0 or not is_int(free_mb):
            #mb.showerror('Ошибка', 'Неверная кол. мб')
            free_mb = ''
        price_mb = entry_price_mb.get()
        if len(price_mb) > 5 or len(price_mb) <= 0 or not is_number(price_mb):
            #mb.showerror('Ошибка', 'Неверная ст. мб')
            price_mb = ''
        if not(name == '') and not(subscr == '') and not(mins_in == '') and not(mins_out == '') and not(price_roum == '') and not(price_in == '') and not(price_out == '')and not(free_sms == '') and not(free_mms == '') and not(price_sms == '') and not(price_mms == '') and not(free_mb == '') and not(price_mb == ''):
            t_main.insert('', 'end', text=str(len(t_main.get_children()) + 1), values=(name, subscr, mins_in, mins_out, price_roum,
                                                                               price_in, price_out, free_sms, free_mms, price_sms,
                                                                               price_mms, free_mb, price_mb))
        else:
            mb.showerror('Ошибка', 'Неверный ввод')
            open_fill_window()
        new_window.destroy()
        

    new_window = tk.Toplevel(w_main)
    new_window.title("Добавить тариф")
    new_window.geometry('450x380+200+100')
    new_window.resizable(False, False)
    new_window.focus_set()
    new_window.attributes("-topmost", True)
    label = tk.Label(new_window, text="Введите характеристики тарифного плана:", font='Arial 14 bold')
    label.grid(column='0', row='0', columnspan='2', sticky='wn', padx='4')

    entry_name = tk.Entry(new_window, width='20', justify='right')
    entry_name.grid(column='1', row='1')
    label1 = tk.Label(new_window, text='Тариф')
    label1.grid(column='0', row='1', sticky='e')
    entry_subscr = tk.Entry(new_window, width='20', justify='right')
    entry_subscr.grid(column='1', row='2')
    label2 = tk.Label(new_window, text='Абонентская плата')
    label2.grid(column='0', row='2', sticky='e')
    entry_mins_in = tk.Entry(new_window, width='20', justify='right')
    entry_mins_in.grid(column='1', row='3')
    label3 = tk.Label(new_window, text='Мин внутри сети')
    label3.grid(column='0', row='3', sticky='e')
    entry_mins_out = tk.Entry(new_window, width='20', justify='right')
    entry_mins_out.grid(column='1', row='4')
    label4 = tk.Label(new_window, text='Минут на другие сети')
    label4.grid(column='0', row='4', sticky='e')
    entry_price_roum = tk.Entry(new_window, width='20', justify='right')
    entry_price_roum.grid(column='1', row='5')
    label5 = tk.Label(new_window, text='Стоимость роуминга')
    label5.grid(column='0', row='5', sticky='e')
    entry_price_in = tk.Entry(new_window, width='20', justify='right')
    entry_price_in.grid(column='1', row='6')
    label6 = tk.Label(new_window, text='Стоимость внутри сети')
    label6.grid(column='0', row='6', sticky='e')
    entry_price_out = tk.Entry(new_window, width='20')
    entry_price_out.grid(column='1', row='7')
    label7 = tk.Label(new_window, text='Стоимость на другие сети')
    label7.grid(column='0', row='7', sticky='e')
    entry_free_sms = tk.Entry(new_window, width='20')
    entry_free_sms.grid(column='1', row='8')
    label8 = tk.Label(new_window, text='Количество СМС')
    label8.grid(column='0', row='8', sticky='e')
    entry_free_mms = tk.Entry(new_window, width='20')
    entry_free_mms.grid(column='1', row='9')
    label9 = tk.Label(new_window, text='Количество ММС')
    label9.grid(column='0', row='9', sticky='e')
    entry_price_sms = tk.Entry(new_window, width='20', justify='right')
    entry_price_sms.grid(column='1', row='10')
    label10 = tk.Label(new_window, text='Стоимость СМС')
    label10.grid(column='0', row='10', sticky='e')
    entry_price_mms = tk.Entry(new_window, width='20', justify='right')
    entry_price_mms.grid(column='1', row='11')
    label11 = tk.Label(new_window, text='Стоимость ММС')
    label11.grid(column='0', row='11', sticky='e')
    entry_free_mb = tk.Entry(new_window, width='20', justify='right')
    entry_free_mb.grid(column='1', row='12')
    label12 = tk.Label(new_window, text='Количество Мегабайт')
    label12.grid(column='0', row='12', sticky='e')
    entry_price_mb = tk.Entry(new_window, width='20', justify='right')
    entry_price_mb.grid(column='1', row='13')
    label13 = tk.Label(new_window, text='Стоимость Мегабайт')
    label13.grid(column='0', row='13', sticky='e')

    button_add = tk.Button(new_window, text='Добавить', command=add_row, width='10')
    button_exit = tk.Button(new_window, text='Выход', command=new_window.destroy, width='10')
    button_add.grid(column='0', row='14', pady='15', padx='10', sticky='e')
    button_exit.grid(column='1', row='14', pady='15', padx='10', sticky='w')

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
