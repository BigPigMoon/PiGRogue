from bearlibterminal import terminal


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.status = -1

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

    def block_move(self, area):
        try:
            return area.area[self.x][self.y].block
        except IndexError:
            return False

    def move(self, dx, dy, area):
        self.x += dx
        self.y += dy

        if self.block_move(area):
            self.x -= dx
            self.y -= dy

    def check_dungeon(self, chunk):
        dungeon = chunk.dungeon

        if self.x == chunk.dungeon_x and self.y == chunk.dungeon_y:
            self.status += 1
            self.x = dungeon.floors[self.status].start.x1
            self.y = dungeon.floors[self.status].start.y1
            self.droper(dungeon.floors[self.status].area)

        if self.status >= 0:
            floor = dungeon.floors[self.status]

            if self.x == floor.end.x1 and self.y == floor.end.y1:
                self.status += 1
                if self.status > dungeon.max_floor_num - 1:
                    self.status = dungeon.max_floor_num - 1
                self.x = dungeon.floors[self.status].start.x1
                self.y = dungeon.floors[self.status].start.y1
                self.droper(dungeon.floors[self.status].area)

            if self.x == floor.start.x1 and self.y == floor.start.y1:
                self.status -= 1

                if self.status == -1:
                    self.x = chunk.dungeon_x
                    self.y = chunk.dungeon_y
                    self.droper(chunk.area)
                else:
                    self.x = dungeon.floors[self.status].end.x1
                    self.y = dungeon.floors[self.status].end.y1
                    self.droper(dungeon.floors[self.status].area)

    def droper(self, area):
        if area[self.x][self.y + 1].block is False:
            self.y += 1
        elif area[self.x][self.y - 1].block is False:
            self.y -= 1
        elif area[self.x + 1][self.y].block is False:
            self.x += 1
        elif area[self.x - 1][self.y].block is False:
            self.x -= 1
