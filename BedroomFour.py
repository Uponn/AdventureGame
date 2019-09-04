import time

from Room import Room
from Player import Player
from Parser import parser_furniture, parser_items
john = Player()


class FamilyRoom(Room):
	furniture = ("couch", "tv", "table", "toys")
	items = ["knife"]
	def __init__(self):
		self.__name = "Family Room"
		john.set_room(self.get_name())

	def room_info(self):
		print("This seems to be a family room, looks a lot like the Living Room. There is a {}, a {}, {} and a lot of {}.".format(*self.furniture))
		self.action()

	def get_name(self):
		return self.__name

	def action(self):
		from SecondFloor import SecondFloor, clear_screen
		second_floor = SecondFloor()
		choice = input("What now:\n>>> ")
		user_choice = parser_furniture(choice, self.furniture)
		if user_choice == "couch":
			print("You sit on the couch to catch your breath.")
			time.sleep(2)
			print("5 minutes later.")
			time.sleep(1)
			print("There is nothing really useful on the couch for you to take.")
			self.action()
		elif user_choice == "tv":
			print("Same as the the one in the Living Room, nothing to loot either.")
			time.sleep(1)
			self.action()
		elif user_choice == "table":
			print("There is a rusty {} on the table.".format(*self.items))
			choice = input("Would you like to take it just in case?:\n>>> ")
			user_choice = parser_items(choice, self.items)
			if user_choice == "knife" or choice == "yes":
				print("You took the knife.")
				john.take(self.items)
				self.items.remove("knife")
				self.action()
			else:
				self.action()
		elif user_choice == "toys":
			print("A lot of scattered toys around the ground, but none look useful.")
			time.sleep(1)
			self.action()
		elif choice == "leave":
			clear_screen()
			print("You return back to the Second Floor")
			second_floor.introduction()
		else:
			self.action()
