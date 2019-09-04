from Room import Room
from Player import Player
from Parser import parser_furniture, parser_items

john = Player()


class Kitchen(Room):
	furniture = ("stove", "table", "cupboard", "fridge")
	items = ["potion"]
	def __init__(self):
		self.__name = "Kitchen"
		john.set_room(self.get_name())

	def room_info(self):
		print(
			"You've entered the kitchen there is an old rusty {}, a {}, broken down {} and an empty {}.".format(*self.furniture))
		self.action()

	def get_name(self):
		return self.__name

	def action(self):
		from FirstFloor import FirstFloor, clear_screen
		first_floor = FirstFloor()
		choice = input("What now:\n>>> ")
		user_choice = parser_furniture(choice, self.furniture)
		if user_choice == "stove":
			print("Did you think there would be a food or something?")
			self.action()
		elif user_choice == "table":
			print("There is a green {} on the table, it looks very suspicious.".format(*self.items))
			choice = input("What would you like to do with it?:\n>>> ")
			user_choice = parser_items(choice, self.items)
			if user_choice == "potion" or choice == "yes":
				john.take(*self.items)
				print("You took the potion.")
				self.items.remove("potion")
				self.action()
			else:
				self.action()
		elif user_choice == "cupboard":
			print("There are some kitchen accessories here, nothing special")
			self.action()
		elif user_choice == "fridge":
			print("It's an empty fridge with some garbage in it, what did you expect?")
			self.action()
		elif choice == "leave":
			clear_screen()
			print("You return back to the First Floor")
			first_floor.introduction()
		else:
			self.action()