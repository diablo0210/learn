from tkinter import *

def converter():
    miles = float(miles_input.get())
    kms = miles * 1.609
    km_result_label.config(text=f"{kms}")

window = Tk()
window.title("Converter: miles to kms")
window.config(padx=80, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="kms")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Convert", command=converter)
calculate_button.grid(column=1, row=2)


window.mainloop()