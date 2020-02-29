from bearlibterminal import terminal


class Dialog:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.x = (100 - self.width) // 2
        self.y = (50 - self.height) // 2

        self.cursor = 0
        self.max_cursor = 0
        self.var_bool = False

    def draw(self):
        for i in range(100):
            terminal.layer(i)
            terminal.clear_area(self.x, self.y, self.width, self.height)
        terminal.layer(100)
        for x in range(1, self.width - 1):
            terminal.put(self.x + x, self.y, '_')

        for y in range(1, self.height):
            terminal.put(self.x, self.y + y, '|')
            terminal.put(self.x + self.width - 1, self.y + y, '|')

        for x in range(1, self.width - 1):
            terminal.put(self.x + x, self.y + self.height - 1, '_')

    def move(self, dx, dy):
        if dy < 0:
            # move cursor up
            self.cursor -= 1
            if self.cursor < 0:
                self.cursor = 0

        if dy > 0:
            # move cursor down
            self.cursor += 1
            if self.cursor > self.max_cursor - 1 and self.max_cursor != 0:
                self.cursor = self.max_cursor - 1
            if self.max_cursor == 0:
                self.cursor = 0

        if dx < 0:
            self.var_bool = False
