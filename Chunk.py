from random import randint, choice

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
        self.dungeon_x = randint(2, self.size - 2)
        self.dungeon_y = randint(2, self.size - 2)
        self.area[self.dungeon_x][self.dungeon_y] = Tile(
            "Подземелье", "red", False
        )
        self.dungeon = Dungeon(self.size)

    def spawn_entities(self):
        m_pack = get_monster_pack()
        for _ in range(randint(1, 2)):
            x, y = randint(2, self.size - 2), randint(2, self.size - 2)
            self.entities.append(choice(m_pack))
            self.entities[-1].area = self.area
            self.entities[-1].level = randint(1, 10)
            self.entities[-1].x, self.entities[-1].y = x, y
            self.entities[-1].update()

    def update(self):
        for entity in self.entities:
            entity.move(randint(-1, 1), randint(-1, 1))
