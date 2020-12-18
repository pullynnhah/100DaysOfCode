import time
from tkinter import *
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#ff737c"
RED = "#ff2a00"
GREEN = "#1c8c0f"
YELLOW = "#ffd966"
FONT_NAME = "4 My Lover"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CHECK_MARK = "✔️"
reps = 0
timer = None
allow_start_button = True


# ---------------------------- STATE SETUP ------------------------------- #
def get_state(repetitions):
    if repetitions % 8 == 0:
        return 'Long Break'
    elif repetitions % 2 == 0:
        return 'Short Break'
    else:
        return 'Work'


# ---------------------------- SOUND SETUP ------------------------------- #
def alarm():
    state = get_state(reps + 1)
    if state == 'Long Break':
        playsound('./sounds/long_break_time.mp3')
    elif state == 'Short Break':
        playsound('./sounds/short_break_time.mp3')
    else:
        playsound('./sounds/work_time.mp3')


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_timer, text=" 00:00 ", font=(FONT_NAME, 50))
    title.config(text="Timer")
    tick.config(text="")


# --------------------------- TIMER MECHANISM ------------------------------ #
def start_timer():
    global reps
    if not allow_start_button:
        return
    reps += 1
    state = get_state(reps)

    if state == 'Long Break':
        title.config(text="LONG BREAK", fg=RED, font=(FONT_NAME, 24))
        count_down(LONG_BREAK_MIN * 60)
    elif state == 'Short Break':
        title.config(text="SHORT BREAK", fg=PINK, font=(FONT_NAME, 24))
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title.config(text="WORK", fg=GREEN, font=(FONT_NAME, 36))
        count_down(WORK_MIN * 60)


# ------------------------- COUNTDOWN MECHANISM ---------------------------- #
def count_down(count):
    global allow_start_button, reps, timer
    if count == 0:
        tick.config(text=f'{CHECK_MARK * ((reps + 1) // 2)}')
    if count < 0:
        state = get_state(reps + 1)
        canvas.itemconfig(canvas_timer, text=f" {state} \n    Next... ", font=(FONT_NAME, 24))

        allow_start_button = True
        window.lift()
        alarm()
        return
    allow_start_button = False
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(canvas_timer, text=f" {count_min:02}:{count_sec:02} ", font=(FONT_NAME, 50))
    timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=25, pady=25, bg=YELLOW)
window.resizable(False, False)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato)
canvas_timer = canvas.create_text(101, 140, text=' 00:00 ', font=(FONT_NAME, 50))

title = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36))
start = Button(text="START", font=(FONT_NAME, 16), width=4,
               highlightthickness=0, command=start_timer)
reset = Button(text="RESET", font=(FONT_NAME, 16), width=4,
               highlightthickness=0, command=reset_timer)

canvas.grid(column=1, row=1)
title.grid(column=1, row=0)
tick.grid(column=1, row=3)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

window.mainloop()
