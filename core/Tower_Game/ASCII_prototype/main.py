from ASCII_prototype.GridMap import create_grid, print_grid
import os
import time

def main():
    os.system('cls')
    x = 17
    y = 17
    grid = create_grid(x, y)

    while True:
        print_grid(grid, x, y)
        time.sleep(0.5)
        print()
        input()
        os.system('cls')

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