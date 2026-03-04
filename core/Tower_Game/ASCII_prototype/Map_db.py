from random import choice, randint

YELLOW = '\033[93m'
BLUE = '\033[34m'
LIGHTBLUE = '\033[94m'

GREEN = '\033[32m'
LIGHTGREEN = '\033[92m'

RED = '\033[31m'
RESET = '\033[0m'
BOLD = '\033[1m'
H1 = BOLD + BLUE
H2 = BOLD + RED

class Tile():
    def __init__(self, type:str, symbol:str, collision:bool = None, height:int = None):
        self.type = type
        self.symbol = symbol
        self.collision = collision
        self.height = height

tiles_default = {
    "wall_h": Tile("wall_horizontal", "███", True, 0),
    "wall_v": Tile("wall_vertical", "█  ", True, 0),
    "floor": Tile("floor", "-  ", False, 1),
    "hero": Tile("hero", f"{H1}H{RESET}  "),
    "monster": Tile("monster", f"{H2}M{RESET}  "),
    "loot": Tile("loot", f"{YELLOW}?{RESET}  "),
    "start": Tile("start", "S  "),
    "exit": Tile("exit", "E  ")
}

all_tiles = {
    "wall_h": Tile("wall_horizontal", "███", True, 0),
    "wall_v": Tile("wall_vertical", "█  ", True, 0),
    "empty": Tile("empty", "   ", True, 0),
    "water": Tile("water", f"{LIGHTBLUE}~~~{RESET}", True, 0),
    "grass": Tile("grass", f"{LIGHTGREEN},,,{RESET}", False, 1),
    "floor": Tile("floor", "-  ", False, 1),
    "stairs": Tile("stairs", "░░ ", False, 2),
    "trees": Tile("trees", f"{GREEN}Y{RESET}  ", False, 2),
    "mountains": Tile("mountains", "^^^", True, 3),
    "hero": Tile("hero", f"{H1}H{RESET}  "),
    "monster": Tile("monster", f"{H2}M{RESET}  "),
    "loot": Tile("loot", f"{YELLOW}?{RESET}  "),
    "start": Tile("start", "S  "),
    "exit": Tile("exit", "E  ")
}


class Biome():
    def __init__(self, name:str, tiles:dict):
        self.name = name
        self.tiles = tiles_default | tiles

biomes = {
    "dungeon": Biome("dungeon", 
        {
            "stairs": Tile("stairs", "░░░", False, 2),
        }),
    "plains": Biome("plains", 
        {
            "water": Tile("water", f"{LIGHTBLUE}~~~{RESET}", True, 0),
            "grass": Tile("grass", f"{LIGHTGREEN},,,{RESET}", False, 1),
            "trees": Tile("trees", f"{GREEN}Y{RESET}  ", False, 2),
        }),
    "mountains": Biome("mountains", 
        {
            "mountains": Tile("mountains", "^^^", True, 3),
            "grass": Tile("grass", f"{LIGHTGREEN},,,{RESET}", False, 1),
        })
}
