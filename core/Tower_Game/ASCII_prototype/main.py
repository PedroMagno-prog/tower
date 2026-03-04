from GridMap import *
from Map_db import *
import os
import time
import sys
from core.colors import *
sys.stdout.reconfigure(encoding='utf-8')

def menu():
    print(f"{HIGHLIGHT}===================================={RESET}")
    print(f"{HIGHLIGHT}{BOLD}            THE TOWER               {RESET}")
    print(f"{HIGHLIGHT}===================================={RESET}")
    #print(f"{H3}{ITALIC}Hey you fool! Want to enter the Tower? Maybe you are worthy....\nbut first...{RESET}")
    #print(f"\n{H1}~~~WHO YOU ARE??~~~{RESET}\n")
    
    print()
    print("=" * 56,
          "\nChoose an option:"
          "\n(1) Continue"
          "\n(2) New Game"
          "\n(3) Save & Quit"
          "\nType any other value to exit"
          )
    print("=" * 56)
    option = input("--> ")
    # --- The "Dispatch Table" ---
    # We use 'lambda' to "delay" execution
    # and to pass the correct arguments (party_level, floor).
    options = {
        '1': lambda: enter_combat(), # !!!!!!!!!!!!!!!!!!!!
        '2': lambda: enter_map(),
        
        #'3': lambda: save_all_data()
    }
    function_to_execute = options.get(option)

    if function_to_execute:
        function_to_execute()  # Executes the lambda (which calls the real function)
        return True  # Returns True to continue the loop 'while menu_option:'
    else:
        print("\nReturning to initial setup...")
        return False  # Returns False to break the loop 'while menu_option:'

def enter_map():
    first_level = Map(31, 26, "dungeon")
    first_level.generate_map()
    while True:
    
        first_level.generate_terrain(6, 3, 3, tile=all_tiles["water"])
        first_level.generate_terrain(1, 1, 7, tile=all_tiles["monster"], irregular=False)
        first_level.generate_terrain(5, 3, 3, tile=all_tiles["mountains"], irregular=True)
        first_level.generate_terrain(2, 2, 3, tile=all_tiles["trees"], irregular=True)
        
        first_level.print_map()
        time.sleep(0.5)
        print()
        if input("Back to the menu? (y/n) --> ") == "n":
            break
        os.system('cls')


def main():
    os.system('cls')
    # floor1 = Map(26, 31, )
    while True:
        menu()
    


main()


















"""
class Player(object):
    def __init__(self, name):
        self.name = name

    def movement(self):
        while True:
            print room.userpos
            move = raw_input("[W], [A], [S], or [D]: ").lower() #Movement WASD.
            while True:
                if move == 'w':  #Have only coded the 'w' of the wasd for simplicity. 
                    x, y = (1, 0)   #x, y are column, row respectively.  This is done
                    break           ##to apply changes to the player's position on the map.
            a = room.column + x  #a and b represent the changes that take place to player's 
            b = room.row + y  ##placement index in the map, or 'tilemap' list.
            room.userpos = tilemap[a][b]
            if room.userpos == 3:
                print "LOOT!"   #Representing what happens when a player comes across
            return room.userpos ##a tile with the value 3 or 'loot'.
            break               

class Room(object):
    def __init__(self, column, row):
        self.userpos = tilemap[column][row]
        self.column = column    #Column/Row dictates player position in tilemap.
        self.row = row

floor = 0
entry = 1
exit = 2
loot = 3                #Tile map w/ vairbale names.
tilemap = [[0, 1, 0],   #[floor, entry, floor],  
           [3, 0, 0],   #[loot, floor, floor],
           [0, 2, 0]]   #[floor, exit, floor]

room = Room(0, 0)       #Player position for 'room' and 'Room' class -- too similar names
user = Player('Bryce')  #for larger exercices, but I figure I could get away with it here.

def main():     #Loads the rest of the program -- returns user position results.
    inp = raw_input("Press any button to continue.: ")  
    if inp != '':
        user.movement()
        print room.userpos
main()  
"""