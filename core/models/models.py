from dataclasses import dataclass, field
from enum import Enum


@dataclass
class Monster:

    name:        str
    type:        str
    family:      str
    level:       float
    description: str = None

    def __str__(self):
        # This helps to identify the object in the Django admin
        return f"{self.name} (Level {self.level})"

@dataclass
class Loot:
    name:        str
    rarity:      str
    value:       int
    description: str = None

    def __str__(self):
        return f"Loot: {self.name}, Rarity: {self.rarity}, Value: {self.value}"

# --- Enums ---

class ArmorType(Enum):
    none = "None"
    cloth = "Cloth"
    leather = "Leather"
    mail = "Mail"
    plate = "Plate"

class CharSize(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"

# --- Componentes do Personagem ---

@dataclass
class Archetype:
    name:         str
    key_stats:    list #[str]
    hit_die:      int
    level1_hp:    int
    saves:        dict #[str, int]
    armor_prof:   ArmorType
    weapons_prof: list #[str]
    start_gear:   list #[str]
    features:     dict #[int, list[str]]

@dataclass
class Ancestry:
    class AncBonus:
        pass
    name:  str
    size:  CharSize
    bonus: AncBonus

@dataclass
class Stats:
    STR: int
    DEX: int
    INT: int
    WIL: int

@dataclass
class Skills:
    arcana: int
    craft: int
    examination: int
    finesse: int
    influence: int
    insight: int
    lore: int
    might: int
    naturecraft: int
    perception: int
    stealth: int

# --- Main Class: CHARACTER ---

@dataclass
class Character:
    name:       str
    archetype:  Archetype
    ancestry:   Ancestry
    stats:      Stats
    skills:     Skills
    armor:      int

    level:      int = 1  # initial
    speed:      int = 6 #default

    initiative: int = field(init=False)
    hp_max:     int = field(init=False)
    hp:         int = field(init=False)
    hd_max:     int = field(init=False)
    hd:         int = field(init=False)
    wounds_max: int = 6
    wounds:     int = 0
    mana_max:   int = 0
    inv_slots:  int = field(init=False)

    def __post_init__(self):
        # 1. Validação do nível
        if not (1 <= self.level <= 20):
            raise ValueError("O nível deve estar entre 1 e 20!")

        # 2. Cálculo dos atributos dependentes
        # Agora sim temos acesso a self.stats e self.archetype
        self.initiative = self.stats.DEX
        self.hp_max = self.archetype.level1_hp
        self.hp = self.hp_max
        self.hd_max = self.level
        self.hd = self.hd_max
        self.inv_slots = 10 + self.stats.STR

"""
class Archetype:
    class ArmorType(Enum):
        none = "None"
        cloth = "Cloth"
        leather = "Leather"
        mail = "Mail"
        plate = "Plate"

    def __init__(self, name:str, key_stats:list, hit_die:int, level1_hp:int, saves:list, armor:, weapons:list,starting_gear:list):
        self.name = name
        self.key_stats = key_stats
        self.hit_die = hit_die
        self.level1_hp = level1_hp
        self.saves = saves
        self.armor = armor
        self.weapons = weapons
        self.starting_gear = starting_gear
        pass

class Stats:
    pass

class Character:
    def __init__(self, name:str, archetype:Archetype, level:int, stats:Stats):
        self.name = name
        self.archetype = archetype
        self.level = level
        self.stats = stats
"""