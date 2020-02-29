import json
from copy import copy
from random import choice, randint

from Corporation import get_corporations


def get_name():
    first_part = ["Убойный", "Крошащий", "Смертельный", "Излучающий", "Доброжелательный"]
    second_part = ["Убиватель", "Самотык", "Крошитель", "Разрушитель", "Кактус", "Карандаш", "Ломатель"]

    return choice(first_part) + " " + choice(second_part)


def gen_weapon():
    bases, grips, barrels, butts, sights, magazines = get_components()
    corporations = get_corporations()
    corporation = choice(corporations)
    level = randint(1, 10)

    name = get_name()

    magaz = choice(magazines)
    base = choice(bases)
    grip = choice(grips)
    if randint(0, 4) in {1, 2, 3}:
        barrel = choice(barrels)
    else:
        barrel = None
    if randint(0, 1):
        butt = choice(butts)
    else:
        butt = None
    if randint(0, 4) == 1:
        sight = choice(sights)
    else:
        sight = None

    weapon = Weapon(name, corporation, level,
                    magaz, base, grip, barrel,
                    butt, sight)

    return copy(weapon)


def get_components():
    bases = []
    magazines = []
    grips = []
    barrels = []
    butts = []
    sights = []

    file = open("Jsons/weapon_component.json", 'r', encoding="utf-8")
    weapon_components = json.load(file)
    file.close()

    bases_json = weapon_components["bases"]
    magazines_json = weapon_components["magazines"]
    grips_json = weapon_components["grips"]
    barrels_json = weapon_components["barrels"]
    sights_json = weapon_components["sights"]
    butts_json = weapon_components["butts"]

    for base in bases_json:
        bases.append(Base(base))

    for grip in grips_json:
        grips.append(Grip(grip))

    for barrel in barrels_json:
        barrels.append(Barrel(barrel))

    for sight in sights_json:
        sights.append(Sight(sight))

    for butt in butts_json:
        butts.append(Butt(butt))

    for magazine in magazines_json:
        magazines.append(Magazine(magazine))

    return bases, grips, barrels, butts, sights, magazines


class Weapon:
    def __init__(self, nm, cp, lv, magaz, base, grip, barrel, butt, sight):
        self.name = nm
        self.corporation = cp
        self.level = lv
        # обязательные компоненты
        self.base = base  # база
        self.magazine = magaz  # магазин
        self.grip = grip  # ручка
        # не обязательные компоненты
        self.barrel = barrel  # ствол
        self.butt = butt  # приклад
        self.sight = sight  # прицел
        self.bullet_type = None

        self.max_bullets_size = self.magazine.size

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

        self.damage *= self.corporation.damage
        self.speed *= self.corporation.speed
        self.distance *= self.corporation.distance
        self.accuracy *= self.corporation.accuracy
        self.reload_speed *= self.corporation.reload_speed
        self.magazine.size = int(self.magazine.size * self.corporation.size)

    def reload(self):
        pass


class Base:
    def __init__(self, base):
        self.damage = base["dm"]
        self.speed = base["sp"]
        self.distance = base["ds"]
        self.accuracy = base["ac"]


class Grip:
    def __init__(self, grip):
        self.accuracy = grip["ac"]
        self.reload_speed = grip["rl_sp"]


class Barrel:
    def __init__(self, barrel):
        self.damage = barrel["dm"]
        self.speed = barrel["sp"]
        self.distance = barrel["ds"]
        self.accuracy = barrel["ac"]


class Butt:
    def __init__(self, butt):
        self.distance = butt["ds"]
        self.accuracy = butt["ac"]


class Sight:
    def __init__(self, sight):
        self.distance = sight["ds"]
        self.accuracy = sight["ac"]


class Magazine:
    def __init__(self, magazine):
        self.reload_speed = magazine["rl_sp"]
        self.size = magazine["size"]
        self.count = self.size
