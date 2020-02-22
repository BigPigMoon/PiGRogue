from bearlibterminal import terminal

from Map import Chunk

from GenDungeon import Dungeon

class View():
    def __init__(self, player):
        self.w = 50
        self.h = 50
        self.player = player

        self.update()

    def update(self):
        self.x = self.player.x - self.w // 2 + 1
        self.y = self.player.y - self.h // 2 + 1

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def draw(self, chunk):
        x = 0
        y = 0
        terminal.layer(1)

        if self.x > chunk.size - self.w:
            self.x = chunk.size - self.w
        if self.y > chunk.size - self.h:
            self.y = chunk.size - self.h

        for j in range(self.y, self.h + self.y):
            for i in range(self.x, self.w + self.x):
                cell = chunk.area[i][j]
                terminal.color(cell.color)
                terminal.put(x, y, cell.type[0].upper())
                x += 1
            y += 1
            x = 0

        terminal.color("white")
        terminal.layer(0)

        self.player.draw(self.x, self.y)
