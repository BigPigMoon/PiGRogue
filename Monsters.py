import json

from Entity import Entity


def get_monster_pack():
    monster_pack = []

    file = open("Jsons/monster.json", 'r', encoding="utf-8")
    monster_json = json.load(file)
    file.close()

    monster_json = monster_json["monsters"]
    for m in monster_json:
        monster_pack.append(Entity(m["name"], m["color"], m["hp"],
                                   m["dam_resist"]))

    return monster_pack


if __name__ == '__main__':
    for m in get_monster_pack():
        print(m.name)
