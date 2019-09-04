from BedroomOne import BedroomOne
from BedroomTwo import BedroomTwo
from BedroomThree import Bathroom
from BedroomFour import FamilyRoom
from CeilingRoom import CeilingRoom
from Player import Player
from Parser import parser_rooms
import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


john = Player()
bedroom_one = BedroomOne()
bedroom_two = BedroomTwo()
bathroom = Bathroom()
family_room = FamilyRoom()
ceiling = CeilingRoom()


class SecondFloor:
    john.set_floor("second")
    rooms = ["master", "kids", "bathroom", "family", "first", "ceiling"]

    def welcome(self):
        clear_screen()
        print(
            "You got up at the Second Floor here you have: {}, {}, {}, {}, {} or the {}."
                .format(bedroom_one.get_name(), bedroom_two.get_name(), bathroom.get_name(), family_room.get_name(),
                        "Staircase to the First Floor", "Staircase to the Ceiling"))
        time.sleep(1)
        self.introduction()

    def introduction(self):
        from FirstFloor import FirstFloor
        first_floor = FirstFloor()

        choice = input("Where would you like to go: \n>>> ")
        user_choice = parser_rooms(choice, self.rooms)
        if user_choice == "master":
            bedroom_one.room_info()
        elif user_choice == "kids":
            bedroom_two.room_info()
        elif user_choice == "bathroom":
            bathroom.room_info()
        elif user_choice == "family":
            family_room.room_info()
        elif user_choice == "first":
            clear_screen()
            print("You are now back to the First Floor")
            first_floor.introduction()
        elif user_choice == "ceiling":
            ceiling.welcome()
        elif choice == "quit" or choice == "exit":
            exit()
        else:
            time.sleep(1)
            self.introduction()
