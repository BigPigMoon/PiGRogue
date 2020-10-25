from copy import copy
from random import choice, randint

from Corporation import get_corporations


def get_name():
    first_part = ["Убойный", "Крошащий", "Смертельный", "Излучающий",
                  "Доброжелательный", "Испепиляющий"]
    second_part = ["Убиватель", "Самотык", "Крошитель", "Разрушитель",
                   "Кактус", "Карандаш", "Ломатель"]

    return choice(first_part) + " " + choice(second_part)


def gen_weapon(level):
    corporations = get_corporations()
    corporation = choice(corporations)

    name = get_name()

    magazine = Magazine()
    base = Base()
    grip = Grip()
    barrel = Barrel()

    if randint(0, 1):
        butt = Butt()
    else:
        butt = None
    if randint(0, 4) == 1:
        sight = Sight()
    else:
        sight = None

    weapon = Weapon(name, corporation, level,
                    magazine, base, grip, barrel,
                    butt, sight)

    return copy(weapon)


class Weapon:
    def __init__(self, nm, cp, lv, magazine, base, grip, barrel, butt, sight):
        self.name = nm
        self.corporation = cp
        self.level = lv
        # обязательные компоненты
        self.base = base  # база
        self.magazine = magazine  # магазин
        self.grip = grip  # ручка
        self.barrel = barrel  # ствол
        # не обязательные компоненты
        self.butt = butt  # приклад
        self.sight = sight  # прицел
        self.bullet_type = None

        self.size = self.magazine.size

        self.damage = self.base.damage  # + self.bullet_type.damage
        self.speed = self.base.speed  # + self.bullet_type.speed
        self.distance = self.base.distance  # + self.bullet_type.distance
        self.accuracy = self.base.accuracy + self.grip.accuracy
        # + self.bullet_type.accuracy

        self.reload_speed = self.grip.reload_speed + self.magazine.reload_speed

        if self.barrel is not None:
            self.damage += self.barrel.damage
            self.speed += self.barrel.speed
            self.distance += self.barrel.distance
            self.accuracy += self.barrel.accuracy

        if self.butt is not None:
            self.distance += self.butt.distance
            self.accuracy += self.butt.accuracy

        if self.sight is not None:
            self.distance += self.sight.distance
            self.accuracy += self.sight.accuracy

        self.damage += self.damage * self.level * 0.3
        self.speed += self.speed * self.level * 0.16
        self.distance += self.distance * self.level * 0.009
        self.accuracy += self.accuracy * self.level * 0.006
        self.reload_speed -= self.reload_speed * self.level * 0.015

        self.damage *= self.corporation.damage
        self.speed *= self.corporation.speed
        self.distance *= self.corporation.distance
        self.accuracy *= self.corporation.accuracy
        self.reload_speed *= self.corporation.reload_speed
        self.magazine.size = int(self.magazine.size * self.corporation.size)

        self.reload_speed = int(self.reload_speed)
        self.distance = int(self.distance)
        self.speed = int(self.speed)

        if self.reload_speed <= 0:
            self.reload_speed = 1

    def reload(self):
        pass


class Base:
    def __init__(self):
        self.damage = randint(2, 10)
        self.speed = randint(0, 5)
        self.distance = randint(1, 5)
        self.accuracy = randint(5, 10)


class Grip:
    def __init__(self):
        self.accuracy = randint(10, 15)
        self.reload_speed = randint(1, 2)


class Barrel:
    def __init__(self):
        self.damage = randint(1, 10)
        self.speed = randint(1, 5)
        self.distance = randint(1, 10)
        self.accuracy = randint(5, 25)


class Butt:
    def __init__(self):
        self.distance = randint(3, 5)
        self.accuracy = randint(15, 25)


class Sight:
    def __init__(self):
        self.distance = randint(5, 10)
        self.accuracy = randint(15, 25)


class Magazine:
    def __init__(self):
        self.reload_speed = randint(2, 5)
        self.size = randint(1, 60)
        self.count = self.size
