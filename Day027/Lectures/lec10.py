import tkinter

FONT = ("Letters for Learners", 16, "bold")
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=FONT)
label.pack()


def button_clicked():
    string = tk_input.get()
    label.config(text=string, font=FONT)


button = tkinter.Button(text="Click Me", font=FONT, command=button_clicked)
button.pack()

tk_input = tkinter.Entry(width=10, font=FONT)
tk_input.pack()

window.mainloop()
