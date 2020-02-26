from random import randint

from Tile import Tile
from Chunk import Chunk


class Map:
    def __init__(self):
        self.chunk_num = 5
        self.chunk_size = 128
        self.world = [
            [Chunk(self.chunk_size) for _ in range(self.chunk_num)]
            for _ in range(self.chunk_num)
        ]

        self.create_world()

    def create_world(self):
        for i in range(self.chunk_num):
            for j in range(self.chunk_num):
                self.world[i][j].area = [
                    [Tile("Grass", "white", False)
                     for _ in range(self.chunk_size)]
                    for _ in range(self.chunk_size)
                ]

        for i in range(self.chunk_num):
            for j in range(self.chunk_num):
                for _ in range(int(0.46875 * self.chunk_size)):
                    self.create_area(
                        Tile("Tree", "green", False),
                        2, i, j
                    )

                for _ in range(int(self.chunk_size * 0.0234375)):
                    self.create_area(
                        Tile("Lake", "blue", True),
                        4, i, j
                    )
                if randint(0, 1):
                    self.world[i][j].create_dungeon_enter()

                # self.world[i][j].spawn_entities()

    def create_area(self, tile, radius, chunk_x, chunk_y):
        i = randint(0, self.chunk_size)
        j = randint(0, self.chunk_size)

        if radius == 1:
            radius = 2

        for _ in range(100):
            chunk = self.world[chunk_x][chunk_y].area

            n = randint(1, radius)
            w = randint(1, radius)
            e = randint(1, radius)
            s = randint(1, radius)
            try:
                if n == 1:
                    i -= 1
                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j] = tile

                if s == 1:
                    i += 1
                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j] = tile

                if w == 1:
                    j -= 1
                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j] = tile

                if e == 1:
                    j += 1
                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j] = tile
            except IndexError:
                print("ERROR: landspace generator")

    def check_i_j(self, i, j, chunk, chunk_x, chunk_y):
        if i >= self.chunk_size:
            chunk_x += 1

            if chunk_x + 1 > self.chunk_num:
                chunk_x = 0
            chunk = self.world[chunk_x][chunk_y].area
            i = 0

        if j >= self.chunk_size:
            chunk_y += 1
            if chunk_y + 1 > self.chunk_num:
                chunk_y = 0

            chunk = self.world[chunk_x][chunk_y].area
            j = 0

        if i < 0:
            chunk_x -= 1
            if chunk_x < 0:
                chunk_x = self.chunk_num - 1

            chunk = self.world[chunk_x][chunk_y].area
            i = self.chunk_size - 1

        if j < 0:
            chunk_y -= 1
            if chunk_y < 0:
                chunk_y = self.chunk_num - 1

            chunk = self.world[chunk_x][chunk_y].area
            j = self.chunk_size - 1

        return i, j, chunk
