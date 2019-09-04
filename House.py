from Player import Player
from FirstFloor import FirstFloor
from SecondFloor import SecondFloor
from Basement import Basement
from CeilingRoom import CeilingRoom

import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


##########Map###########
# ---------------------
# |      Ceiling      |          Start from l1r2 'doorway'
# |-------------------|
# |l2r1|l2r2|l2r3|l2r4|
# |-------------------|
# |l1r1|l1r2|l1r3|l1r4|
# |-------------------|
# |      Basement     |
# ---------------------

john = Player()
basement = Basement()
first_floor = FirstFloor()
second_floor = SecondFloor()
ceiling = CeilingRoom()

class House:
    def __init__(self):
        clear_screen()
        print("Welcome %s, to The adventures in the old house!!!" %john.get_name())
        time.sleep(1)

    def start(self):
        first_floor.welcome()

