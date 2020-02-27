import json

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


def get_monster_pack():
    monster_pack = []

    file = open("monster.json", 'r', encoding="utf-8")
    monster_json = json.load(file)
    file.close()

    monster_json = monster_json["monsters"]
    for m in monster_json:
        monster_pack.append(Entity(m["name"], m["color"], m["hp"],
                                   m["damage"], m["dam_resist"]))

    return monster_pack


if __name__ == '__main__':
    for m in get_monster_pack():
        print(m.name)
