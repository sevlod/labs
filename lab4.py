import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = 12
    chars = ""

    if lowercase_var.get():
        chars += string.ascii_lowercase
    if digits_var.get():
        chars += string.digits
    if special_var.get():
        chars += "!@#$%"

    if not chars:
        messagebox.showerror("Ошибка", "Выберите хотя бы один параметр!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_label.config(text=f"Сгенерированный пароль: {password}")


root = tk.Tk()
root.title("Генератор паролей")
root.geometry("400x300")

title_label = tk.Label(root, text="Генератор паролей", font=("Arial", 16))
title_label.pack(pady=10)

lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

lowercase_check = tk.Checkbutton(root, text="Включить алфавит нижнего регистра [a-z]", variable=lowercase_var)
lowercase_check.pack(anchor="w", padx=20)

digits_check = tk.Checkbutton(root, text="Включить цифры [0-9]", variable=digits_var)
digits_check.pack(anchor="w", padx=20)

special_check = tk.Checkbutton(root, text="Включить спецсимволы [! @ # $ %]", variable=special_var)
special_check.pack(anchor="w", padx=20)

generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
password_label.pack(pady=10)

root.mainloop()
