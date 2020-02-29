class Tile:
    def __init__(self, tile_type, color, block):
        self.type = tile_type
        self.item_on_me = None
        self.color = color
        self.block = block
        self.entity_on_me = None
