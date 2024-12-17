def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Выход")

        choice = input("Введите номер операции (1-5): ")

        if choice == "5":
            print("До свидания!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: Введите числовое значение!")
                continue

            if choice == "1":
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()