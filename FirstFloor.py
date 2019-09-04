from Kitchen import Kitchen
from DiningRoom import DiningRoom
from LivingRoom import LivingRoom
from OfficeRoom import OfficeRoom
from SecondFloor import SecondFloor
from Basement import Basement
from Player import Player
from Parser import parser_rooms
import time
import os


def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


john = Player()
kitchen = Kitchen()
dining_room = DiningRoom()
living_room = LivingRoom()
office = OfficeRoom()
second_floor = SecondFloor()
basement = Basement()

class FirstFloor:
	rooms = ["kitchen", "dining", "living", "office", "second", "basement"]
	john.set_floor("first")

	def welcome(self):
		print(
			"You are at the First Floor here you have: {}, {}, {}, "
			"{}, {} and {}. "
				.format(kitchen.get_name(), dining_room.get_name(), living_room.get_name(), office.get_name(),
			            "Staircase to Second Floor", "Staircase to Basement"))
		time.sleep(1)
		self.introduction()


	def introduction(self):
		choice = input("Where would you like to go: \n>>> ")
		user_choice = parser_rooms(choice, self.rooms)
		if user_choice == "kitchen":
			kitchen.room_info()
		elif user_choice == "dining":
			dining_room.room_info()
		elif user_choice == "living":
			living_room.room_info()
		elif user_choice == "office":
			office.room_info()
		elif user_choice == "second":
			second_floor.welcome()
		elif user_choice == "basement":
			if "key" in john.inventory:
				basement.welcome()
			else:
				print("The basement seems to be locked, you would have to find the key in order to enter it.")
				self.introduction()
		elif choice == "quit" or choice == "exit":
			exit()
		else:
			time.sleep(1)
			self.introduction()
