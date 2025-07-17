from tkinter import *

font = "Arial"
normal_text_size = 11


def Add_Paint():
    r = Toplevel()

    r.title("Add Paint...")
    r.geometry("400x300")

    name_textbox_label = Label(r, text="Name", font=(font, normal_text_size)).grid(
        row=0
    )
    name_textbox = Entry(r).grid(row=0, column=1)

    brand_textbox_label = Label(r, text="Brand", font=(font, normal_text_size)).grid(
        row=1
    )
    brand_textbox = Entry(r).grid(row=1, column=1)

    type_textbox_label = Label(r, text="Type", font=(font, normal_text_size)).grid(
        row=2
    )
    type_textbox = Entry(r).grid(row=2, column=1)

    rgb_textbox_label = Label(
        r, text="RGB Value (optional)", font=(font, normal_text_size)
    ).grid(row=3)
    rgb_textbox = Entry(r).grid(row=3, column=1)

    status_textbox_label = Label(
        r, text="Status (optional)", font=(font, normal_text_size)
    ).grid(row=4)
    status_textbox = Entry(r).grid(row=4, column=1)

    add_button = Button(r, text="Add", command=print("Added Paint!!"))
    add_button.grid(row=5, column=3)
