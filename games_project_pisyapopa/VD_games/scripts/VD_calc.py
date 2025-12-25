import operator
import random


def calculate_expression(num1, num2, operation):
    """Вычисляет результат математического выражения."""
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    return operations[operation](num1, num2)


def play_calc_game():
    """Запускает игру 'Калькулятор'."""
    print("Welcome to the Calculator Game!")
    print("What is the result of the expression?")

    # Генерация случайного выражения
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(["+", "-", "*"])

    print(f"Question: {num1} {operation} {num2}")

    # Получение ответа от пользователя
    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    # Вычисление правильного ответа
    correct_answer = calculate_expression(num1, num2, operation)

    # Проверка ответа
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is '{correct_answer}'")


def main():
    play_calc_game()


if __name__ == "__main__":
    main()
