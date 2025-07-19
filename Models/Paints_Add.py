from tkinter import *
import json

font = "Arial"
normal_text_size = 11
path = "Data\JSON_Test.json"


def Add_Paint():
    def Register():
        name = name_textbox.get()
        brand = brand_textbox.get()
        type = type_textbox.get()
        value = rgb_textbox.get()
        status = status_textbox.get()

        try:
            with open(path, "r") as f:
                data = json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            data = {"Paints": []}

        existing_ids = [paint["id"] for paint in data["Paints"]]
        new_id = max(existing_ids, default=0) + 1

        new_paint = {
            "id": new_id,
            "name": name,
            "brand": brand,
            "type": type,
            "value": value,
            "status": status,
        }

        data["Paints"].append(new_paint)

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    r = Toplevel()

    r.title("Add Paint...")
    r.geometry("400x300")

    Label(r, text="Name", font=(font, normal_text_size)).grid(row=0, column=0)
    name_textbox = Entry(r)
    name_textbox.grid(row=0, column=1)

    Label(r, text="Brand", font=(font, normal_text_size)).grid(row=1, column=0)
    brand_textbox = Entry(r)
    brand_textbox.grid(row=1, column=1)

    Label(r, text="Type", font=(font, normal_text_size)).grid(row=2, column=0)
    type_textbox = Entry(r)
    type_textbox.grid(row=2, column=1)

    Label(r, text="RGB Value (optional)", font=(font, normal_text_size)).grid(
        row=3, column=0
    )
    rgb_textbox = Entry(r)
    rgb_textbox.grid(row=3, column=1)

    Label(r, text="Status (optional)", font=(font, normal_text_size)).grid(
        row=4, column=0
    )
    status_textbox = Entry(r)
    status_textbox.grid(row=4, column=1)

    add_button = Button(r, text="Add", command=Register)
    add_button.grid(row=5, column=1)
