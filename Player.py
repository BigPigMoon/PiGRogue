from bearlibterminal import terminal

from Inventory import Inventory


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.status = -1
        self.area = None

        self.name = "BigPigMoon"
        self.hp = 100
        self.damage = 1
        self.level = 1
        self.damage_resistance = 0.5

        self.inventory = Inventory()

    def draw(self, x, y):
        terminal.layer(10)
        terminal.color("red")
        terminal.put(self.x - x, self.y - y, '@')
        terminal.color("white")
        terminal.layer(0)

    def sit_down_tile(self):
        try:
            self.area[self.x][self.y].entity_on_me = self
        except IndexError as e:
            try:
                self.area[0][self.y].entity_on_me = self
            except IndexError as e:
                self.area[self.x][0].entity_on_me = self

    def stand_up_tile(self):
        self.area[self.x][self.y].entity_on_me = None

    def block_move(self):
        try:
            if self.x < 0 or self.y < 0:
                return False
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

        self.sit_down_tile()

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
        # TODO исправить is False на not
        self.stand_up_tile()
        if area[self.x][self.y + 1].block is False:
            self.y += 1
        elif area[self.x][self.y - 1].block is False:
            self.y -= 1
        elif area[self.x + 1][self.y].block is False:
            self.x += 1
        elif area[self.x - 1][self.y].block is False:
            self.x -= 1
        self.sit_down_tile()
