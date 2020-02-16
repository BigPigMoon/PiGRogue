from bearlibterminal import terminal

from Map import Chunk


class View():
    def __init__(self, player, x=0, y=0):
        self.w = 50
        self.h = 50
        self.x = x
        self.y = y
        self.player = player

    def draw(self, chunk):
        x = 0
        y = 0
        terminal.layer(1)
        for j in range(self.y, self.h + self.y):
            for i in range(self.x, self.w + self.x):
                cell = chunk.area[i][j]
                terminal.color(cell.color)
                terminal.put(x, y, cell.type[0].upper())
                x+= 1
            y += 1
            x = 0

        terminal.color("white")
        terminal.layer(0)

        self.player.draw(self.x, self.y)
