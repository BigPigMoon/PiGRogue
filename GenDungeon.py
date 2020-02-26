"""Алгоритм генерации Этажа."""
import random

from Tile import Tile
from Floor import Floor
from ScanWall import scan_wall, choise_wall
from Rect import Rect


class Dungeon:
    def __init__(self, size):
        self.floors = list()
        self.floor_num = 0
        self.floor_size = size
        self.max_floor_num = random.randint(3, 8)
        for i in range(self.max_floor_num):
            self.create_level(i)

    def create_level(self, num_iter):
        """Сборная солянка из функций."""
        floor = [
            [Tile("wall#", "white", True) for _ in range(self.floor_size)]
            for _ in range(self.floor_size)
        ]

        start = self.create_start()
        start.dig_me(floor)
        first_room = self.create_first_room(start, floor)

        rooms = [first_room]
        tonels = []
        self.create_main(rooms, tonels, floor)
        rooms.remove(first_room)

        if num_iter == self.max_floor_num - 1:
            end = Rect(-1, -1, 0, 0)
        else:
            end = self.create_end(rooms, floor)
        rooms.append(first_room)

        floor[end.x1][end.y1] = Tile("eXit", "blue", False)
        floor[start.x1][start.y1] = Tile("Enter", "blue", False)

        self.floors.append(Floor(floor, start, end, rooms, self.floor_size))
        self.floors[-1].spawn_entities()

    def create_main(self, rooms, tonels, floor):
        """Главный Алгоритм который создает уровень(этаж)."""
        for i in range(self.floor_size):  # Число модов
            failed = False
            while not failed:
                w = random.randint(3, 6)
                h = random.randint(3, 6)
                direct = random.randint(1, 4)
                if i % 3 != 0:  # Две комнаты на один тонель
                    # Делаем комнату
                    tonel = random.choice(tonels + rooms)
                    wall = choise_wall(direct, tonel)
                    door = self.create_tonel(direct, wall, 1, 1)

                    wall_door = choise_wall(direct, door)
                    new_room = self.create_room(direct, wall_door, h, w)
                    if new_room.x1 <= 0 or new_room.x2 >= self.floor_size:
                        continue
                    if new_room.y1 <= 0 or new_room.y2 >= self.floor_size:
                        continue
                else:
                    # Делаем тонель
                    room = random.choice(rooms + tonels)
                    wall = choise_wall(direct, room)
                    new_tonel = self.create_tonel(direct, wall, w+2, h + 2)
                    if new_tonel.x1 <= 0 or new_tonel.x2 >= self.floor_size:
                        continue
                    if new_tonel.y1 <= 0 or new_tonel.y2 >= self.floor_size:
                        continue

                if direct in {1, 3}:
                    # UP and DOWN
                    if i % 3 != 0:
                        # Сканируем комнату
                        wall = [
                            [x for x in range(new_room.x1-1, new_room.x2+1)],
                            wall[1]
                        ]
                        depth = max(new_room.y1, new_room.y2) - min(new_room.y1, new_room.y2) + 3
                        if scan_wall(direct, wall, depth, floor):
                            door.dig_me(floor)
                            new_room.dig_me(floor)
                            rooms.append(new_room)
                            failed = True
                    else:
                        # Сканируем тонель
                        wall = [
                            [x for x in range(new_tonel.x1-1, new_tonel.x1+2)],
                            wall[1]
                        ]
                        depth = max(new_tonel.y1, new_tonel.y2) - min(new_tonel.y1, new_tonel.y2) + 3
                        if scan_wall(direct, wall, depth, floor):
                            new_tonel.dig_me(floor)
                            tonels.append(new_tonel)
                            failed = True
                if direct in {2, 4}:
                    # LEFT and RIGHT
                    if i % 3 != 0:
                        # Сканируем комнату
                        wall = [
                            wall[0],
                            [y for y in range(new_room.y1-1, new_room.y2+1)]
                        ]
                        depth = max(new_room.x1, new_room.x2) - min(new_room.x1, new_room.x2) + 3
                        if scan_wall(direct, wall, depth, floor):
                            door.dig_me(floor)
                            new_room.dig_me(floor)
                            rooms.append(new_room)
                            failed = True
                    else:
                        # Сканируем тонель
                        wall = [
                            wall[0],
                            [y for y in range(new_tonel.y1-1, new_tonel.y1+2)]
                        ]
                        depth = max(new_tonel.x1, new_tonel.x2) - min(new_tonel.x1, new_tonel.x2) + 3
                        if scan_wall(direct, wall, depth, floor):
                            new_tonel.dig_me(floor)
                            tonels.append(new_tonel)
                            failed = True

    def create_first_room(self, start, floor):
        """Генерит начальную комнату."""
        def check_outside():
            """Вспомогательная функция.

            Проверяет не вышла ли первая комната за пределы карты.
            """
            if (self.floor_size - 1 > room.x1 > 1 and
                self.floor_size - 1 > room.x2 > 1 and
                self.floor_size - 1 > room.y1 > 1 and
                    self.floor_size - 1 > room.y2 > 1):
                room.dig_me(floor)
                return True
            return False

        first_room = False
        while not first_room:
            direct = random.randint(1, 4)
            w = random.randint(3, 6)
            h = random.randint(3, 6)

            if direct in {1, 3}:
                mid = int(w/2)

                if direct == 3:
                    if scan_wall(
                            direct,
                            [
                                [x for x in range(start.x1-mid, start.x1+mid)],
                                start.y1 + 1
                            ], h + 1, floor
                    ):
                        room = Rect(start.x1 - mid, start.y1 + 1, w, h)
                        first_room = check_outside()
                else:
                    if scan_wall(
                            direct,
                            [
                                [x for x in range(start.x1-mid, start.x1+mid)],
                                start.y1
                            ], h + 1, floor
                    ):
                        room = Rect(start.x1 - mid, start.y1 - h, w, h)
                        first_room = check_outside()
            if direct in {2, 4}:
                mid = int(h/2)
                if direct == 2:
                    if scan_wall(
                            direct,
                            [
                                start.x1 + 1,
                                [y for y in range(start.y1-mid, start.y1+mid)]
                            ], w + 1, floor
                    ):
                        room = Rect(start.x1 + 1, start.y1 - mid, w, h)
                        first_room = check_outside()
                else:
                    if scan_wall(
                            direct,
                            [
                                start.x1,
                                [y for y in range(start.y1-mid, start.y1+mid)]
                            ], w+1, floor
                    ):
                        room = Rect(start.x1 - w, start.y1 - mid, w, h)
                        first_room = check_outside()

        return room

    @staticmethod
    def create_room(direct, wall, h, w):
        """Создает комнату."""
        if direct == 1:
            # UP
            x = random.choice(wall[0])
            y = wall[1]
            return Rect(x - w // 2, y - h, w, h)

        if direct == 2:
            # RIGHT
            x = wall[0]
            y = random.choice(wall[1])
            return Rect(x, y - h // 2, w, h)

        elif direct == 3:
            # DOWN
            x = random.choice(wall[0])
            y = wall[1]
            return Rect(x - w // 2, y, w, h)

        elif direct == 4:
            # LEFT
            x = wall[0]
            y = random.choice(wall[1])
            return Rect(x - w, y - h // 2, w, h)

    @staticmethod
    def create_tonel(direct, wall, w, h):
        """Создает тонель."""
        if direct in {1, 3}:
            if len(wall[0]) > 2:
                wall[0] = wall[0][1:-1]
        elif direct in {2, 4}:
            if len(wall[1]) > 2:
                wall[1] = wall[1][1:-1]

        if direct == 1:
            # UP
            x = random.choice(wall[0])
            y = wall[1]
            return Rect(x - 1 // 2, y - h, 1, h)

        if direct == 2:
            # RIGHT
            x = wall[0]
            y = random.choice(wall[1])
            return Rect(x, y - 1 // 2, w, 1)

        elif direct == 3:
            # DOWN
            x = random.choice(wall[0])
            y = wall[1]
            return Rect(x - 1 // 2, y, 1, h)

        elif direct == 4:
            # LEFT
            x = wall[0]
            y = random.choice(wall[1])
            return Rect(x - w, y - 1 // 2, w, 1)

    def create_start(self):
        """Создает начальную точку от которой будут строится комнаты.

        Если x и y это None координаты будут рандомными иначе заданные.

        Возвращает Rect
        """
        x = random.randint(10, self.floor_size - 10)
        y = random.randint(10, self.floor_size - 10)

        start = Rect(x, y, 1, 1)

        return start

    def create_end(self, rooms, floor):
        """Создает конец в рандомной комнате.

        Возвращает Rect.
        """
        failed = False
        while not failed:
            end_room = random.choice(rooms)
            direct = random.randint(1, 4)
            wall = choise_wall(direct, end_room)
            if scan_wall(direct, wall, 2, floor):
                end = self.create_tonel(direct, wall, 1, 1)
                end.dig_me(floor)
                failed = True
        return end
