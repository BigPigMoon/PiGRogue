import re

from bearlibterminal import terminal


class Entity:
    def __init__(self, name, color, hp, damage, dam_resist, x=0, y=0):
        self.x = x
        self.y = y
        self.area = None
        # свойства который идут из json
        self.name = name
        self.level = None
        self.hp = hp
        self.xp = 0
        self.damage = damage
        self.damage_resistance = dam_resist
        # for drawing
        self.color = terminal.color_from_argb(*[int(a) for a in color.split(' ')])
        self.layer = 10
        try:
            self.char = re.search(r'[A-ZА-Я]', name).group(0)
        except AttributeError:
            self.char = name[-1]

    def sit_down_tile(self):
        self.area[self.x][self.y].entity_on_me = self

    def stand_up_tile(self):
        self.area[self.x][self.y].entity_on_me = None

    def update(self):
        self.hp *= self.level
        self.damage *= self.level
        self.damage_resistance *= self.level
        self.xp = self.hp * self.damage * self.level * 0.1
        self.sit_down_tile()

    def draw(self, x, y):
        if self.x - x < 50 and self.y - y < 50:
            terminal.layer(1)
            terminal.put(self.x - x, self.y - y, ' ')

            terminal.layer(self.layer)
            terminal.color(self.color)
            terminal.put(self.x - x, self.y - y, self.char)

            terminal.color("white")
            terminal.layer(0)

    def block_move(self):
        try:
            return self.area[self.x][self.y].block
        except IndexError:
            return False

    def move(self, dx, dy):
        self.stand_up_tile()

        self.x += dx
        self.y += dy

        if self.block_move():
            self.x -= dx
            self.y -= dy

        elif self.x < 0 or self.y < 0 or self.x >= len(self.area) or self.y >= len(self.area):
            self.x -= dx
            self.y -= dy

        elif self.area[self.x][self.y].entity_on_me:
            self.x -= dx
            self.y -= dy

        self.sit_down_tile()
