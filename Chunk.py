from random import randint, choice
from copy import copy
from math import fabs

from Monsters import *
from Weapon import gen_weapon
from GenDungeon import Dungeon
from Tile import Tile


class Chunk:
    def __init__(self, size):
        self.area = list(list())
        self.size = size
        self.entities = list()

        self.chunk_x, self.chunk_y = 0, 0
        self.start_x, self.start_y = 0, 0

        self.min_level = self.get_min_level()
        self.max_level = self.min_level

        self.dungeon_x = None
        self.dungeon_y = None
        self.dungeon = None

    def upgrade(self):
        self.min_level = self.get_min_level()
        self.max_level = self.min_level + 3

    def get_min_level(self):
        ret = fabs(self.start_x-self.chunk_x) + fabs(self.start_y-self.chunk_y)
        return 1 if ret <= 0 else ret

    def create_dungeon_enter(self):
        self.dungeon_x = randint(2, self.size - 2)
        self.dungeon_y = randint(2, self.size - 2)
        self.area[self.dungeon_x][self.dungeon_y] = Tile(
            "Подземелье", "blue", False
        )
        self.dungeon = Dungeon(self.size, self.min_level)

    def spawn_entities(self):
        m_pack = get_monster_pack()
        for _ in range(randint(10, 20)):
            while True:
                x, y = randint(2, self.size - 2), randint(2, self.size - 2)
                if not self.area[x][y].block and\
                        not self.area[x][y].entity_on_me:
                    break

            self.entities.append(copy(choice(m_pack)))
            self.entities[-1].area = self.area
            self.entities[-1].level = randint(self.min_level, self.max_level)
            self.entities[-1].x, self.entities[-1].y = x, y
            self.entities[-1].update()

    def spawn_weapons(self):
        for _ in range(randint(10, 20)):
            while True:
                x, y = randint(2, self.size - 2), randint(2, self.size - 2)
                if not self.area[x][y].block and not self.area[x][y].item_on_me:
                    break

            self.area[x][y].item_on_me = gen_weapon(randint(self.min_level,
                                                            self.max_level))

    def update(self, player):
        for entity in self.entities:
            entity.move(randint(-1, 1), randint(-1, 1))

        if self.area[player.x][player.y].item_on_me is not None:
            player.inventory.items.append(self.area[player.x][player.y].item_on_me)
            self.area[player.x][player.y].item_on_me = None
