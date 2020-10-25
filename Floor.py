from random import randint, choice
from copy import copy

from Monsters import *
from Weapon import gen_weapon


class Floor:
    """Класс одного уровня(Этажа)."""
    def __init__(self, floor, start, end, rooms, size, min_level):
        self.area = floor
        self.size = size
        self.entities = list()

        self.start = start
        self.end = end
        self.rooms = rooms
        self.min_level = min_level
        self.max_level = len(rooms) // 3 + self.min_level
        self.max_level = 1 if self.max_level <= 0 else self.max_level

        self.spawn_entities()
        self.spawn_weapons()

    def spawn_entities(self):
        m_pack = get_monster_pack()
        for _ in range(randint(len(self.rooms) // 2, len(self.rooms))):
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
        for _ in range(2, randint(len(self.rooms), len(self.rooms) + 3)):
            room = choice(self.rooms)
            while True:
                x, y = room.get_random()
                if not self.area[x][y].item_on_me:
                    self.area[x][y].item_on_me = gen_weapon(
                        randint(self.min_level, self.max_level))
                    break

    def update(self, player):
        for entity in self.entities:
            entity.move(randint(-1, 1), randint(-1, 1))

        if self.area[player.x][player.y].item_on_me is not None:
            player.inventory.items.append(
                self.area[player.x][player.y].item_on_me)
            self.area[player.x][player.y].item_on_me = None
