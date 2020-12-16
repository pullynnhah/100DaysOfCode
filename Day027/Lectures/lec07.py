from tkinter import *

FONT = ("Letters for Learners", 16, "bold")
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = Label(text="I am a Label", font=FONT)
label.pack(side='left')

label["text"] = "I am still a Label"
label.config(text="Nope. Still a Label")

window.mainloop()
