import json
import os
from core.models.models import Monster, Loot, Archetype, Character
from core.colors import RED, RESET, LIGHTBLUE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.dirname(BASE_DIR)

MONSTERS_FILE = os.path.join(CORE_DIR, "database", "monsters.json")
LOOTS_FILE = os.path.join(CORE_DIR, "database", "loots.json")
ARCHETYPES_FILE = os.path.join(CORE_DIR, "database", "archetypes.json")
CHARACTERS_FILE = os.path.join(CORE_DIR, "database", "characters.json")

# Will be populated with objects from models classes
monster_list = []
loot_list = []
archetype_list = []
character_list = []

# --- Nested Classes  ---
def custom_serializer(obj):
    """Fallback for objects json module does not know how to serialize."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    # If it's an Enum, you can return obj.name or obj.value here
    return str(obj)

def save_all_data():
    # Save lists created during runtime to JSON files
    print("Saving data...")
    # Transforms objects from models classes into dictionaries
    monsters_data = [monster.__dict__ for monster in monster_list]
    loots_data = [loot.__dict__ for loot in loot_list]
    archetypes_data = [loot.__dict__ for loot in archetype_list]
    characters_data = [character.__dict__ for character in character_list]

    # Dump the dictionaries into JSON files
    with open(MONSTERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(monsters_data, f, indent=4, ensure_ascii=False, default=custom_serializer)
    with open(LOOTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(loots_data, f, indent=4, ensure_ascii=False, default=custom_serializer)
    with open(ARCHETYPES_FILE, 'w', encoding='utf-8') as f:
        json.dump(archetypes_data, f, indent=4, ensure_ascii=False, default=custom_serializer)
    with open(CHARACTERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(characters_data, f, indent=4, ensure_ascii=False, default=custom_serializer)

    print("Data saved successfully!")
    pass


# --- Loads ---

def load_monster_data(return_list=False):
    """Loads data from JSON files into memory lists."""
    global monster_list

    if os.path.exists(MONSTERS_FILE):
        with open(MONSTERS_FILE, 'r', encoding='utf-8') as f:
            # Read raw data (list of dictionaries)
            monsters_data = json.load(f)
            # **data is a shortcut to unpack the dictionary
            # It's the same as: Monster(name=data['name'], type=data['type'], ...)
            monster_list = [Monster(**data) for data in monsters_data]
    if return_list:
        return monster_list
    else:
        print(f"{RED}Function: load_monster_data{RESET}")
        print(f"{LIGHTBLUE}Data loaded: {len(monster_list)} monsters{RESET}\n")

def load_loot_data(return_list=False):
    """Loads data from JSON files into memory lists."""
    global loot_list

    if os.path.exists(LOOTS_FILE):
        with open(LOOTS_FILE, 'r', encoding='utf-8') as f:
            # Read raw data (list of dictionaries)
            loots_data = json.load(f)
            # **data is a shortcut to unpack the dictionary
            # It's the same as: Loot(name=data['name'], rarity=data['rarity'], ...)
            loot_list = [Loot(**data) for data in loots_data]
    if return_list:
        return loot_list
    else:
        print(f"{RED}Function: load_loot_data{RESET}")
        print(f"{LIGHTBLUE}Data loaded: {len(loot_list)} loots.{RESET}\n")

def load_archetype_data(return_list=False):
    """Loads data from JSON files into memory lists."""
    global archetype_list

    if os.path.exists(ARCHETYPES_FILE):
        with open(ARCHETYPES_FILE, 'r', encoding='utf-8') as f:
            # Read raw data (list of dictionaries)
            archetypes_data = json.load(f)
            # **data is a shortcut to unpack the dictionary
            # It's the same as: Archetype(name=data['name'], key_stats=data['key_stats'], ...)
            archetype_list= [Archetype(**data) for data in archetypes_data]
    if return_list:
        return archetype_list
    else:
        print(f"{RED}Function: load_archetype_data{RESET}")
        print(f"{LIGHTBLUE}Data loaded: {len(archetype_list)} archetypes.{RESET}\n")

def load_character_data(return_list=False):
    """Loads data from JSON files into memory lists."""
    global character_list

    if os.path.exists(CHARACTERS_FILE):
        with open(CHARACTERS_FILE, 'r', encoding='utf-8') as f:
            # Read raw data (list of dictionaries)
            characters_data = json.load(f)
            # **data is a shortcut to unpack the dictionary
            # It's the same as: Character(name=data['name'], archetype=data['archetype'], ...)
            character_list = [Character(**dict) for dict in characters_data]
    if return_list:
        return character_list
    else:
        print(f"{RED}Function: load_character_data{RESET}")
        print(f"{LIGHTBLUE}Data loaded: {len(character_list)} characters.{RESET}\n")


def load_all_data():
    try:
        load_monster_data()
        load_loot_data()
        load_archetype_data()
        load_character_data()
    except Exception as e:
        print(f"Something went wrong while loading data: {e}")


# --- Registers ---

def register_monster():
    print("Let's register some monsters! (type 'nimble' in the NAME field to exit)")
    print("=" * 56)
    while True:
        try:
            name = input("What is its name? --> ")
            if name == 'nimble':
                print("Returning to menu... ")
                return
            type_ = input("Is it Minion(m), Normal(n) or Legendary(l)? --> ")
            if type_ == "n":
                type_ = "Normal"
            elif type_ == "l":
                type_ = "Legendary"
            elif type_ == "m":
                type_ = "Minion"
            else:
                raise Exception
            family = "Neutral"
            print("Saving Monster as Neutral Family (Only spawns when encounter is random)")
            level = float(input("What is its level? --> "))
            description = input("Describe the monster (optional) \n-->")
            new_monster = Monster(name=name, type=type_, family=family, level=level, description=description)
            monster_list.append(new_monster)
            print(f"\nMonster '{new_monster.name}' was registered. Don't forget to save!")
        except:
            print("Try Again")
            continue

    pass

def register_loot():
    print("Let's register some LOOT! (type 'nimble' in the NAME field to exit)")
    print("=" * 56)
    while True:
        try:
            name = input("What is the item's name? --> ")
            if name == 'nimble':
                print("Returning to menu... ")
                return
            rarity = input("Is it Common(c), Uncommon(u), Rare(r), Epic(e) or Legendary(l)? --> ")
            if rarity == "c":
                rarity = "Common"
            elif rarity == "u":
                rarity = "Uncommon"
            elif rarity == "r":
                rarity = "Rare"
            elif rarity == "e":
                rarity = "Epic"
            elif rarity == "l":
                rarity = "Legendary"
            else:
                raise Exception
            value = int(input("What is the item's value in Gold Pieces? --> "))
            description = input("Describe the item (optional) \n-->")
            new_loot = Loot(name=name, rarity=rarity, value=value, description=description)
            loot_list.append(new_loot)
            print(f"\nLoot '{new_loot.name}' was registered. Don't forget to save!")
        except:
            print("Try Again")
            continue

    pass


# --- Creators --- DEVELOPING

def create_monster():

    monster_type = input("What type of Monster? Minion (m), Normal(n) or Legendary (l)? --> ")
    if monster_type == "l":
        # In development
        pass
    else:
        print("Do you want ")
        pass
    print("Do you want to create a monster at what level?")
    # create_monster()

    pass

# --- Views ---

def view_monsters():
    print("\n--- List of Registered Monsters ---")
    if not monster_list:
        print("(No monsters registered)")
        return

    # The __str__ you defined is used here!
    for monster in monster_list:
        print(f"- {monster}")

def view_loots():
    print("\n--- List of Registered Loots ---")
    if not loot_list:
        print("(No loots registered)")
        return

    for loot in loot_list:
        print(f"- {loot}")

def view_archetypes():
    print("\n--- List of Registered Archetypes ---")
    if not archetype_list:
        print("(No archetypes registered)")
        return

    for archetype in archetype_list:
        print(f"- {archetype}")

def view_characters():
    print("\n--- List of Registered Characters ---")
    if not character_list:
        print("(No characters registered)")
        return

    for character in character_list:
        print(f"- {character}")