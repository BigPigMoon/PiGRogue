from bearlibterminal import terminal

from Player import *
from Map import Map
from View import View


class Game():
    def __init__(self):
        self.turn_counter = -1
        self.game_flag = True

        self.player = Player(45, 55)
        self.view = View(self.player)
        self.map = Map()

        self.chunk_size = self.map.chunk_size
        self.chunk_x = 3
        self.chunk_y = 3
        self.load_chunk = self.map.world[self.chunk_x][self.chunk_y]

        self.main()

    def main(self):
        terminal.open()
        terminal.set("GameSettings.ini")

        while self.game_flag:
            self.game_input()

            self.view.draw(self.load_chunk)

            terminal.printf(52, 1, f"view x:{self.view.x}, y:{self.view.y}")
            terminal.printf(52, 3, f"player x:{self.player.x}, y:{self.player.y}")

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

            if key == terminal.TK_LEFT or key == terminal.TK_H:
                if self.player.x > self.view.w // 2 - 1 and \
                        self.player.x < self.chunk_size - self.view.w // 2:
                    self.view.x -= 1

                self.player.x -= 1

                if self.player.x < 0:
                    self.update_chunk(-1, 0)
                    self.player.x = self.chunk_size - 1

                self.turn_counter += 1

            if key == terminal.TK_RIGHT or key == terminal.TK_L:
                if self.player.x > self.view.w // 2 - 2 and \
                        self.player.x < self.chunk_size - self.view.w // 2 - 1:
                    self.view.x += 1

                self.player.x += 1

                if self.player.x > self.chunk_size - 1:
                    self.update_chunk(1, 0)
                    self.player.x = 0

                self.turn_counter += 1

            if key == terminal.TK_DOWN or key == terminal.TK_J:
                if self.player.y > self.view.h // 2 - 2 and\
                        self.player.y < self.chunk_size - self.view.h // 2 - 1:
                    self.view.y += 1

                self.player.y += 1

                if self.player.y > self.chunk_size - 1:
                    self.update_chunk(0, 1)
                    self.player.y = 0

                self.turn_counter += 1

            if key == terminal.TK_UP or key == terminal.TK_K:
                # chek view zone
                if self.player.y > self.view.h // 2 - 1 and\
                        self.player.y < self.chunk_size - self.view.h // 2:
                    self.view.y -= 1
                
                # move player
                self.player.y -= 1

                # chek jump to next chunk
                if self.player.y < 0:
                    self.update_chunk(0, -1)
                    self.player.y = self.chunk_size - 1

                self.turn_counter += 1


if __name__ == "__main__":
    g = Game()
