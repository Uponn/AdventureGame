class Player:
    def __init__(self):
        self.__name = "John Snow"
        self.__age = 15
        self.__room = ''
        self.__floor = ''

    inventory = []

    def set_floor(self, floor):
        self.__floor = floor

    def set_room(self, room):
        self.__room = room

    def get_room(self):
        return self.__room

    def get_floor(self):
        return self.__floor

    def get_name(self):
        return self.__name

    def take(self, item):
        self.inventory.append(item)

    def get_inventory(self):
        return self.inventory

    def get_age(self):
        return self.__age
