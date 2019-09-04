import time
from Room import Room
from Player import Player
from Parser import parser_furniture




john = Player()


class BedroomOne(Room):
	furniture = ("bed", "closet", "mirror", "mattress")
	def __init__(self):
		self.__name = "Master Bedroom"
		john.set_room(self.get_name())


	def room_info(self):
		print(
			"You've entered the Master Bedroom by the looks of it the mother and the father of the family lived in it."
			"Here you can see a {}, {}, a half broken {} and a {} laying on the floor.".format(*self.furniture))
		self.action()

	def get_name(self):
		return self.__name

	def action(self):
		from SecondFloor import SecondFloor, clear_screen
		second_floor = SecondFloor()
		choice = input("What now:\n>>> ")
		user_choice = parser_furniture(choice, self.furniture)
		if user_choice == "bed":
			print("You are at the bed but there seems to be nothing useful here.")
			time.sleep(1)
			self.action()
		elif user_choice == "closet":
			print("There are some old clothes here, nothing that could be of use.")
			time.sleep(1)
			self.action()
		elif user_choice == "mirror":
			print("You look at the broken mirror, you noticed that there is someone behind you, you startle turn around"
				  "just to see that there is nothing there.")
			time.sleep(1)
			self.action()
		elif user_choice == "mattress":
			print("By the looks of it it is the mattress from the bed, just moved to the ground. Strange, seems like someone has been sleeping here")
			time.sleep(1)
			self.action()
		elif choice == "leave":
			clear_screen()
			print("You return back to the Second Floor")
			second_floor.introduction()
