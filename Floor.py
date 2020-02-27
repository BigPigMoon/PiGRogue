from random import randint, choice
from copy import copy

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
        m_pack = get_monster_pack()
        for _ in range(randint(len(self.rooms) // 4, len(self.rooms) // 2)):
            x, y = randint(2, self.size - 2), randint(2, self.size - 2)
            while self.area[x][y].block:
                x, y = randint(2, self.size - 2), randint(2, self.size - 2)

            self.entities.append(copy(choice(m_pack)))
            self.entities[-1].area = self.area
            self.entities[-1].level = randint(1, 10)
            self.entities[-1].x, self.entities[-1].y = x, y
            self.entities[-1].update()

    def update(self):
        for entity in self.entities:
            entity.move(randint(-1, 1), randint(-1, 1))
