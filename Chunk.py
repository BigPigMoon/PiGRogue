from random import randint

from Monsters import *
from GenDungeon import Dungeon
from Tile import Tile


class Chunk:
    def __init__(self, size):
        self.area = list(list())
        self.size = size
        self.entities = list()

        self.dungeon_x = None
        self.dungeon_y = None
        self.dungeon = None

    def create_dungeon_enter(self):
        # TODO пофиксить импорт класса из модуля GenDungeon

        self.dungeon_x = randint(2, self.size - 2)
        self.dungeon_y = randint(2, self.size - 2)
        self.area[self.dungeon_x][self.dungeon_y] = Tile(
            "Dungeon", "red", False
        )
        self.dungeon = Dungeon(self.size)

    def spawn_entities(self):
        for _ in range(randint(20, 40)):
            x, y = randint(2, self.size), randint(2, self.size)
            self.entities.append(Animal(self.area, "Bear", x, y))

    def update(self):
        for entity in self.entities:
            entity.move(randint(-1, 1), randint(-1, 1))
