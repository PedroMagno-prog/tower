import json
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MONSTERS_FILE = os.path.join(BASE_DIR, 'database', 'monsters.json')

# Mappings
KEY_MAPPING = {
    "nome": "name",
    "tipo": "type",
    "familia": "family",
    "nivel": "level",
    "descricao": "description"
}

TYPE_MAPPING = {
    "Normal": "Normal",
    "Minion": "Minion",
    "Lendario": "Legendary"
}

FAMILY_MAPPING = {
    "Bandido": "Bandit",
    "Goblin": "Goblin",
    "Kobold": "Kobold",
    "Morto-Vivo": "Undead",
    "Homem-Cobra": "Snakeman",
    "Troglodita": "Troglodyte",
    "Planta": "Plant",
    "Fada": "Fey",
    "Infernal": "Fiend",
    "Fera": "Beast",
    "Cultista": "Cultist",
    "Gnoll": "Gnoll",
    "Limo": "Ooze",
    "Homem-Lagarto": "Lizardfolk",
    "Monstruosidade": "Monstrosity",
    "Dragão": "Dragon",
    "Aranha": "Spider",
    "Humanoide": "Humanoid",
    "Constructo": "Construct",
    "Gigante": "Giant",
    "Elfo Negro": "Drow"
}

def translate_monsters():
    if not os.path.exists(MONSTERS_FILE):
        print(f"File not found: {MONSTERS_FILE}")
        return

    with open(MONSTERS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_data = []
    for monster in data:
        new_monster = {}
        for key, value in monster.items():
            new_key = KEY_MAPPING.get(key, key)
            new_value = value

            if key == "tipo":
                new_value = TYPE_MAPPING.get(value, value)
            elif key == "familia":
                new_value = FAMILY_MAPPING.get(value, value)
            
            new_monster[new_key] = new_value
        new_data.append(new_monster)

    with open(MONSTERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully translated {len(new_data)} monsters.")

if __name__ == "__main__":
    translate_monsters()
