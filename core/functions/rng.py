from scipy.interpolate import lagrange
from functions.manager_db import load_monster_data
from random import choice, choices
from functions.useful import convert_difficulty, list_monsters_by_family


"""
            Floor 1
C: 80 -- U: 15 -- R: 4 -- E: 0.9 -- L: 0.1
            Floor 25
C: 70 -- U: 20 -- R: 8 -- E: 1.5 -- L: 0.5
            Floor 50
C: 55 -- U: 30 -- R: 10 -- E: 4 -- L: 1
            Floor 75
C: 35 -- U: 20 -- R: 25 -- E: 15 -- L: 5
            Floor 100
C: 5 -- U: 10 -- R: 40 -- E: 30 -- L: 15
"""
FLOORS =        [1,   25,  50, 75, 100]
WEIGHTS = {"Common":[80,  70,  55, 35, 5],
       "Uncommon":[15,  20,  30, 20, 10],
          "Rare":[4,   8,   10, 25, 40],
        "Epic": [0.9, 1.5, 4,  15, 30],
     "Legendary": [0.1, 0.5, 1,  5,  15]}



print("="*56)
# index: [0] = Floor 1; [1] = Floor 25; [2] = Floor 50; [3] = Floor 75; [4] = Floor 100

"""
DIFFICULTY == inversely proportional to the weight of COMMON rarity

Dif = 0% ; common_weight = 100%
Dif = 50% ; common_weight = 50%
Dif = 100% ; common_weight = 0% 
"""

def rng_rarity(floor:int, difficulty:int) -> dict:

    rng_polys = {}    # dictionary, with the 'poly' function for each rarity
    final_weights = {} # dictionary, with the final weights for each rarity, for the selected floor

    for r in WEIGHTS:
        rng_polys[r] = lagrange(FLOORS, WEIGHTS[r])
    for r in rng_polys:
        p = rng_polys[r](floor)
        if r == "Common":
            final_weights[r] = p - p*(difficulty/100)
        else:
            final_weights[r] = p

    return final_weights

def open_chest(floor:int, n_players:int) -> list:
    try:
        difficulty = input("What was the difficulty of the encounter you just had?\n"
                        "   type: easy, normal, hard, deadly or impossible: ")
        difficulty = convert_difficulty(difficulty)
    except:
        difficulty = 0

    weights = rng_rarity(floor, difficulty)
    rarities = list(weights.keys())
    weights = list(weights.values())

    return list((choices(rarities, weights=weights)[0]) for _ in range(n_players))

def generate_encounter(party_level):
    difficulty = 0
    while difficulty == 0:
        try:
            difficulty = input("What was the difficulty of the encounter you just had?\n"
                                "   type: easy, normal, hard, deadly or impossible: ")
            difficulty = convert_difficulty(difficulty)
        except:
            difficulty = 0
    max_monster_level = (difficulty/100) * party_level
    print(f"Total monster level will be: {max_monster_level}")

    family = input(""
        "\n==> Bandit: Outlaw humans."
        "\n==> Goblin: Goblins, Bugbears and Hobgoblins. "
        "\n==> Kobold: Kobolds."
        "\n==> Undead: Skeletons, Zombies, Mummies, Vampires, Death Knights, etc."
        "\n==> Snakeman: Snakemen."
        "\n==> Troglodyte: Troglodytes."
        "\n==> Plant: Plant monsters (Seedlings, Treants)."
        "\n==> Fey: Fey creatures (Sprites, Gremlins, Mav)."
        "\n==> Fiend: Demons and devils."
        "\n==> Beast: Animals (Wolves, Raptors, Bats) and bestial creatures."
        "\n==> Cultist: Fanatical humans."
        "\n==> Gnoll: Gnolls."
        "\n==> Ooze: Oozes and Jellies."
        "\n==> Dragon: Drakes and Dragons."
        "\n==> Spider: Giant Spiders and Ettercaps."
        "\n==> Monstrosity: Hybrid or unnatural creatures (Mimics, Griffons, Chimeras, Aberrations)."
        "\n==> Construct: Mana machines (Scions, Hulks, Titans)"
        "\n==> Humanoid: General NPCs (Druids, Mages)."
        "\n==> Lizardfolk: Lizardfolk."
        "\n==> Orc: Orcs."
        "\n==> Giant: Giants, Trolls and Ogres."
        "\n==> Drow: Drow and Driders."
        "\n==> Aberration: Alien or psychic creatures (Cloakers, Ul'vek, Dravok)."
        "\n\nWhich monster family will compose the encounter? Or leave empty to use all: ")

    monster_list = load_monster_data(True)
    final_monster_list = list_monsters_by_family(monster_list, family)

    sum_monster_level = 0
    encounter = list()

    while sum_monster_level < max_monster_level:
        monster = choice(final_monster_list)
        if monster.level+sum_monster_level > max_monster_level:
            continue
        encounter.append(monster)
        sum_monster_level += monster.level
    for m in encounter:
        print(m)

    pass

# print(open_chest(78, 4))
# generate_encounter(20)