import json


class Corporation:
    def __init__(self, corporation):
        self.name = corporation["name"]

        # bonus
        self.damage = corporation["dm"]
        self.speed = corporation["sp"]
        self.distance = corporation["ds"]
        self.accuracy = corporation["ac"]

        self.reload_speed = corporation["rs"]
        self.size = corporation["size"]


def get_corporations():
    corporations = []

    file = open("Jsons/corporations.json", 'r', encoding="utf-8")
    json_file = json.load(file)
    file.close()

    corporations_json = json_file["corporations"]

    for corporation in corporations_json:
        corporations.append(Corporation(corporation))

    return corporations
