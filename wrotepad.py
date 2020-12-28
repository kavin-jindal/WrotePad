from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as ScrolledText
from tkinter import ttk
import webbrowser


root = Tk()
root.title("WrotePad")
root.geometry("1365x707")

menu = Menu(root)
root.config(menu=menu)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)


frame1 = Frame(my_notebook, width=1365, height=707, bg="white")
frame2 = Frame(my_notebook, width=1365, height=707, bg="white")

frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)

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
    root.title(f'{name} -  Equit')

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
    info.title("Equit App Info")
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

text = ScrolledText.ScrolledText(frame1, width=1365, height=707, font=("Arial", 20))
text.pack()

#label1 = Label(frame2, text="Program Help", bg="white", fg="black", font=("Arial", 40))
#label1.pack()

#l#abel2 = Label(frame2, text="dd", fg="black", bg="white")
#label2.pack()



root.mainloop()