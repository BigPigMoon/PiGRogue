from bearlibterminal import terminal


class ViewMode:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.char = 'X'
        self.chunk = None
        self.mode_bool = False
        self.color = "yellow"

    def set_position(self, px, py, chunk):
        self.x = px
        self.y = py
        self.chunk = chunk

    def draw(self, x, y):
        terminal.layer(15)
        terminal.color(self.color)
        terminal.put(self.x - x, self.y - y, self.char)
        terminal.color("white")
        terminal.layer(0)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

        if self.x < 0 or self.y < 0 or self.y >= self.chunk.size or self.x >= self.chunk.size:
            self.x -= dx
            self.y -= dy

    def print_information(self):
        inform = self.chunk.area[self.x][self.y]
        terminal.printf(51, 1, f"name: {inform.type}")
        if inform.entity_on_me is not None:
            terminal.printf(51, 3, f"entity: {inform.entity_on_me.name}")
            terminal.printf(51, 4, f"hp: {inform.entity_on_me.hp}")
            terminal.printf(51, 5, f"damage: {inform.entity_on_me.damage}")
            terminal.printf(51, 6, f"level: {inform.entity_on_me.level}")
            terminal.printf(
                51, 7,
                f"damage resistance: {inform.entity_on_me.damage_resistance}"
            )
