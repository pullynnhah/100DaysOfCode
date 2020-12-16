import tkinter

FONT = ("Letters for Learners", 16, "bold")
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=FONT)
label.pack()

window.mainloop()
