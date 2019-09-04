import time

from Room import Room
from Player import Player
from Parser import parser_furniture

john = Player()


class BedroomTwo(Room):
    furniture = ("bed", "toys", "horse", "doll")

    def __init__(self):
        self.__name = "Kids Bedroom"
        john.set_room(self.get_name())

    def room_info(self):
        print("By the looks of it this bedroom was used from the child of the family. "
              "Here you can see a {}, a lots of {}, a rocking {} and a creepy looking {} on the bed.".format(*self.furniture))
        self.action()

    def get_name(self):
        return self.__name

    def action(self):
        from SecondFloor import SecondFloor, clear_screen
        second_floor = SecondFloor()
        choice = input("What now:\n>>> ")
        user_choice = parser_furniture(choice, self.furniture)
        if user_choice == "bed":
            print("Nothing our of the ordinary, just the creepy looking doll. But nothing that would be of use to you.")
            time.sleep(1)
            self.action()
        elif user_choice == "toys":
            print("Just some creepy old toys, they are of no use to you.")
            time.sleep(1)
            self.action()
        elif user_choice == "horse":
            print("You remember that you've watched a horror movie yesterday where the rocking horse started moving "
                  "on its own so you get worried.")
            time.sleep(1)
            self.action()
        elif user_choice == "doll":
            print("The doll is legit creepy so you just put her under the bed.")
            time.sleep(1)
            self.action()
        elif choice == "leave":
            clear_screen()
            print("You return back to the Second Floor")
            second_floor.introduction()
        else:
            self.action()
