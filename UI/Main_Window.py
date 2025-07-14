import tkinter as tk

class MainWindow:        
    def __init__(self, master):
        self.master = master
        self.master.geometry ('1200x700')
        self.master.title ('Miniature Paint Catalog')

        # Header
        header = tk.Label(master, text='Warhammer Paint Catalog', font=('Arial', 30))

        # # Navbar
        btnWidth = 30

        collectionBtn = tk.Button(master, text='Paint Collection', width=btnWidth)
        schemesBtn = tk.Button(master, text='Paint Schemes', width=btnWidth)

        header.pack(pady=20)
        collectionBtn.pack()
        schemesBtn.pack()
