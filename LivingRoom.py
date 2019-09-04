from Room import Room
from Player import Player
from Parser import parser_furniture, parser_items
import time

john = Player()

class LivingRoom(Room):
	furniture = ["couch", "tv", "photo", "fireplace"]
	items = []
	def __init__(self):
		self.__name = "Living Room"
		john.set_room(self.get_name())

	def room_info(self):
		print("You've entered the Living Room, there is an old {}, very old {}, a family {} which is very creepy and a {}"
			.format(*self.furniture))
		self.action()

	def get_name(self):
		return self.__name

	def action(self):
		from FirstFloor import FirstFloor, clear_screen
		first_floor = FirstFloor()
		choice = input("What now: \n>>> ")
		user_choice = parser_furniture(choice, self.furniture)
		if user_choice == "couch":
			print("You couldn't find anything here.")
			time.sleep(1)
			self.action()
		elif user_choice == "tv":
			print("It is just an old broken TV, you couldn't find anything")
			time.sleep(1)
			self.action()
		elif user_choice == "photo":
			print("It is a an old family photo, it is very creepy, you checked if there is anything behind it but "
				"you couldn't find anything")
			time.sleep(1)
			self.action()
		elif user_choice == "fireplace":
			print("You checked inside and around the fireplace but you didn't find anything useful.")
			time.sleep(1)
			self.action()
		elif choice == "leave":
			clear_screen()
			print("You return back to the First Floor")
			first_floor.introduction()
		else:
			self.action()

