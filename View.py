import re

from bearlibterminal import terminal


class View:
    def __init__(self, player):
        self.w = 50
        self.h = 50
        self.x = 0
        self.y = 0
        self.player = player
        self.target = player

        self.update()

    def update(self):
        self.x = self.target.x - self.w // 2 + 1
        self.y = self.target.y - self.h // 2 + 1

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def draw(self, chunk):
        """Рисует все что должен видеть игрок.

        слои
            1 -- карта
            10 -- игрок
        """
        terminal.layer(1)

        if self.x > chunk.size - self.w:
            self.x = chunk.size - self.w
        if self.y > chunk.size - self.h:
            self.y = chunk.size - self.h

        x = 0
        y = 0
        for j in range(self.y, self.h + self.y):
            for i in range(self.x, self.w + self.x):
                cell = chunk.area[i][j]
                terminal.color(cell.color)
                try:
                    char = re.search(r'[А-ЯA-Z]', cell.type).group(0)
                except AttributeError:
                    char = cell.type[-1]
                terminal.put(x, y, char)
                x += 1
            y += 1
            x = 0

        terminal.color("white")
        terminal.layer(0)

        for entity in chunk.entities:
            entity.draw(self.x, self.y)

        self.player.draw(self.x, self.y)
