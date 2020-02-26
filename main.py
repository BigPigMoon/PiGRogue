from bearlibterminal import terminal

from Player import Player
from Chunk import Chunk
from Map import Map
from View import View


class Game:
    def __init__(self):
        self.turn_counter = -1
        self.game_flag = True

        self.player = Player(45, 55)

        self.view = View(self.player)
        self.map = Map()

        self.chunk_size = self.map.chunk_size
        self.chunk_x = 2
        self.chunk_y = 2
        self.load_chunk = self.map.world[self.chunk_x][self.chunk_y]

        self.main()

    def main(self):
        terminal.open()
        terminal.set("GameSettings.ini")

        while self.game_flag:
            if self.game_input():
                self.turn_counter += 1

                if self.player.status == -1:
                    self.load_chunk.update()
                else:
                    self.load_chunk.dungeon.floors[self.player.status].update()

            if self.player.status == -1:
                self.view.draw(self.load_chunk)
            else:
                self.view.draw(
                    self.load_chunk.dungeon.floors[self.player.status]
                )
                terminal.printf(52, 5, f"floor {self.player.status + 1}")

            self.player.check_dungeon(self.load_chunk)

            self.view.update()

            terminal.printf(52, 1, f"{self.view.x=}\n{self.view.y=}")
            terminal.printf(52, 3, f"{self.player.x=}\n{self.player.y=}")

            terminal.refresh()
            terminal.clear()

        terminal.close()

    def update_chunk(self, chunk_x, chunk_y):
        num_chunk = self.map.chunk_num

        if chunk_x == 0:
            self.chunk_y += chunk_y

            if chunk_y > 0:
                self.view.y = 0
            else:
                self.view.y = self.chunk_size - self.view.h

        elif chunk_y == 0:
            self.chunk_x += chunk_x

            if chunk_x > 0:
                self.view.x = 0
            else:
                self.view.x = self.chunk_size - self.view.w

        if self.chunk_x < 0:
            self.chunk_x = num_chunk - 1
        if self.chunk_x > num_chunk - 1:
            self.chunk_x = 0
        if self.chunk_y < 0:
            self.chunk_y = num_chunk - 1
        if self.chunk_y > num_chunk - 1:
            self.chunk_y = 0

        self.load_chunk = self.map.world[self.chunk_x][self.chunk_y]

    def game_input(self):
        if self.turn_counter == -1:
            self.turn_counter += 1
            return

        if terminal.has_input():
            key = terminal.read()

            if key == terminal.TK_ESCAPE or key == terminal.TK_CLOSE:
                self.game_flag = False

            # player movement
            area = self.load_chunk if self.player.status == -1 else\
                self.load_chunk.dungeon.floors[self.player.status]
            if key == terminal.TK_LEFT or key == terminal.TK_H:
                self.player.move(-1, 0, area)
                self.jump_chunk()
                return True

            if key == terminal.TK_RIGHT or key == terminal.TK_L:
                self.player.move(1, 0, area)
                self.jump_chunk()
                return True

            if key == terminal.TK_DOWN or key == terminal.TK_J:
                self.player.move(0, 1, area)
                self.jump_chunk()
                return True

            if key == terminal.TK_UP or key == terminal.TK_K:
                self.player.move(0, -1, area)
                self.jump_chunk()
                return True

            if key == terminal.TK_Y:    # move up-left
                self.player.move(-1, -1, area)
                self.jump_chunk()
                return True

            if key == terminal.TK_U:    # move up-right
                self.player.move(1, -1, area)
                self.jump_chunk()
                return True

            if key == terminal.TK_B:
                self.player.move(-1, 1, area)
                self.jump_chunk()
                return True

            if key == terminal.TK_N:
                self.player.move(1, 1, area)
                self.jump_chunk()
                return True

    def jump_chunk(self):
        if type(self.load_chunk) == Chunk:
            if self.player.y < 0:
                self.update_chunk(0, -1)
                self.player.y = self.chunk_size - 1

            if self.player.y > self.chunk_size - 1:
                self.update_chunk(0, 1)
                self.player.y = 0

            if self.player.x > self.chunk_size - 1:
                self.update_chunk(1, 0)
                self.player.x = 0

            if self.player.x < 0:
                self.update_chunk(-1, 0)
                self.player.x = self.chunk_size - 1


if __name__ == "__main__":
    g = Game()
