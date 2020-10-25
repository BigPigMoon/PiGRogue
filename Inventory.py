from DialogWindow import Dialog

from bearlibterminal import terminal


class InfoWindow(Dialog):
    def __init__(self):
        super().__init__(60, 40)
        self.draw_x = 0

    def move(self, dx, dy):
        super().move(dx, dy)

    def draw(self, item):
        super().draw()
        name = f"{item.name} от {item.corporation.name}"
        self.draw_x = 0
        terminal.printf(self.x + 1, self.y + 2, f"{name:-^58}")
        self.print(f"уровень: {item.level}")
        self.print(f"Урон: {item.damage:.1f}")
        self.print(f"Скорость стрельбы: {item.speed} пуль за ход")
        self.print(f"Дальность: {item.distance} клеток")
        self.print(f"Точность: {item.accuracy:.1f}%")
        self.print(f"Скорость перезарядки: {item.reload_speed} ход.")
        self.print(f"Емкость: {item.size}")
        self.print(f"Тип пуль: {item.bullet_type}")

        s = "Конструкция"
        self.draw_x += 4
        terminal.printf(self.x + 1, self.y+self.draw_x + 1, f"{s:-^58}")
        self.print(f"База: {item.base is not None}")
        self.print(f"Ручка: {item.grip is not None}")
        self.print(f"Ствол: {item.barrel is not None}")
        self.print(f"Приклад: {item.butt is not None}")
        self.print(f"Прицел: {item.sight is not None}")

    def print(self, message):
        terminal.printf(self.x + 2, self.y + 4 + self.draw_x, message)
        self.draw_x += 1


class InventoryDialog(Dialog):
    def __init__(self):
        super().__init__(20, 30)
        self.info = InfoWindow()
        self.max_cursor = 3

    def draw(self):
        if not self.info.var_bool:
            super().draw()
            terminal.put(self.x + 2, self.cursor + self.y + 2, '+')
            terminal.printf(self.x + 4, self.y + 2, "Информация")
            terminal.printf(self.x + 4, self.y + 3, "Экипировать")
            terminal.printf(self.x + 4, self.y + 4, "Выкинуть")
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




