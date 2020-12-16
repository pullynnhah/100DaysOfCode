from tkinter import *

FONT = ("Letters for Learners", 24, "bold")


def calculate():
    km = float(entry.get()) * 1.60934
    label4.config(text=f'{km:.5f}')


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)

label1 = Label(text='Miles', font=FONT, padx=10, pady=10)
label2 = Label(text='Km', font=FONT, padx=10, pady=10)
label3 = Label(text='is equal to', font=FONT, padx=10, pady=10)
label4 = Label(text='', font=FONT, padx=10, pady=10)

button = Button(text='Calculate', command=calculate, font=FONT, padx=10, pady=10)

entry = Entry(width=8, font=FONT)

label1.grid(column=2, row=0)
label2.grid(column=2, row=1)
label3.grid(column=0, row=1)
label4.grid(column=1, row=1)
button.grid(column=1, row=2)
entry.grid(column=1, row=0)

window.mainloop()
