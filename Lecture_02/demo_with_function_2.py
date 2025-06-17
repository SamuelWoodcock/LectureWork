import random


def main():
    name = "Samuel Woodcock"
    print()
    print_menu()
    choice = input("> ").strip().upper()

    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid Choice. Please select from the menu options.")

        print()
        print_menu()
        choice = input("> ").strip().upper()

    print("Goodbye!")


def print_menu():
    print("Menu:")
    print("G - Get valid name")
    print("P - Print greeting")
    print("S - Print secret name")
    print("Q - Quit")


def print_greeting(name):
    print_line(len(name))
    print(name)
    print_line(len(name))


def get_valid_name():
    name = input("Enter your name: ").strip()
    while name == "":
        print('Invalid Name. Please enter a non-empty name.')
        name = input("Enter your name: ").strip()
    return name


def print_line(length):
    print('-' * length)


def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print(''.join(letters))


if __name__ == "__main__":
    main()

