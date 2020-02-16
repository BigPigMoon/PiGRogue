from bearlibterminal import terminal

from Player import *
from Map import Map
from View import View


class Game():
    def __init__(self):
        self.turn_counter = -1
        self.chunk_x = 1
        self.chunk_y = 1
        self.chunk_size = 128
        self.game_flag = True
        self.player = Player()
        self.map = Map(self.chunk_size)
        self.view = View(self.player)

        self.main()

    def main(self):
        terminal.open()
        terminal.set("GameSettings.ini")

        while self.game_flag:
            self.game_input()

            self.view.draw(self.map.world[self.chunk_x][self.chunk_y])

            terminal.refresh()
            terminal.clear()

        terminal.close()

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
                self.turn_counter += 1

            if key == terminal.TK_RIGHT or key == terminal.TK_L:
                if self.player.x > self.view.w // 2 - 2 and \
                        self.player.x < self.chunk_size - self.view.w // 2 - 1:
                    self.view.x += 1
                self.player.x += 1

                self.turn_counter += 1

            if key == terminal.TK_DOWN or key == terminal.TK_J:
                if self.player.y > self.view.h // 2 - 2 and\
                        self.player.y < self.chunk_size - self.view.h // 2 - 1:
                    self.view.y += 1
                self.player.y += 1
                self.turn_counter += 1

            if key == terminal.TK_UP or key == terminal.TK_K:
                if self.player.y > self.view.h // 2 - 1 and\
                        self.player.y < self.chunk_size - self.view.h // 2 - 1:
                    self.view.y -= 1
                self.player.y -= 1
                self.turn_counter += 1


if __name__ == "__main__":
    g = Game()
