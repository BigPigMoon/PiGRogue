class Tile:
    def __init__(self, tile_type, color, block, objects=[]):
        self.type = tile_type
        self.on_tile = objects
        self.color = color
        self.block = block
        self.entity_on_me = None
