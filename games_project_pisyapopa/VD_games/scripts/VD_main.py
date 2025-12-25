def main():
    print("Welcome to VD Games!")
    print("Available games:")
    print("1. Welcome Game (vd-main)")
    print("2. Even Number Game (vd-even)")
    print("3. Calculator Game (vd-calc)")
    print("4. GCD Game (vd-gcd)")
    print("5. Exit")

    choice = input("Select game (1-5): ")

    if choice == "1":
        from . import VD_games

        VD_games.welcome()
    elif choice == "2":
        from .VD_even import main as even_main

        even_main()
    elif choice == "3":
        from .VD_calc import main as calc_main

        calc_main()
    elif choice == "4":
        from .VD_gcd import main as gcd_main

        gcd_main()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
