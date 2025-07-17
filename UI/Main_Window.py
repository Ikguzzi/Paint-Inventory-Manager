import tkinter as tk
from UI.Paint_View import Open_Paints_View
from UI.Schemes_View import Open_Schemes_View

class MainWindow:        
    def __init__(self, master):
        self.master = master
        self.master.geometry ('500x300')
        self.master.title ('Miniature Paint Catalog')

        # Header
        header = tk.Label(master, text='Warhammer Paint Catalog', font=('Arial', 30))

        # # Navbar
        btnWidth = 30

        collectionBtn = tk.Button(master, text='Paint Collection', width=btnWidth, command=Open_Paints_View)
        schemesBtn = tk.Button(master, text='Paint Schemes', width=btnWidth, command=Open_Schemes_View)

        header.pack(pady=20)
        collectionBtn.pack()
        schemesBtn.pack()
