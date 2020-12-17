from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#ff737c"
RED = "#ff2a00"
GREEN = "#1c8c0f"
YELLOW = "#ffd966"
FONT_NAME = "JetBrains Mono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CHECK_MARK = "✔️"

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
def say_something(a, b, c):
    print(a)
    print(b)
    print(c)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, say_something, 3, 5, 8)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato)
canvas.create_text(101, 140, text='00:00', font=(FONT_NAME, 36, 'bold'))

title = Label(text="Study", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
tick = Label(text=CHECK_MARK, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36))

start = Button(text="START", font=(FONT_NAME, 16), width=4, highlightthickness=0)
reset = Button(text="RESET", font=(FONT_NAME, 16), width=4, highlightthickness=0)

canvas.grid(column=1, row=1)
title.grid(column=1, row=0)
tick.grid(column=1, row=3)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

window.mainloop()
