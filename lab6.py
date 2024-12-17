import sqlite3
import tkinter as tk
from tkinter import messagebox

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT)''')
    conn.commit()
    conn.close()

def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    if not username or not password:
        messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Успех", "Пользователь зарегистрирован!")
        reg_window.destroy()  # Закрыть окно регистрации
    except sqlite3.IntegrityError:
        messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует!")
    finally:
        conn.close()

def login_user():
    username = login_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Успех", "Успешная авторизация!")
    else:
        messagebox.showerror("Ошибка", "Неправильный логин или пароль!")

def open_registration_window():
    global reg_window, reg_username_entry, reg_password_entry

    reg_window = tk.Toplevel(root)
    reg_window.title("Регистрация")
    reg_window.geometry("300x200")

    tk.Label(reg_window, text="Логин:").pack(pady=5)
    reg_username_entry = tk.Entry(reg_window)
    reg_username_entry.pack(pady=5)

    tk.Label(reg_window, text="Пароль:").pack(pady=5)
    reg_password_entry = tk.Entry(reg_window, show="*")
    reg_password_entry.pack(pady=5)

    tk.Button(reg_window, text="Зарегистрировать", command=register_user).pack(pady=10)

init_db()
root = tk.Tk()
root.title("Авторизация")
root.geometry("300x200")

tk.Label(root, text="Логин:").pack(pady=5)
login_entry = tk.Entry(root)
login_entry.pack(pady=5)

tk.Label(root, text="Пароль:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Войти", command=login_user).pack(pady=5)
tk.Button(root, text="Зарегистрироваться", command=open_registration_window).pack(pady=5)

root.mainloop()
