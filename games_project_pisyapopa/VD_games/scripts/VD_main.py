def main():
    print("Welcome to VD Games!")
    print("Available games:")
    print("1. Welcome Game (vd-main)")
    print("2. Even Number Game (vd-even)")
    print("3. Exit")
    
    choice = input("Select game (1-3): ")
    
    if choice == "1":
        from . import VD_games
        VD_games.welcome()
    elif choice == "2":
        from .VD_even import main as even_main
        even_main()
    else:
        print("Goodbye!")
