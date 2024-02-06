import tkinter as tkinter

from tkinter import *
root = Tk()

def test_click():
    root.title('WAS TESTED')

main_window = Label(root, width = '100', height='40')
test_button = Button(text = 'test button', command=test_click)

root.title('NOT TESTED')


test_button.pack()
main_window.pack()





root.mainloop()