import random


def main():
    name = ""
    print("Menu:")
    users_choice = input("> ").upper()
    while users_choice != "Q":
        if users_choice == "G":
            name = get_valid_name()
        elif users_choice == "P":
            print_greeting(name)
        elif users_choice == "S":
            print_secret_name(name)
        else:
            print("Invalid Choice")
        print("Menu:")
        users_choice = input("> ").upper()


def get_valid_name():
    name = input("Enter your name: ")
    while name == "":
        print('Invalid Name')
        name = input("Enter your name: ")
    return name

def print_greeting(name):
    print_line(len(name))
    print(name)
    print_line(len(name))

def print_line(Length):
    print('-' * Length)


def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print(''.join(letters))

main()