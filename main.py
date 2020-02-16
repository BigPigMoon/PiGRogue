from bearlibterminal import terminal

from Player import *
from Map import Map


class Game():
    def __init__(self):
        self.turn_counter = -1
        self.game_flag = True
        self.player = Player()
        self.map = Map(64)
        self.main()

    def main(self):
        terminal.open()
        terminal.set("GameSettings.ini")

        while self.game_flag:
            self.game_input()
            # draw all game objects
            self.map.draw(1, 1)

            # self.player.draw()

            terminal.refresh()

        terminal.close()

    def game_input(self):
        if self.turn_counter == -1:
            self.turn_counter += 1
            return
        if terminal.has_input():
            key = terminal.read()

            if key == terminal.TK_ESCAPE or key == terminal.TK_CLOSE:
                self.game_flag = False

            if key == terminal.TK_LEFT or key == terminal.TK_L:
                self.player.clear()
                self.player.x -= 1
                self.turn_counter += 1

            if key == terminal.TK_RIGHT or key == terminal.TK_H:
                self.player.clear()
                self.player.x += 1
                self.turn_counter += 1

            if key == terminal.TK_DOWN or key == terminal.TK_J:
                self.player.clear()
                self.player.y += 1
                self.turn_counter += 1

            if key == terminal.TK_UP or key == terminal.TK_K:
                self.player.clear()
                self.player.y -= 1
                self.turn_counter += 1


if __name__ == "__main__":
    g = Game()
