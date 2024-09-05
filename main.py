from tkinter import *
import random
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for char in range(nr_letters)]
    password_list2 = [random.choice(symbols) for sym in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for nos in range(nr_numbers)]
    password_list = password_list1+password_list2+password_list3
    random.shuffle(password_list)
    p = ''.join(password_list)
    input_password.insert(index=0, string=p)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    wb = input_website.get()
    em = input_email.get()
    pwd = input_password.get()
    new_dic = {wb: {"email": em, "password": pwd}}
    if len(wb) == 0 or len(pwd) == 0:
        messagebox.showwarning(title="Note:", message="Please fill out all the fields")
    else:
        try:  # opening the file without creating one
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:  # if an error occurs what to do
            with open("data.json", "w") as file:
                json.dump(new_dic, file, indent=4)
        else:  # if the try block suceeds or the except block is executed
            data.update(new_dic)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)
# ---------------------------- SEARCH PASSWORD------------------------------- #

def save_pwd():
    web = input_website.get()
    with open("data.json", "r") as file:
        data = json.load(file)
        if web in data:
            messagebox.showinfo(title="Found:",message=f"Email:{data[web]["email"]}\nPassword:{data[web]["password"]}")
        else:
            messagebox.showwarning(title="Note:",message="Website details not found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
pic = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=pic)
canvas.grid(column=1, row=0)
website = Label(text="Website:", font=("Calibri", 10, "bold"))
website.grid(column=0, row=1)
email = Label(text="Email/User_name:", font=("Calibri", 10, "bold"))
email.grid(column=0, row=2)
password = Label(text="Password:", font=("Calibri", 10, "bold"))
password.grid(column=0, row=3)
input_website = Entry(width=35)
input_website.focus()
input_website.grid(column=1, row=1, columnspan=2)
input_email = Entry(width=35)
input_email.insert(index=0, string="name@email.com")
input_email.grid(column=1, row=2, columnspan=2)
input_password = Entry(width=35)
input_password.grid(column=1, row=3, columnspan=2)
button1 = Button(text="generate password",command=generate)
button1.grid(column=2, row=3,columnspan=1)
button2 = Button(text="Add",width=30,command=save)
button2.grid(column=1, row=4, columnspan=2)
button3 = Button(text="Search",width=14,command=save_pwd)
button3.grid(column=2, row=1, columnspan=2)
window = mainloop()
