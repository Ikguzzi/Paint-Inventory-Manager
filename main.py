import tkinter as tk

windowSize = '1200x700'

app = tk.Tk()

paintTitle = 'Miniature Paint Catalog'
app.title(paintTitle)
app.geometry(windowSize)

# Header
header = tk.Label(app, text='Warhammer Paint Catalog', font=('Arial', 30))
header.pack(pady=20)

# Navbar

btnWidth = 30

collectionBtn = tk.Button(text='Paint Collection', width=btnWidth)
collectionBtn.pack()

schemesBtn = tk.Button(text='Paint Schemes', width=btnWidth)
schemesBtn.pack()

app.mainloop()
