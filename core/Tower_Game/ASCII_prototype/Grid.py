from random import choice, randint
from Map import *

class Grid():
    def __init__(self, x_axis:int, y_axis:int):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.grid_id = create_grid_id(x_axis, y_axis)
        
        self.grid = fill_grid(self.grid_id, x_axis, y_axis)


# Grid id creation (Which tile is in each position of the grid)
def create_grid_id(x_axis, y_axis):
    grid_id = []
    for x in range(x_axis):
        grid_line = []
        for y in range(y_axis):
            #grid_line.append(choice(list(tiles.values())))
            grid_line.append(tiles["floor"])
        grid_id.append(grid_line)
    return grid_id    


# Grid symbols disposition (How the grid will be displayed)
def fill_grid(grid_id, x_axis, y_axis):
    grid = []
    for x in range(x_axis):
        grid_line = []
        for y in range(y_axis): 
            grid_line.append(grid_id[x][y].symbol)
            # grid_line.append("-  ")
            
            # Sobreposition of tiles (Borders must be walls)
            if x == 0 or y == 0 or y == y_axis - 1 or x == x_axis - 1:
                if x == 0 and y < y_axis - 1 or x == x_axis - 1 and y < y_axis - 1:
                    grid_line[y] = "███" # Wall
                else:
                    grid_line[y] = "█  " # Wall
        
        grid.append(grid_line)
    return grid 

def print_grid(grid):
    x = len(grid)
    y = len(grid[0])
    print(f"[{x}, {y}]")
    for i in range(x):
        centralizer = "                    "          # 6 'tabs' to the right
        line = centralizer
        for j in range(y):
            line += grid[i][j]
        print(line)
