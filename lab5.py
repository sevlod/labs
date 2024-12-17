import random

def get_exchange_rate():

    return round(random.uniform(80, 100), 2)

def rub_to_usd(rubles, rate):
    return round(rubles / rate, 2)

def usd_to_rub(dollars, rate):
    return round(dollars * rate, 2)

def main():
    print("=== Конвертер валют: Рубли ↔ Доллары ===")
    exchange_rate = get_exchange_rate()
    print(f"Текущий (гипотетический) курс доллара: 1 USD = {exchange_rate} RUB\n")

    while True:
        print("Выберите действие:")
        print("1. Конвертировать рубли в доллары")
        print("2. Конвертировать доллары в рубли")
        print("3. Выйти из программы")

        choice = input("Введите номер действия (1/2/3): ")

        if choice == "1":
            try:
                rubles = float(input("Введите сумму в рублях: "))
                if rubles < 0:
                    print("Сумма не может быть отрицательной!")
                else:
                    dollars = rub_to_usd(rubles, exchange_rate)
                    print(f"{rubles} RUB = {dollars} USD при курсе {exchange_rate} руб/доллар.\n")
            except ValueError:
                print("Ошибка: Введите корректное число!\n")

        elif choice == "2":
            try:
                dollars = float(input("Введите сумму в долларах: "))
                if dollars < 0:
                    print("Сумма не может быть отрицательной!")
                else:
                    rubles = usd_to_rub(dollars, exchange_rate)
                    print(f"{dollars} USD = {rubles} RUB при курсе {exchange_rate} руб/доллар.\n")
            except ValueError:
                print("Ошибка: Введите корректное число!\n")

        elif choice == "3":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.\n")

if __name__ == "__main__":
    main()
