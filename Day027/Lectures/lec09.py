import tkinter

FONT = ("Letters for Learners", 16, "bold")
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=FONT)
label.pack()


def button_clicked():
    label.config(text="I am Still a Label")


button = tkinter.Button(text="Click Me", font=FONT, command=button_clicked)
button.pack()

window.mainloop()
