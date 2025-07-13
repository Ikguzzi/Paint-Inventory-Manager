import tkinter as tk

debugSize = '1200x700'

app = tk.Tk()

paintTitle = 'Miniature Paint Catalog'
app.title(paintTitle)
app.geometry(debugSize)

# Header
header = tk.Label(app, text='Hello World!', font=('Arial', 14))
header.pack(pady=20)

app.mainloop()
