from tkinter import *
import requests

FONT = ("Letters for Learners", 30, "bold")


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    text = response.json()["quote"]
    canvas.itemconfig(quote, text=text)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote = canvas.create_text(150, 207, text="Kanye Quote goes HERE",
                           width=250, font=FONT, fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
