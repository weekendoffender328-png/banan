import random


def is_even(number):
    return number % 2 == 0


def play_even_game():
    print("Welcome to the Even Number Game!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    number = random.randint(1, 100)
    print(f"Question: {number}")

    user_answer = input("Your answer: ").strip().lower()
    correct_answer = "yes" if is_even(number) else "no"

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! Correct answer is '{correct_answer}'")


def main():
    play_even_game()


if __name__ == "__main__":
    main()
