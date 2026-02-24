from core.colors import *

family_list = ["Aberration", "Spider", "Bandit", "Construct", "Cultist", "Dragon", "Drow",
    "Fey", "Beast", "Giant", "Gnoll", "Goblin", "Snakeman", "Lizardfolk", "Humanoid", "Fiend",
    "Kobold", "Ooze", "Monstrosity", "Undead", "Orc", "Plant", "Troglodyte"]

def calculate_party_level(level: int, n_players: int) -> int:
    return level * n_players

def convert_difficulty(difficulty: str) -> int:
    print(f"{RED}Function: convert_difficulty{RESET}")
    difficulty = difficulty.strip().lower()
    difficulties = {"easy": 50, "e": 50,
                    "normal": 75, "n": 75,
                    "hard": 100, "h": 100,
                    "deadly": 125, "d": 125,
                    "impossible": 150, "i": 150}
    return difficulties[difficulty]

def list_monsters_by_family(unfiltered_monster_list:list, family:str)-> list:
    print(f"{RED}Function: list_monsters_by_family{RESET}")
    monster_list = list()
    for monster in unfiltered_monster_list:
        if monster.type != "Legendary":
            monster_list.append(monster)

    if family not in family_list:
        return monster_list

    final_monster_list = list()
    for monster in monster_list:
        if monster.family == family:
            final_monster_list.append(monster)
    return final_monster_list