import tkinter as tk
from tkinter.ttk import * 
from Models.Paints_Add import *

def Open_Paints_View():
    
    # Root
    r = tk.Toplevel()

    r.title("Paint Inventory")
    r.geometry("1200x700")

    header = tk.Label(r, text='Paint Catalog', font=('Arial', 30))
    header.pack()

    menu = tk.Menu(r)

    r.config(menu=menu)
    fileMenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=fileMenu)
    fileMenu.add_command(label="New Paint", command=Add_Paint)
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