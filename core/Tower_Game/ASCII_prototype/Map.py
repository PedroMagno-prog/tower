from random import choice, randint

YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
H1 = BOLD + YELLOW

class Tile():
    def __init__(self, type:str, symbol:str, collision:bool = None, height:int = None):
        self.type = type
        self.symbol = symbol
        self.collision = collision
        self.height = height

tiles = {
    "wall_h": Tile("wall_horizontal", "███", True, 0),
    "wall_v": Tile("wall_vertical", "█  ", True, 0),
    "empty": Tile("empty", "   ", True, 0),
    "water": Tile("water", f"{BLUE}~~~{RESET}", True, 0),
    "floor": Tile("floor", "-  ", False, 1),
    "stairs": Tile("stairs", "░░░", False, 2),
    "mountains": Tile("mountains", "^^^", True, 3),
    "hero": Tile("hero", f"{H1}H{RESET}  "),
    "monster": Tile("monster", "M  "),
    "loot": Tile("loot", "?  "),
    "start": Tile("start", "S  "),
    "exit": Tile("exit", "E  ")
}

biomes = {
    "plains": {
        "floor": Tile("floor", "-  ", False, 1),
        "stairs": Tile("stairs", "░░░", False, 2),
        "mountains": Tile("mountains", "^^^", True, 3),
        "hero": Tile("hero", f"{H1}H{RESET}  "),
        "monster": Tile("monster", "M  "),
        "loot": Tile("loot", "?  "),
        "start": Tile("start", "S  "),
        "exit": Tile("exit", "E  ")
    }
}





