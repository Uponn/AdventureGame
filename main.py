import time
import os
from House import House

keywords = ["go", "enter", "take", "grab", "show", "map", "quit", "leave"]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()


def about_menu():
    clear_screen()
    print("The story revolves around a boy named John he lost a bet with his friends and he was to enter the "
          "abandoned house in their neighborhood\n\nAuthor: Steliyan Nedev\n")
    time.sleep(5)
    choice = input("Would you like to return to the Main Menu?(yes) or (no): ")
    if choice == 'yes' or 'y':
        clear_screen()
        main_menu()
    else:
        time.sleep(1)
        about_menu()


def help_menu():
    print("Those are the recognized keywords:", format(keywords))
    time.sleep(3)
    print("For interacting with items you should use the 'take', 'grab' or 'use'.\nIf you want to leave a given room, "
          "just type 'leave'.")
    time.sleep(1)
    choice = input("Would you like to return to the Main Menu?(yes) or (no): ")
    if choice == 'yes' or 'y':
        clear_screen()
        main_menu()
    else:
        time.sleep(1)
        help_menu()


def welcome_menu():
    print("#####################################################")
    print("# Hello there player, please choose one of the options:\n1: Play\n2: Help\n3: About\n4: Exit")
    print("#####################################################")


def main_menu():
    welcome_menu()
    choice = input('>>> ')
    choice = choice.lower().strip()
    if choice == '1' or choice == 'play':
        house = House()
        house.start()
    elif choice == '2' or choice == 'help':
        help_menu()
    elif choice == '3' or choice == 'about':
        about_menu()
    elif choice == '4' or choice == 'exit':
        exit()
    else:
        print("This is not a valid option, please try again.")
        time.sleep(1)
        clear_screen()
        main_menu()


main_menu()