from bearlibterminal import terminal

from Map import Chunk


class Player():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.status = None # "dungeon", ""

    def draw(self, x, y):
        terminal.layer(10)
        terminal.color("red")
        terminal.put(self.x - x, self.y - y, '@')
        terminal.color("white")
        terminal.layer(0)

    def clear(self):
        terminal.layer(10)
        terminal.put(self.x, self.y, ' ')
        terminal.layer(0)
    
    def check_dungeon(self, chunk):
        if type(chunk) == Chunk:
            if self.x == chunk.dungeon_x and self.y == chunk.dungeon_y:
                dungeon = chunk.dungeon

                self.x = dungeon.floors[dungeon.floor_num].start.x1
                self.y = dungeon.floors[dungeon.floor_num].start.y1

                return dungeon.floors[dungeon.floor_num]
        return chunk
