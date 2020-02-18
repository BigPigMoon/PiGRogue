from bearlibterminal import terminal

from View import View


class Player():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

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
