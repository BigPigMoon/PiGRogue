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
                    [Tile("grass", "white", False) for _ in range(self.chunk_size)]
                    for _ in range(self.chunk_size)
                ]

        for i in range(self.chunk_num):
            for j in range(self.chunk_num):
                for _ in range(int(0.46875 * self.chunk_size)):
                    self.create_area(
                        Tile("tree", "green", False),
                        2, i, j
                        )

                for _ in range(int(self.chunk_size * 0.0234375)):
                    self.create_area(
                        Tile("lake", "blue", True),
                        4, i, j
                        )
                
                self.world[i][j].create_dungeon_enter()

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
                    chunk = self.world[chunk_x][chunk_y].area

                if s == 1:
                    i += 1
                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j] = tile
                    chunk = self.world[chunk_x][chunk_y].area

                if w == 1:
                    j -= 1
                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j] = tile
                    chunk = self.world[chunk_x][chunk_y].area

                if e == 1:
                    j += 1
                    i, j, chunk = self.check_i_j(i, j, chunk, chunk_x, chunk_y)
                    chunk[i][j] = tile
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
    def __init__(self, tile_type, color, block, objects=[]):
        self.type = tile_type
        self.on_tile = objects
        self.color = color
        self.block = block


class Chunk():
    def __init__(self, size):
        self.area = list(list())
        self.size = size
    
    def create_dungeon_enter(self):
        from GenDungeon import Dungeon
        
        self.dungeon_x = 50
        self.dungeon_y = 60
        self.area[self.dungeon_x][self.dungeon_y] = Tile("dungeon", "red", False)
        self.dungeon = Dungeon()


