import json
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


# ---------------------------- SEARCH PASSWORD ------------------------------ #
def search():
    website = website_entry.get()
    if len(website) == 0:
        message = "Please make sure the field 'Website' is not empty."
        messagebox.showinfo(title='Oops', message=message)
        return
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        message = "No Data File Found"
        messagebox.showerror(title="No Data", message=message)
    else:
        if website in data:
            password = data[website]["password"]
            username = data[website]["username"]
            message = f'Username: {username}\nPassword: {password}'
            messagebox.showinfo(title=website, message=message)
        else:
            message = 'No details for the website exists.'
            messagebox.showerror(title="No Website", message=message)


# ----------------------------- SAVE PASSWORD ------------------------------- #
def add_file(new_data):
    try:
        with open('passwords.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('passwords.json', 'w') as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open('passwords.json', 'w') as file:
            json.dump(data, file, indent=4)


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        message = "Please make sure you haven't left any fields empty."
        messagebox.showinfo(title='Oops', message=message)
        return
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    message = f'These are the details entered:\nUsername: {username}'
    message += f'\nPassword: {password}\nIs it ok to save?'
    is_ok = messagebox.askyesno(title=website, message=message)
    if not is_ok:
        return

    add_file(new_data)
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

website_entry = Entry(width=25, font=FONT)
website_entry.focus()
username_entry = Entry(width=42, font=FONT)
username_entry.insert(0, "pullynnhah")
password_entry = Entry(width=25, font=FONT)

add_button = Button(text="Add", font=FONT, width=40, command=save)
generate_password_button = Button(text="Generate Password", font=FONT,
                                  command=generate_password, width=14)
search_button = Button(text="Search", font=FONT, command=search, width=14)
canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

add_button.grid(column=1, row=4, columnspan=2)
generate_password_button.grid(column=2, row=3)
search_button.grid(column=2, row=1)

window.mainloop()
