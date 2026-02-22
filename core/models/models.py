from dataclasses import dataclass
from enum import Enum


class Monster:

    def __init__(self, name, type, family, level, description=None):

        self.name = name
        self.type = type
        self.family = family
        self.level = level
        self.description = description

    def __str__(self):
        # This helps to identify the object in the Django admin
        return f"{self.name} (Level {self.level})"


class Loot:

    def __init__(self, name, rarity, value, description=None):

        self.name = name
        self.rarity = rarity
        self.value = value
        self.description = description

    def __str__(self):
        return f"Loot: {self.name}, Rarity: {self.rarity}, Value: {self.value}"

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

@dataclass
class Archetype:

    name:         str
    key_stats:    list
    hit_die:      int
    level1_hp:    int
    saves:        dict
    armor_prof:   ArmorType
    weapons_prof: list
    start_gear:   list
    features:     dict

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
    initiative: int = stats.DEX #default
    hp_max:     int = archetype.level1_hp #initial
    hp:         int = hp_max #default
    hd_max:     int = level #default
    hd:         int = hd_max
    wounds_max: int = 6 #default
    wounds:     int = 0 #initial
    mana_max:   int = 0
    inv_slots:  int = 10+stats.STR #default

    @level.setter
    def _level(self, value):
        if not (1 <= value <= 20):
            raise ValueError("O nível deve estar entre 1 e 20!")
        self.level = value

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