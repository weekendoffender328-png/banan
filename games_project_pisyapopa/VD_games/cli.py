def welcome_user():
    """Приветствует пользователя и запрашивает имя."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name
