import random

def guess_number_game():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("Игра 'Угадай число'!")
    print("Загадано число от 1 до 10. У вас есть 3 попытки, чтобы его угадать.")

    for i in range(attempts):
        try:
            guess = int(input(f"Попытка {i+1}: Введите число: "))
        except ValueError:
            print("Ошибка! Введите целое число.")
            continue

        if guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number} с {i+1}-й попытки!")
            break
        elif i < attempts - 1:
            print("Неправильно. Попробуйте ещё раз.")
        else:
            print(f"Вы проиграли! Загаданное число было: {secret_number}")

if __name__ == "__main__":
    guess_number_game()
