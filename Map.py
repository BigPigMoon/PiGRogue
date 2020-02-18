from random import randint

from bearlibterminal import terminal


class Map():
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
                    [Tile("grass", "white") for _ in range(self.chunk_size)]
                    for _ in range(self.chunk_size)
                ]

        for i in range(self.chunk_num):
            for j in range(self.chunk_num):
                for _ in range(20):
                    self.create_area("tree", "green", i, j)
                
                for _ in range(3):
                    self.create_area("lake", "blue", i, j)

    def create_area(self, tile_type, color, chunk_x, chunk_y):
        i = randint(0, self.chunk_size)
        j = randint(0, self.chunk_size)
        for _ in range(40):
            chunk = self.world[chunk_x][chunk_y].area

            n = randint(1, 3)
            w = randint(1, 3)
            e = randint(1, 3)
            s = randint(1, 3)
            try:
                if n == 1:
                    i -= 1

                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j].type = tile_type
                    chunk[i][j].color = color

                    chunk = self.world[chunk_x][chunk_y].area

                if s == 1:
                    i += 1

                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)

                    chunk[i][j].type = tile_type
                    chunk[i][j].color = color

                    chunk = self.world[chunk_x][chunk_y].area

                if w == 1:
                    j -= 1

                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)

                    chunk[i][j].type = tile_type
                    chunk[i][j].color = color

                    chunk = self.world[chunk_x][chunk_y].area

                if e == 1:
                    j += 1

                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)

                    chunk[i][j].type = tile_type
                    chunk[i][j].color = color

                    chunk = self.world[chunk_x][chunk_y].area
            except IndexError:
                print("EROR: landspace generator")


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
                chukn_y = self.chunk_num - 1

            chunk = self.world[chunk_x][chunk_y].area
            j = self.chunk_size - 1
        
        return i, j, chunk


class Tile():
    def __init__(self, tile_type, color, objects=[]):
        self.type = tile_type
        self.on_tile = objects
        self.color = color


class Chunk():
    def __init__(self, size):
        self.area = list(list())
        self.size = size
