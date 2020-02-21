def choise_wall(direct, room):
    """Выбирает комнату в зависимости от направления.

    args:
        direct -- направление выбора стены
        room -- комната в которой набо выбирать(Rect)

    return:
        wall -- список со списком координат и одной координатой.
        Если не задать направления вернет None.
        [x, [y1, y2]]
        or
        [[x1, x2], y]

    схема направления
          1
          |
       4--.--2
          |
          3
    """
    x1 = room.x1
    x2 = room.x2
    y1 = room.y1
    y2 = room.y2

    if direct == "UP" or direct == 1:
        wall = [[x for x in range(min(x1, x2), max(x1, x2))], y1]
    elif direct == "DOWN" or direct == 3:
        wall = [[x for x in range(min(x1, x2), max(x1, x2))], y2]
    elif direct == "LEFT" or direct == 4:
        wall = [x1, [y for y in range(min(y1, y2), max(y1, y2))]]
    elif direct == "RIGHT" or direct == 2:
        wall = [x2, [y for y in range(min(y1, y2), max(y1, y2))]]
    else:
        print("oops, change true direction")
        return

    return wall


def scan_wall(direct, coords, depth, floor):
    """Сканирует стену в глубину для новой комнаты, тунеля и пр.
    
    args:
        deriect -- направление для сканирования
        coords -- список координат для сканирования
        depth -- глубина сканирования
        floor -- карта для сканирования

    return:
        clear -- чисто или нет(true or false)

    схема направления
          1
          |
       4--.--2
          |
          3
    """
    if coords is not None:
        if direct == "UP" or direct == 1:
            return scan_up(coords, depth, floor)
        elif direct == "RIGHT" or direct == 2:
            return scan_right(coords, depth, floor)
        elif direct == "DOWN" or direct == 3:
            return scan_down(coords, depth, floor)
        elif direct == "LEFT" or direct == 4:
            return scan_left(coords, depth, floor)
    else:
        print("oops, your coordinates is None.")
        return


def scan_up(coords, depth, floor):
    y = coords[1]
    for x in coords[0]:
        for yd in range(1, depth + 1):
            try:
                if y-yd < 0:
                    return False
                if not floor[x][y-yd].block:
                    return False
            except IndexError:
                return False
    return True


def scan_down(coords, depth, floor):
    y = coords[1]
    for x in coords[0]:
        for yd in range(0, depth):
            try:
                if not floor[x][y+yd].block:
                    return False
            except IndexError:
                return False
    return True


def scan_left(coords, depth, floor):
    x = coords[0]
    for y in coords[1]:
        for xd in range(1, depth + 1):
            try:
                if x - xd < 0:
                    return False
                if not floor[x-xd][y].block:
                    return False
            except IndexError:
                return False
    return True


def scan_right(coords, depth, floor):
    x = coords[0]
    for y in coords[1]:
        for xd in range(0, depth):
            try:
                if not floor[x+xd][y].block:
                    return False
            except IndexError:
                return False
    return True
