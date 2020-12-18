import time

import pandas
import random
from tkinter import *

# --------------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
TITLE_COLOR = "#BB00FF"
WORD_COLOR = "#FF0080"
FONT_TITLE = ("Letters for Learners", 36, 'italic')
FONT_WORD = ("Letters for Learners", 80, "bold")
word = None
allow_buttons = True

# ---------------------------- DATA ACCESS/SAVING ----------------------------#
try:
    data_frame = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("./data/french_words.csv")

words = data_frame.to_dict(orient="records")


# -------------------------- CREATING FLASHCARDS ---------------------------- #
def flip_card():
    canvas.itemconfig(background_card, image=back_img)
    canvas.itemconfig(title_canvas, text="English")
    canvas.itemconfig(word_canvas, text=word["English"])


def right():
    global words
    words.remove(word)
    gen_flashcard()
    words_data_frame = pandas.DataFrame(words)
    words_data_frame.to_csv('./data/words_to_learn.csv', index=False)


def gen_flashcard():
    global flip, word
    window.after_cancel(flip)
    canvas.itemconfig(background_card, image=front_img)
    word = random.choice(words)
    canvas.itemconfig(title_canvas, text="French")
    canvas.itemconfig(word_canvas, text=word["French"])
    flip = window.after(3000, flip_card)


# --------------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)

front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
background_card = canvas.create_image(400, 263, image=front_img)

title_canvas = canvas.create_text(400, 150, text='Title',
                                  fill=TITLE_COLOR, font=FONT_TITLE)

word_canvas = canvas.create_text(400, 263, text='',
                                 fill=WORD_COLOR, font=FONT_WORD)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=gen_flashcard)
right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=right)

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)
gen_flashcard()
window.mainloop()
