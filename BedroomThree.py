import time

from Room import Room
from Player import Player
from Parser import parser_furniture

john = Player()


class Bathroom(Room):
    furniture = ("sink", "toilet", "shower", "bathtub")

    def __init__(self):
        self.__name = "Bathroom"
        john.set_room(self.get_name())

    def room_info(self):
        print("This seems to be the main Bathroom. There is a {}, a {}, {} with a {}.".format(*self.furniture))
        self.action()

    def get_name(self):
        return self.__name

    def action(self):
        from SecondFloor import SecondFloor, clear_screen
        second_floor = SecondFloor()
        choice = input("What now:\n>>> ")
        user_choice = parser_furniture(choice, self.furniture)
        if user_choice == "sink":
            print("It is an dirty sink, nothing more and nothing for looting.")
            time.sleep(1)
            self.action()
        elif user_choice == "toilet":
            print("Clearly there wouldn't be anything of use from the toiler...")
            time.sleep(1)
            self.action()
        elif user_choice == "shower":
            print("You try to turn it on for your surprise there is a running water, but nothing for looting")
            time.sleep(1)
            self.action()
        elif user_choice == "bathtub":
            print("Just an dirty bathtub")
            time.sleep(1)
            self.action()
        elif choice == "leave":
            clear_screen()
            print("You return back to the Second Floor")
            second_floor.introduction()
        else:
            self.action()
