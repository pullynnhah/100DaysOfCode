import tkinter

FONT = ("Letters for Learners", 16, "bold")


def button_clicked():
    string = tk_input.get()
    label.config(text=string, font=FONT)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text="I am a Label", font=FONT)
button1 = tkinter.Button(text="Click Me 1", font=FONT, command=button_clicked)
button2 = tkinter.Button(text="Click Me 2", font=FONT, command=button_clicked)
tk_input = tkinter.Entry(width=10, font=FONT)

label.config(padx=20, pady=20)
button1.config(padx=20, pady=20)
button2.config(padx=20, pady=20)

label.grid(column=0, row=0)
button1.grid(column=1, row=1)
button2.grid(column=2, row=0)
tk_input.grid(column=3, row=2)

window.mainloop()
