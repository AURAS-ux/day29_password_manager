from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GeneratePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for i in range(nr_letters)]

    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)
    passwordBox.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def SaveData():
    website = websiteBox.get()
    email = emailUsernameBox.get()
    password = passwordBox.get()
    new_dic = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if websiteBox.get() == "" or emailUsernameBox.get() == "" or passwordBox.get() == "":
        messagebox.showinfo(title="Error", message="Please fill all spaces")
    else:
        data = LoadJsonFile()
        data.update(new_dic)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


def LoadJsonFile():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data
    except json.decoder.JSONDecodeError:
        with open("data.json", "w") as file:
            json.dump({}, file, indent=4)


def EmptyEntrys():
    websiteBox.delete(0, END)
    passwordBox.delete(0, END)

def Find(site):
    jsonData = LoadJsonFile()
    for i in jsonData:
        if i == site:
            messagebox.showinfo(title="Your credentials",
                                message=f"E-mail:{jsonData[i]['email']}\nPassword:{jsonData[i]['password']}")
        else:
            messagebox.showinfo(title="Error",message=f"No data entries for website:{site}")
            break


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
LoadJsonFile()
window.title("Password Manager")
window.config(pady=50, padx=50)
window.resizable(False, False)

mainImage = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=mainImage)
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0, sticky="e")
websiteBox = Entry(width=32)
websiteBox.grid(row=1, column=1, columnspan=2, sticky="w")
websiteBox.focus()

searchButton = Button(text="Search", relief="groove", height=1, width=12, command=lambda: [Find(websiteBox.get())])
searchButton.grid(column=2, row=1)

emailUsernameLabel = Label(text="Email/Username:")
emailUsernameLabel.grid(row=2, column=0)
emailUsernameBox = Entry(width=35)
emailUsernameBox.grid(row=2, column=1, columnspan=2, sticky="w")
emailUsernameBox.insert(0, "auraspaltaneamarian@gmail.com")

passwordLabel = Label(text="Password")
passwordLabel.grid(row=3, column=0)
passwordBox = Entry(width=32)
passwordBox.grid(row=3, column=1, sticky="w", columnspan=2)
genPassword = Button(text="Generate Password", relief="groove", height=1, width=14,
                     command=lambda: [GeneratePassword()])
genPassword.grid(row=3, column=2, sticky="w")

addButton = Button(text="Add", height=1, width=39, relief="groove",
                   command=lambda: [SaveData(),
                                    EmptyEntrys()])
addButton.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
