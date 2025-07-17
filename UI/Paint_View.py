from tkinter import *
from tkinter.ttk import *
from Models.Paints_Add import *
import json


def Open_Paints_View():

    # Root
    r = Toplevel()

    r.title("Paint Inventory")
    r.geometry("1200x700")

    header = Label(r, text="Paint Catalog", font=("Arial", 30))
    header.pack()

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

    with open("Data\JSON_Test.json", "r") as f:
        data = f.read()
        if data.strip() == "":
            print("JSON file is empty!")
        else:
            data = json.loads(data)
            for v in data["Paints"]:
                paint_frame = Frame(r, width=800)
                paint_frame.pack(fill=X)

                for i in range(4):
                    paint_frame.columnconfigure(i, weight=1)

                name = Label(paint_frame, text=v["name"], bg="lightblue").grid(
                    row=0, column=0, sticky="ew", padx=10, pady=5
                )
                brand = Label(paint_frame, text=v["brand"], bg="red").grid(
                    row=0, column=1, sticky="ew", padx=10, pady=5
                )
                type = Label(paint_frame, text=v["type"], bg="green").grid(
                    row=0, column=2, sticky="ew", padx=10, pady=5
                )
                status = Label(paint_frame, text=v["status"], bg="yellow").grid(
                    row=0, column=3, sticky="ew", padx=10, pady=5
                )

                paint_frame.pack(fill=X)
