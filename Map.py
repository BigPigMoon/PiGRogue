from random import randint

from bearlibterminal import terminal


class Map():
    def __init__(self):
        self.chunk_num = 5
        self.chunk_size = 128
        self.world = [
                [Chunk() for _ in range(self.chunk_num)]
                for _ in range(self.chunk_num)
            ]

        self.create_world()

    def create_world(self):
        for i in range(self.chunk_num):
            for j in range(self.chunk_num):
                self.world[i][j].area = [
                    [Tile("grass", "white") for _ in range(self.chunk_size)]
                    for _ in range(self.chunk_size)
                ]
                for _ in range(20):
                    self.create_area(
                        randint(0, self.chunk_size),
                        randint(0, self.chunk_size),
                        "tree", "green", i, j
                    )

    def create_area(self, x, y, tile_type, color, chunk_x, chunk_y):
        i = x
        j = y
        for _ in range(40):
            chunk = self.world[chunk_x][chunk_y].area

            n = randint(1, 3)
            w = randint(1, 3)
            e = randint(1, 3)
            s = randint(1, 3)

            if n == 1:
                i -= 1
                if j >= self.chunk_size:
                    j = 0
                if i >= self.chunk_size:
                    i = 0
                chunk[i][j].type = tile_type
                chunk[i][j].color = color
            if s == 1:
                i += 1
                if i >= self.chunk_size:
                    i = 0
                if j >= self.chunk_size:
                    j = 0
                chunk[i][j].type = tile_type
                chunk[i][j].color = color
            if w == 1:
                j -= 1
                if j >= self.chunk_size:
                    j = 0
                if i >= self.chunk_size:
                    i = 0
                chunk[i][j].type = tile_type
                chunk[i][j].color = color
            if e == 1:
                j += 1
                if j >= self.chunk_size:
                    j = 0
                if i >= self.chunk_size:
                    i = 0
                chunk[i][j].type = tile_type
                chunk[i][j].color = color


class Tile():
    def __init__(self, tile_type, color, objects=[]):
        self.type = tile_type
        self.on_tile = objects
        self.color = color


class Chunk():
    def __init__(self):
        self.area = list(list())
