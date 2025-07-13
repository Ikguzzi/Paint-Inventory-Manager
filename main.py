import tkinter as tk

app = tk.Tk()

paintTitle = 'Miniature Paint Catalog'
app.title(paintTitle)

# Header
header = tk.Label(app, text="Hello World!", font=('Arial', 14))
header.pack(pady=20)

app.mainloop()
