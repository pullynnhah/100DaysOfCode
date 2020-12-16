import tkinter

FONT = ("Letters for Learners", 16, "bold")


def button_clicked():
    string = tk_input.get()
    label.config(text=string, font=FONT)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=FONT)
button = tkinter.Button(text="Click Me", font=FONT, command=button_clicked)
tk_input = tkinter.Entry(width=10, font=FONT)

label.place(x=0, y=0)
button.place(x=100, y=50)
tk_input.place(x=0, y=100)

window.mainloop()
