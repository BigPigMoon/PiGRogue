class Weapon:
    def __init__(self, nm, cp, magaz, base, grip, barrel, butt, sight):
        self.name = nm
        self.corparation = cp

        self.base = base  # база
        self.magazine = magaz  # магазин
        self.grip = grip  # ручка
        self.barrel = barrel  # ствол
        self.butt = butt  # приклад
        self.sight = sight  # прицел

        self.max_bullets_size = self.magazine.size
        self.bullet_type = self.base.bullet_type

        self.damage = self.base.damage + self.barrel.damage +\
            self.bullet_type.damage

        self.speed = self.base.speed + self.barrel.speed + \
            self.bullet_type.speed

        self.distance = self.base.distance + self.barrel.distance + \
            self.butt.distance + self.sight.distance + \
            self.bullet_type.distance

        self.accuracy = self.base.accuracy + self.grip.accuracy + \
            self.barrel.accuracy + self.butt.accuracy + self.sight.accuracy +\
            self.bullet_type.accuracy

        self.reload_speed = self.grip.reload_speed + self.magazine.reload_speed


class Base:
    def __init__(self, dm, sp, ds, ac, bt):
        self.damage = dm
        self.speed = sp
        self.distance = ds
        self.accuracy = ac
        self.bullet_type = bt


class Grip:
    def __init__(self, ac, rs):
        self.accuracy = ac
        self.reload_speed = rs


class Barrel:
    def __init__(self, dm, sp, ds, ac, bt):
        self.damage = dm
        self.speed = sp
        self.distance = ds
        self.accuracy = ac
        self.bullet_type = bt


class Butt:
    def __init__(self, ds, ac):
        self.distance = ds
        self.accuracy = ac


class Sight:
    def __init__(self, ds, ac):
        self.distance = ds
        self.accuracy = ac


class Magazine:
    def __init__(self, rs, bt, size):
        self.reload_speed = rs
        self.bullet_type = bt
        self.size = size
        self.bullets = list()
