from tkinter import *
from tkinter import ttk
import sys
import re
import time
import platform
import tkinter.font as font
import tkinter.scrolledtext as ScrolledText
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import math
import os
#from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

root = Tk()
root.title("WrotePad")
root.geometry("1365x707")

menu = Menu(root)
root.config(menu=menu)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)


frame1 = Frame(my_notebook, width=1365, height=707, bg="white")
#frame2 = Frame(my_notebook, width=1365, height=707, bg="white")

frame1.pack(fill="both", expand=1)
#frame2.pack(fill="both", expand=1)

my_notebook.add(frame1, text="Editor")
#my_notebook.add(frame2, text="Help")





def open_file():
    text.delete('1.0', END)
    text_file = filedialog.askopenfilename(initialdir ='/', title = 'Open Files', filetypes=[('Text Files', "*.txt")])

    if text_file:
        global open_status_name
        open_status_name = text_file


    name = text_file
    name = name.replace('/', '')
    root.title(f'{name} -  WrotePad')

    text_file = open(text_file, 'r')
    stuff = text_file.read()
    text.insert(END, stuff)
    text_file.close()

def new_file():
    text.delete(1.0, END)
    root.title('New File - WrotePad')

    global open_status_name
    open_status_name = False

def save_as_file():
    filetypes=[('Text Files', '*.txt')]
    text_file = filedialog.asksaveasfilename(initialdir ='/', title = 'Save as Files', filetypes=filetypes, defaultextension = filetypes)
    if text_file:
        name = text_file
        name = name.replace('/', '')
        root.title(f'{name} - WrotePad')
        text_file = open(text_file, 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()

def new_window():
    pass


def cut_text(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()
        text.delete('sel.first', 'sel.last')


def copy_text(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()


def paste_text(e):
    if selected:
        position = text.index(INSERT)
        text.insert(position, selected)

def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

def github():
    webbrowser.open('https://github.com/kavinjindal')

def dev_info():
    info = Tk()
    info.title('Developer Info')
    info.configure(bg='white')
    info.geometry('200x200')
    label1_info = Label(info, text='Developer : Kavin Jindal', fg='black', bg='white')
    label1_info.pack()
    label2_info = Label(info, text='Email : kavinsjindal@gmail.com', fg='black', bg='white')
    label2_info.pack()
    label3_info = Label(info, text='Discord ID : KJ#7320', fg='black', bg='white')
    label3_info.pack()
    btn_info =Button(info, text='Kavin Jindal on Github', fg='white', bg='red', command=github)
    btn_info.pack()

def app_info():
    app = Tk()
    app.title("WrotePad Info")
    app.configure(bg='white')
    app.geometry('900x200')
    label1_app = Label(app, text=f'Python Version : {(platform.python_version)}', fg='black', bg='white')
    label1_app.pack()
    label2_app = Label(app, text=f'Modules : ScrolledText, TTk, Tkinter,WebBrowser, Psutil, Platform, Font', fg='black', bg='white')
    label2_app.pack()
    label3_app = Label(app, text=f'Released on : 29.12.2020', fg='black', bg='white')
    label3_app.pack()
    label4_app = Label(app, text=f'Last Updated on : 26.02.2021', fg='black', bg='white')
    label4_app.pack()

def version():
    version = Tk()
    version.title('WrotePad Version')
    version.configure(bg='white')
    version.geometry('200x200')
    label1_version = Label(version, text='VERSION 1.1.0', fg='black', bg='white', font=('Arial', 20))
    label1_version.pack()


file_menu=Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label='New Window', command=new_window)
file_menu.add_separator()
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_separator()

file_menu.add_command(label="Save as", command=save_as_file)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command =lambda: cut_text(False))
edit_menu.add_command(label='Copy', command =lambda: copy_text(False))
edit_menu.add_command(label='Paste',command =lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label='Undo', command =undo)
edit_menu.add_command(label='Redo', command =redo)

info_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='App Version', menu=info_menu)
info_menu.add_command(label='Developer Info', command=dev_info)
info_menu.add_command(label='App Info', command=app_info)
info_menu.add_command(label='WrotePad Version', command=version)


text = ScrolledText.ScrolledText(frame1, width=101, height=30, font=("Arial", 20), selectbackground='yellow',
selectforeground='black', borderwidth=1, undo=True)
text.pack()

#label1 = Label(frame2, text="Program Help", bg="white", fg="black", font=("Arial", 40))
#label1.pack()

#l#abel2 = Label(frame2, text="dd", fg="black", bg="white")
#label2.pack()



root.mainloop()
