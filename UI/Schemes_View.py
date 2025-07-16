import tkinter as tk

def Open_Schemes_View():
    r = tk.Toplevel()
    r.title("Paint Schemes")
    r.geometry("400x300")

    header = tk.Label(r, text='Paint Schemes', font=('Arial', 30))
    header.pack()

    menu = tk.Menu(r)

    r.config(menu=menu)
    fileMenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label="New Scheme")
    fileMenu.add_separator()
    fileMenu.add_command(label="Import...")
    fileMenu.add_command(label="Export")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")

    editMenu = tk.Menu(menu)
    menu.add_cascade(label='Edit', menu=editMenu)

    helpMenu = tk.Menu(menu)
    menu.add_cascade(label='Help', menu=helpMenu)
    helpMenu.add_command(label="Help")
    helpMenu.add_command(label="About")