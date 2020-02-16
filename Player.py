from bearlibterminal import terminal

from View import View


class Player():
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, x, y):
        terminal.layer(10)
        terminal.put(self.x - x, self.y - y, '@')
        terminal.layer(0)

    def clear(self):
        terminal.layer(10)
        terminal.put(self.x, self.y, ' ')
        terminal.layer(0)
