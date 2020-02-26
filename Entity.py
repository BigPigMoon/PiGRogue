import re

from bearlibterminal import terminal


class Entity:
    def __init__(self, area, level, name, color, hp, damage, dam_resist, x=0, y=0):
        self.x = x
        self.y = y
        self.area = area
        # свойства который идут из json
        self.name = name
        self.level = level
        self.hp = level * hp
        self.xp = self.level
        self.damage = self.level * damage
        self.damage_resistance = dam_resist
        # for drawing
        self.layer = 10
        self.color = color
        try:
            self.char = re.search(r'[A-Z]', name).group(0)
        except AttributeError:
            self.char = name[-1]

    def draw(self, x, y):
        terminal.layer(self.layer)
        terminal.color(self.color)
        if self.x - x < 50 and self.y - y < 50:
            terminal.put(self.x - x, self.y - y, self.char)
        terminal.color("white")
        terminal.layer(0)

    def block_move(self):
        try:
            return self.area[self.x][self.y].block
        except IndexError:
            return False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

        if self.block_move():
            self.x -= dx
            self.y -= dy
