from DialogWindow import Dialog

from bearlibterminal import terminal


class InfoWindow(Dialog):
    def __init__(self):
        super().__init__(40, 40)

    def move(self, dx, dy):
        super().move(dx, dy)

    def draw(self, item):
        super().draw()
        terminal.printf(self.x + 2, self.y + 2, f"\t{item.name}")
        terminal.printf(self.x + 2, self.y + 3, f"Урон: {item.damage}")
        terminal.printf(self.x + 2, self.y + 4, "Информативынй Экран")
        terminal.printf(self.x + 2, self.y + 5, "Информативынй Экран")
        terminal.printf(self.x + 2, self.y + 6, "Информативынй Экран")
        terminal.printf(self.x + 2, self.y + 7, "Информативынй Экран")


class InventoryDialog(Dialog):
    def __init__(self):
        super().__init__(20, 30)
        self.info = InfoWindow()
        self.max_cursor = 2

    def draw(self):
        if not self.info.var_bool:
            super().draw()
            terminal.put(self.x + 2, self.cursor + self.y + 2, '+')
            terminal.printf(self.x + 4, self.y + 2, "Информация")
            terminal.printf(self.x + 4, self.y + 3, "Экипировать")
        else:
            self.info.draw(self.item)

    def move(self, dx, dy):
        if not self.info.var_bool:
            super().move(dx, dy)
            if dx > 0:
                if self.cursor == 0:
                    self.info.var_bool = True
        else:
            self.info.move(dx, dy)


class Inventory(Dialog):
    def __init__(self):
        super().__init__(50, 40)
        self.inventory_dialog = InventoryDialog()

        self.items = list()
        self.first_weapon = None
        self.second_weapon = None

        self.bullets = dict()  # bullet_type: count
        self.money = 0

    def draw(self):
        if not self.inventory_dialog.var_bool:
            super().draw()
            terminal.put(self.x + 2, self.cursor + self.y + 2, '+')
            y = 0
            for item in self.items:
                terminal.printf(self.x + 4,
                                self.y + 2 + y,
                                item.name)
                y += 1
        else:
            self.inventory_dialog.draw()

    def move(self, dx, dy):
        if not self.inventory_dialog.var_bool:
            self.max_cursor = len(self.items)
            super().move(dx, dy)
            if dx > 0:
                if self.max_cursor != 0:
                    self.inventory_dialog.item = self.items[self.cursor]
                    self.inventory_dialog.var_bool = True
        else:
            self.inventory_dialog.move(dx, dy)




