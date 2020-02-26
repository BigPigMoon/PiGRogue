from Entity import Entity


class Animal(Entity):
    def __init__(self, area, name, x, y):
        Entity.__init__(self, area, name, "blue", x, y)


class People(Entity):
    def __init__(self, area, name, x, y):
        Entity.__init__(self, area, name, "blue", x, y)


class Monster(Entity):
    def __init__(self, area, name, x, y):
        Entity.__init__(self, area, name, "blue", x, y)
