from tkinter import *


def button_clicked():
    number = round(int(input.get()) * 1.60934, 2)
    converted_kms_label.config(text=number)


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=250, height=250)
window.config(padx=30, pady=30)

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)
# input.config(padx=5, pady=5)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)
# miles_label.config(padx=20, pady=20)

equal_label = Label()
equal_label.config(text="is equal to ")
equal_label.grid(column=0, row=1)
# equal_label.config(padx=20, pady=20)

converted_kms_label = Label()
converted_kms_label.config(text="0")
converted_kms_label.grid(column=1, row=1)
# converted_kms_label.config(padx=20, pady=20)

kms_label = Label()
kms_label.config(text="Km")
kms_label.grid(column=2, row=1)
# kms_label.config(padx=20, pady=20)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
