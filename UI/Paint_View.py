import tkinter as tk

def Open_Paints_View():
    viewWin = tk.Toplevel()
    viewWin.title("Paint Inventory")
    viewWin.geometry("400x300")

    header = tk.Label(viewWin, text='Paint Catalog', font=('Arial', 30))
    header.pack()