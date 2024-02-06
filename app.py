import tkinter as tkinter

import sys
sys.path.insert(1, './modules')
import test_module



from tkinter import *
root = Tk()

def test_click():
    root.title('WAS TESTED')
    test_module.module_func()

main_window = Label(root, width = '100', height='40')
test_button = Button(text = 'test button', command=test_click)

root.title('NOT TESTED')


test_button.pack()
main_window.pack()





root.mainloop()