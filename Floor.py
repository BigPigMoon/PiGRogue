from random import randint

from Monsters import *


class Floor:
    """Класс одного уровня(Этажа)."""
    def __init__(self, floor, start, end, rooms, size):
        self.area = floor
        self.size = size
        self.entities = list()

        self.start = start
        self.end = end
        self.rooms = rooms

    def spawn_entities(self):
        for _ in range(randint(20, 40)):
            x, y = randint(2, self.size), randint(2, self.size)
            self.entities.append(Animal(self.area, "Bear", x, y))

    def update(self):
        for entity in self.entities:
            entity.move(randint(-1, 1), randint(-1, 1))