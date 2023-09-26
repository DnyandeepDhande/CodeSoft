import tkinter as tk
from tkinter import font
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    if complexity == 'Low':
        characters = lower_case + digits
    elif complexity == 'Medium':
        characters = lower_case + upper_case + digits
    elif complexity == 'High':
        characters = lower_case + upper_case + digits + special_chars

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}")


root = tk.Tk()
root.title("Password Generator")


custom_font = font.Font(family="Helvetica", size=16)


length_label = tk.Label(root, text="Password Length:", font=custom_font)
length_label.pack()
length_entry = tk.Entry(root, font=custom_font)
length_entry.pack()


complexity_var = tk.StringVar(value='Medium')
complexity_label = tk.Label(root, text="Complexity Level:", font=custom_font)
complexity_label.pack()
low_radio = tk.Radiobutton(root, text="Low", variable=complexity_var, value='Low', font=custom_font)
medium_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value='Medium', font=custom_font)
high_radio = tk.Radiobutton(root, text="High", variable=complexity_var, value='High', font=custom_font)
low_radio.pack()
medium_radio.pack()
high_radio.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=custom_font)
generate_button.pack()


password_label = tk.Label(root, text="", font=custom_font)
password_label.pack()


root.mainloop()
