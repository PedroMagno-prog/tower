# from functions.useful import calculate_party_level
# from functions.rng import open_chest, generate_encounter
# from functions.manager_db import (
#     load_monster_data,
#     load_loot_data,
#     save_data,
#     create_monster,
#     register_monster,
#     register_loot,
#     view_monsters,
#     view_loots
# )
from functions.manager_db import *
from functions.useful import *
from functions.rng import *

value_in_gp = {} # table rarity with a value X in GP


def menu(party_level, floor, n_players):
    # menu that processes once. In Main we have the infinite loop
    print("=" * 56,
          "\nChoose an option:"
          "\n(1) Register Monster"
          "\n(2) Register Loot"
          "\n(3) View Monsters"
          "\n(4) View Loot"
          "\n(5) Create a Monster"
          "\n(6) Generate an Encounter"
          "\n(7) Open a Chest"
          "\n\n(10) SAVE"
          "\nType any other value to exit"
          )
    print("=" * 56)
    option = input("--> ")
    # --- The "Dispatch Table" ---
    # We use 'lambda' to "delay" execution
    # and to pass the correct arguments (party_level, floor).
    options = {
        '1': lambda: register_monster(),
        '2': lambda: register_loot(),
        '3': lambda: view_monsters(),
        '4': lambda: view_loots(),
        '5': lambda: create_monster(),
        '6': lambda: generate_encounter(party_level),
        '7': lambda: open_chest(floor, n_players),
        '10': lambda: save_all_data()
    }
    # 1. Use .get() to fetch functions.
    # 2. If 'option' (e.g., '1') exists, 'function_to_execute'
    #    receives the lambda (e.g., lambda: create_monster()).
    # 3. If 'option' (e.g., '5') doesn't exist, 'function_to_execute' is 'None'.
    function_to_execute = options.get(option)

    if function_to_execute:
        function_to_execute()  # Executes the lambda (which calls the real function)
        return True  # Returns True to continue the loop 'while menu_option:'
    else:
        print("\nReturning to initial setup...")
        return False  # Returns False to break the loop 'while menu_option:'
    pass

def main():
    load_all_data()
    while True:
        print("="*20 + "Welcome Creator_Dev!" + "="*20)
        print()
        print("Before we start, we need to define some values... ")
        try:
            n_players = int(input("How many players are playing? --> "))
            level = int(input("What level are they individually? (Ex: everyone is level 3) --> "))
            party_level = calculate_party_level(level, n_players)
            print("Party Level is " + str(party_level))
            floor = int(input("What floor is the party on? --> "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


        menu_option = True
        while menu_option:
            menu_option = menu(party_level, floor, n_players)

    print("Program finished")
    pass


if __name__ == "__main__":
    main()
