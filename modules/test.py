import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Age')
tree.heading('#0', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

# Добавляем некоторые начальные строки
tree.insert('', 'end', text='1', values=('Alice', 25))
tree.insert('', 'end', text='2', values=('Bob', 30))

# Функция для добавления новой строки
def add_row():
    name = entry_name.get()
    age = entry_age.get()
    tree.insert('', 'end', text=str(len(tree.get_children()) + 1), values=(name, age))

# Создаем элементы управления для ввода данных
entry_name = tk.Entry(root)
entry_name.pack()
entry_age = tk.Entry(root)
entry_age.pack()
button_add = tk.Button(root, text='Add Row', command=add_row)
button_add.pack()

tree.pack()
root.mainloop()