import random
import string
import tkinter as tk

def generatePassword(length, custom):
    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(character, length)) + custom
    return password

def generate_password():
    length = int(length_entry.get())
    custom = custom_entry.get()
    password = generatePassword(length, custom)
    password_label.config(text="Generated Password: {}".format(password))

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter length of your desired Password:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

custom_label = tk.Label(root, text="Enter your custom character to be included in your Password:")
custom_label.pack()

custom_entry = tk.Entry(root)
custom_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
