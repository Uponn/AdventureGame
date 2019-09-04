from Room import Room
from Player import Player
from Parser import parser_furniture, parser_items
import time

john = Player()


class DiningRoom(Room):
	furniture = ("table", "chairs", "chair")
	def __init__(self):
		self.__name = "Dining Room"
		john.set_room(self.get_name())

	def get_name(self):
		return self.__name

	def room_info(self):
		print("You've entered the Dining Room, an old {} broken down is on the floor with couple of broken {} "
		      "around it.".format(*self.furniture) + " Overall the room seems like it doesn't have anything to loot.")
		self.action()

	def action(self):
		from FirstFloor import FirstFloor, clear_screen
		first_floor = FirstFloor()
		choice = input("What now:\n>>> ")
		user_choice = parser_furniture(choice, self.furniture)
		if user_choice == "table":
			print("There is nothing, on or around the broken table")
			time.sleep(1)
			self.action()
		elif user_choice == "chair" or user_choice == "chairs":
			print("It is just bunch of broken chairs, what did you expect to find here?")
			time.sleep(1)
			self.action()
		elif choice == "leave":
			clear_screen()
			print("You return back to the First Floor")
			first_floor.introduction()
		else:
			self.action()