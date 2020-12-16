import tkinter

FONT = ("Letters for Learners", 16, "bold")
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=FONT)
label.pack()

label["text"] = "I am still a Label"
label.config(text="Nope. Still a Label")


def button_clicked():
    print("I got clicked")


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
