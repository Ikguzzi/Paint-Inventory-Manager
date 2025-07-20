from tkinter import *
from tkinter.ttk import *
from Models.Paints_Add import *
import json

path = "Data\JSON_Test.json"


def Open_Paints_View():

    # Root
    r = Toplevel()

    r.title("Paint Inventory")
    r.geometry("1200x700")

    header = Label(r, text="Paint Catalog", font=("Arial", 30))
    header.grid(row=0, columnspan=2, sticky="we")

    r.grid_rowconfigure(0, weight=0, minsize=40)
    r.grid_rowconfigure(1, weight=1)
    r.grid_columnconfigure(1, weight=3)  # For detailed view

    paint_frame = Frame(r, padx=7.5, pady=7.5)
    paint_frame.grid(row=1, column=0, sticky="nswe")

    menu = Menu(r)

    r.config(menu=menu)
    fileMenu = Menu(menu)
    menu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New Paint", command=Add_Paint)
    fileMenu.add_separator()
    fileMenu.add_command(label="Import...")
    fileMenu.add_command(label="Export")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")

    editMenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label="Help")
    helpMenu.add_command(label="About")

    with open(path, "r") as f:
        data = f.read()
        if data.strip() == "":
            print("JSON file is empty!")
        else:
            data = json.loads(data)

            paint_table = Treeview(
                paint_frame,
                columns=("Name", "Brand", "Type", "Status", "Amount"),
                show="headings",
            )
            paint_table.grid(row=1, column=0, sticky="nsew")

            paint_table.heading("Name", text="Name")
            paint_table.heading("Brand", text="Brand")
            paint_table.heading("Type", text="Type")
            paint_table.heading("Status", text="Status")
            paint_table.heading("Amount", text="Amount")

            for v in data["Paints"]:

                paint_table.insert(
                    parent="",
                    index=0,
                    values=(v["name"], v["brand"], v["type"], v["status"], v["amount"]),
                )

    detail_frame = Frame(r, bg="red", padx=7.5, pady=7.5)
    detail_frame.grid(row=1, column=1, sticky="nswe")
