import tkinter as tk

def Open_Schemes_View():
    viewWin = tk.Toplevel()
    viewWin.title("Paint Schemes")
    viewWin.geometry("400x300")

    header = tk.Label(viewWin, text='Paint Schemes', font=('Arial', 30))
    header.pack()