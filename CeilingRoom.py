import time

from Player import Player
from Parser import parser_rooms, parser_items, parser_furniture

john = Player()

class CeilingRoom:
	furniture = ("bookshelf", "table", "window", "shelf")
	items = ["key"]

	def welcome(self):
		john.set_floor("ceiling")
		print("Now you are at the ceiling. Here you have a {}, {}, {} and a {}".format(*self.furniture))
		self.introduction()
	def introduction(self):
		from SecondFloor import SecondFloor,clear_screen
		second_floor = SecondFloor()
		choice = input("What now:\n>>> ")
		user_choice = parser_furniture(choice, self.furniture)
		if user_choice == "bookshelf":
			print("There are a lot of old books here but nothing of use.")
			time.sleep(1)
			self.introduction()
		elif user_choice == "table":
			print("There is a paper and ashtray but nothing you could use.")
			time.sleep(1)
			self.introduction()
		elif user_choice == "window":
			print("The window is jammed it doesn't move.")
			time.sleep(1)
			self.introduction()
		elif user_choice == "shelf":
			print("There is a {} on the shelf, it is probably for the basement.".format(*self.items))
			choice = input("What would you like to do with it?:\n>>> ")
			user_choice = parser_items(choice, self.items)
			if user_choice == "key" or choice == "yes":
				print("You took the key.")
				john.take(*self.items)
				time.sleep(2)
				choice = input("Would you like to go downstairs to the Second Floor?(y/n)")
				choice = choice.lower().strip()
				if choice == "y" or "yes":
					clear_screen()
					print("You return back to the Second Floor.")
					second_floor.introduction()
			else:
				self.introduction()
		else:
			self.introduction()
