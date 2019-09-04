from Room import Room
from Player import Player
from Parser import parser_furniture, parser_items
import time


john = Player()


class OfficeRoom(Room):
	furniture = ["desk", "chair", "cabinet", "bookshelf"]
	items = ["letter"]
	def __init__(self):
		self.__name = "Office"
		john.set_room(self.get_name())

	def room_info(self):
		print(
			"You've entered the Office Room there are a lot of books scattered here. You can see a {}, {}, {} and {}".format(
				*self.furniture))
		self.action()

	def get_name(self):
		return self.__name

	def action(self):
		from FirstFloor import FirstFloor,clear_screen
		first_floor = FirstFloor()
		choice = input("What now: \n>>> ")
		user_choice = parser_furniture(choice, self.furniture)
		if user_choice == "desk":
			print("You went to the desk, there seems to be nothing useful here.")
			time.sleep(1)
			self.action()
		elif user_choice == "chair":
			print("That is just some wooden chair, what did you expect?")
			time.sleep(1)
			self.action()
		elif user_choice == "bookshelf":
			choice = input("There is an {} here, would you like to take it?".format(*self.items) + "(y/n).\n>>> ")
			choice = choice.lower().strip()
			rebel = parser_items(choice, self.items)
			if (choice == "y" or choice == "yes") or rebel == "letter":
				john.take(self.items)
				self.items.remove("letter")
				self.action()
			elif choice == "n" or choice == "no":
				self.action()
		elif user_choice == "cabinet":
			print("You open the cabinet and there is an bottle of some kind of alcohol but since you are {}".format(john.get_age()) + " you cannot do anything with it!!!")
			time.sleep(1)
			self.action()
		elif choice == "leave":
			clear_screen()
			print("You return back to the First Floor")
			first_floor.introduction()
		else:
			self.action()


