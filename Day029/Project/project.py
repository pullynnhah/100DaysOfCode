from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
from pyperclip import copy

# ------------------------------ CONSTANTS ---------------------------------- #
FONT = ("Letters for Learners1", 11)
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# -------------------------- PASSWORD GENERATOR ----------------------------- #
def generate_password():
    letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_list = letters + symbols + numbers
    
    shuffle(password_list)
    password = ''.join(password_list)
    copy(password)
    password_entry.insert(0, password)


# ----------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        message = "Please make sure you haven't left any fields empty."
        messagebox.showinfo(title='Oops', message=message)
        return
    message = f'These are the details entered:\nUsername: {username}'
    message += f'\nPassword: {password}\nIs it ok to save?'
    is_ok = messagebox.askyesno(title=website, message=message)
    if not is_ok:
        return

    with open('passwords.csv', mode='a') as file:
        file.write(f'{website},{username},{password}\n')
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ------------------------------- UI SETUP ---------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file='padlock.png')
canvas.create_image(100, 100, image=lock)

website_label = Label(text="Website:", font=FONT)
username_label = Label(text="Email/Username:", font=FONT)
password_label = Label(text="Password:", font=FONT)

website_entry = Entry(width=40, font=FONT)
website_entry.focus()
username_entry = Entry(width=40, font=FONT)
username_entry.insert(0, "pullynnhah")
password_entry = Entry(width=21, font=FONT)

add_button = Button(text="Add", font=FONT, width=40, command=save)
generate_password_button = Button(text="Generate Password", font=FONT,
                                  command=generate_password, width=14   )

canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, columnspan=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

add_button.grid(column=1, row=4, columnspan=2)
generate_password_button.grid(column=2, row=3)

window.mainloop()
