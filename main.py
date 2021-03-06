from bearlibterminal import terminal

from Player import Player
from Chunk import Chunk
from Map import Map
from View import View
from ViewMode import ViewMode
from AttackMode import AttackMode


class Game:
    def __init__(self):
        self.turn_counter = -1
        self.game_flag = True

        self.player = Player(15, 55)

        self.view = View(self.player)
        self.attack_mode = AttackMode()
        self.view_mode = ViewMode()
        self.chunk_x = 2
        self.chunk_y = 2
        self.map = Map(self.chunk_x, self.chunk_y)

        self.chunk_size = self.map.chunk_size
        self.load_chunk = self.map.world[self.chunk_x][self.chunk_y]

        self.player.area = self.load_chunk.area

        self.main()

    def main(self):
        terminal.open()
        terminal.set("GameSettings.ini")

        while self.game_flag:
            if self.game_input():
                self.turn_counter += 1

                if self.player.status == -1:
                    self.load_chunk.update(self.player)
                else:
                    self.load_chunk.dungeon.floors[self.player.status].update(
                        self.player)

            if self.player.status == -1:
                self.view.draw(self.load_chunk)
                self.player.area = self.load_chunk.area
            else:
                self.view.draw(
                    self.load_chunk.dungeon.floors[self.player.status]
                )
                terminal.printf(52, 49, f"floor {self.player.status + 1}")
                self.player.area = self.load_chunk.dungeon.floors[
                    self.player.status].area

            terminal.printf(51, 10, f"{self.load_chunk.min_level=}")
            terminal.printf(51, 11, f"{self.load_chunk.max_level=}")

            if self.view_mode.mode_bool:
                self.view_mode.draw(self.view.x, self.view.y)
                self.view_mode.print_information()

            if self.attack_mode.mode_bool:
                self.attack_mode.draw(self.view.x, self.view.y)

            if self.player.inventory.var_bool:
                self.player.inventory.draw()

            self.player.check_dungeon(self.load_chunk)

            self.view.update()

            terminal.refresh()
            terminal.clear()

        terminal.close()

    def game_input(self):
        if self.turn_counter == -1:
            self.turn_counter += 1
            return

        if terminal.has_input():
            key = terminal.read()

            if key == terminal.TK_CLOSE:
                self.game_flag = False

            if key == terminal.TK_ESCAPE:
                if self.view_mode.mode_bool or self.attack_mode.mode_bool or\
                        self.player.inventory.var_bool:
                    self.view_mode.mode_bool = False
                    self.attack_mode.mode_bool = False
                    self.player.inventory.var_bool = False
                    self.view.target = self.player
                else:
                    self.game_flag = False

            # player movement
            if self.view_mode.mode_bool:
                moved_body = self.view_mode
            elif self.attack_mode.mode_bool:
                moved_body = self.attack_mode
            elif self.player.inventory.var_bool:
                moved_body = self.player.inventory
            else:
                moved_body = self.player

            if (key == terminal.TK_LEFT or
                    key == terminal.TK_H or
                    key == terminal.TK_KP_4):
                moved_body.move(-1, 0)
                self.jump_chunk()
                if type(moved_body) == Player:
                    return True

            if (key == terminal.TK_RIGHT or
                    key == terminal.TK_L or
                    key == terminal.TK_KP_6):
                moved_body.move(1, 0)
                self.jump_chunk()
                if type(moved_body) == Player:
                    return True

            if (key == terminal.TK_DOWN or
                    key == terminal.TK_J or
                    key == terminal.TK_KP_2):
                moved_body.move(0, 1)
                self.jump_chunk()
                if type(moved_body) == Player:
                    return True

            if (key == terminal.TK_UP or
                    key == terminal.TK_K or
                    key == terminal.TK_KP_8):
                moved_body.move(0, -1)
                self.jump_chunk()
                if type(moved_body) == Player:
                    return True

            if key == terminal.TK_Y or key == terminal.TK_KP_7:
                moved_body.move(-1, -1)
                self.jump_chunk()
                if type(moved_body) == Player:
                    return True

            if key == terminal.TK_U or key == terminal.TK_KP_9:
                moved_body.move(1, -1)
                self.jump_chunk()
                if type(moved_body) == Player:
                    return True

            if key == terminal.TK_B or key == terminal.TK_KP_1:
                moved_body.move(-1, 1)
                self.jump_chunk()
                if type(moved_body) == Player:
                    return True

            if key == terminal.TK_N or key == terminal.TK_KP_3:
                moved_body.move(1, 1)
                self.jump_chunk()
                if not type(moved_body) == Player:
                    return True

            if key == terminal.TK_SPACE or key == terminal.TK_KP_5:
                if not type(moved_body) == Player:
                    return True

            if key == terminal.TK_X:
                if not self.view_mode.mode_bool:
                    self.view_mode.set_position(self.player.x,
                                                self.player.y,
                                                self.load_chunk)
                    if self.player.status >= 0:
                        self.view_mode.chunk = self.load_chunk.dungeon.floors[
                            self.player.status]

                    self.view.target = self.view_mode
                    self.view_mode.mode_bool = True
                    self.attack_mode.mode_bool = False
                else:
                    self.view.target = self.player
                    self.view_mode.mode_bool = False

            if key == terminal.TK_A:
                if not self.attack_mode.mode_bool:
                    self.attack_mode.set_position(self.player.x,
                                                  self.player.y,
                                                  self.load_chunk)

                    if self.player.status >= 0:
                        self.attack_mode.chunk = self.load_chunk.dungeon.floors[self.player.status]
                    self.view_mode.mode_bool = False
                    self.attack_mode.mode_bool = True
                    self.view.target = self.attack_mode
                else:
                    self.view.target = self.player
                    self.attack_mode.mode_bool = False

            if self.attack_mode.mode_bool and key == terminal.TK_ENTER:
                self.attack_mode.fire()
                self.view.target = self.player
                self.attack_mode.mode_bool = False
                return True

            if key == terminal.TK_I:
                if not self.player.inventory.var_bool:
                    self.player.inventory.var_bool = True
                    self.player.inventory.cursor = 0
                else:
                    self.player.inventory.var_bool = False

            return False

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

            self.player.area = self.load_chunk.area
            self.player.sit_down_tile()


if __name__ == "__main__":
    g = Game()
