import sys
import os
# Add the project root (tower) to sys.path so that absolute imports work regardless of how the script is run.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tower.core.functions.dice_roller import *
from tower.core.functions.manager_db import *
from tower.core.functions.colors import *
from tower.core.functions.rng import *
from tower.core.functions.useful import *
from tower.core.models.models import *


def game_on():
    load_all_data()
    
    character_list = load_character_data(return_list=True)

    if character_list != []:
        print("Escolha seu herói:")
        for character in character_list:
            print(character)
    
        
game_on()


















game_on(Flecher)
