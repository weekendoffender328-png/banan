import math
import random


def calculate_gcd(a, b):
    """Вычисляет наибольший общий делитель (НОД)."""
    return math.gcd(a, b)


def play_gcd_game():
    """Запускает игру 'Наибольший общий делитель'."""
    print("Welcome to the Greatest Common Divisor Game!")
    print("Find the greatest common divisor of given numbers.")

    # Генерация случайных чисел
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print(f"Question: {num1} {num2}")

    # Получение ответа от пользователя
    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    # Вычисление правильного ответа
    correct_answer = calculate_gcd(num1, num2)

    # Проверка ответа
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is '{correct_answer}'")


def main():
    play_gcd_game()


if __name__ == "__main__":
    main()
