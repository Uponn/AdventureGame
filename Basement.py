from Player import Player
from Parser import parser_items, parser_furniture
import time

john = Player()


class Basement:
    furniture = ["shelf", "door", "table", "bike"]

    def welcome(self):
        john.set_floor("basement")
        print(
            "Welcome to the basement, aka. The End Game, here you have a {}, {}, {} and a {}.".format(*self.furniture))
        self.introduction()

    def introduction(self):
        print(john.inventory)
        choice = input("What now:\n>>> ")
        user_choice = parser_furniture(choice, self.furniture)
        if user_choice == "shelf":
            print("There is a lot of jars that are rotten.")
            time.sleep(1)
            self.introduction()
        elif user_choice == "table":
            print("There is a paper and ashtray but nothing you could use.")
            time.sleep(1)
            self.introduction()
        elif user_choice == "door":
            print("The door seems to be jammed.")
            time.sleep(1)
            self.introduction()
        elif user_choice == "bike":
            print("It an very old looking rusty bike.")
            time.sleep(1)
            self.introduction()
        elif parser_items(choice, john.inventory) == "potion":
            if "potion" in john.inventory:
                self.smash()
            else:
                print("Seems like you didn't take the potions. Hint: It is located in the Kitchen.")
                self.introduction()
        elif choice == "quit" or "exit":
            exit()
        else:
            self.introduction()

    def smash(self):
        from FirstFloor import clear_screen
        clear_screen()
        time.sleep(1)
        print("You seem to lose consciousness and fall on the ground. Just before you lose consciousness you notice "
              "that you start turning green.")
        time.sleep(2)
        print("While regaining your consciousness you notice that you are unable to control your body and notice that "
              "you've became way bigger. You have the urge to smash everything, so you do and destroy the "
              "house and leave it.")
        time.sleep(1)
        print("The End.")
