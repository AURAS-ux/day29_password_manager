from tkinter import *
import csv
from tkinter import messagebox
import random
import pyperclip


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

def SaveData(data):
    if websiteBox.get() == "" or emailUsernameBox.get() == "" or passwordBox.get() == "":
        messagebox.showinfo(title="Error", message="Please fill all spaces")
    else:
        answer = messagebox.askokcancel(title="Confirm", message=f"Are those the credentials you wanted to add "
                                                                 f"\nEmail:{emailUsernameBox.get()}"
                                                                 f"\nWebsite:{websiteBox.get()}"
                                                                 f"\nPassword:{passwordBox.get()}")

        if answer:
            file = open("data.csv", "a", newline="")
            writer = csv.writer(file)
            writer.writerow(data)
        else:
            EmptyEntrys()


def GetData(website, email, password):
    data = [website, email, password]
    return data


def EmptyEntrys():
    websiteBox.delete(0, END)
    passwordBox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
window.resizable(False, False)

mainImage = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=mainImage)
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0, sticky="e")
websiteBox = Entry(width=35)
websiteBox.grid(row=1, column=1, columnspan=2, sticky="w")
websiteBox.focus()

emailUsernameLabel = Label(text="Email/Username:")
emailUsernameLabel.grid(row=2, column=0)
emailUsernameBox = Entry(width=35)
emailUsernameBox.grid(row=2, column=1, columnspan=2, sticky="w")
emailUsernameBox.insert(0, "auraspaltaneamarian@gmail.com")

passwordLabel = Label(text="Password")
passwordLabel.grid(row=3, column=0)
passwordBox = Entry(width=21)
passwordBox.grid(row=3, column=1, sticky="w")
genPassword = Button(text="Generate Password", height=1, width=14, command=lambda: [GeneratePassword()])
genPassword.grid(row=3, column=2, sticky="w")

addButton = Button(text="Add", height=1, width=39,
                   command=lambda: [SaveData(GetData(websiteBox.get(), emailUsernameBox.get(), passwordBox.get())),
                                    EmptyEntrys()])
addButton.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
