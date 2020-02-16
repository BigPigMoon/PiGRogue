from bearlibterminal import terminal


class Player():
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self):
        terminal.layer(10)
        terminal.put(self.x, self.y, '@')
        terminal.layer(1)
        terminal.put(self.x, self.y, ' ')
        terminal.layer(0)

    def clear(self):
        terminal.layer(10)
        terminal.put(self.x, self.y, ' ')
        terminal.layer(0)
