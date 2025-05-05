import sqlite3
import hashlib
import secrets
import string


def init_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(login):
    password = generate_password()
    password_hash = hash_password(password)
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (login, password_hash) VALUES (?, ?)", (login, password_hash))
        conn.commit()
        print(f"[+] Пользователь '{login}' добавлен.")
        print(f"[!] Сгенерированный пароль: {password}")
    except sqlite3.IntegrityError:
        print(f"[!] Логин '{login}' уже существует.")
    finally:
        conn.close()


def get_password_hash(login):
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE login = ?", (login,))
    result = c.fetchone()
    conn.close()
    if result:
        print(f"[=] Хеш пароля для '{login}': {result[0]}")
    else:
        print(f"[!] Пользователь '{login}' не найден.")


if __name__ == "__main__":
    init_db()
    while True:
        print("\n1 - Добавить пользователя\n2 - Получить хеш по логину\n3 - Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            login = input("Введите логин: ")
            add_user(login)
        elif choice == "2":
            login = input("Введите логин: ")
            get_password_hash(login)
        elif choice == "3":
            break
        else:
            print("[!] Неверный выбор.")
