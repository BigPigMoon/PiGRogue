import json


class Bullet:
    def __init__(self, bullet):
        self.type = bullet["tp"]
        self.damage = bullet["dm"]
        self.speed = bullet["sp"]
        self.distance = bullet["ds"]
        self.accuracy = bullet["ac"]


def get_bullets():
    bullets = []

    file = open("Jsons/bullet.json", 'r', encoding="utf-8")
    json_file = json.load(file)
    file.close()

    bullets_json = json_file["bullets"]

    for bullet in bullets_json:
        bullets.append(Bullet(bullet))
