from random import choice, randint
from Map_db import *
from useful import *

class Grid():
    def __init__(self, x_axis:int, y_axis:int):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.grid_id = create_grid_id(x_axis, y_axis)
        
        self.grid = fill_grid(self.grid_id, x_axis, y_axis)


# Grid id creation (Which tile is in each position of the grid)
def create_grid_id(x_axis, y_axis):
    grid_id = []
    for y in range(y_axis):
        grid_line = []
        for x in range(x_axis):
            grid_line.append(all_tiles["floor"])
        grid_id.append(grid_line)
    return grid_id    


# Grid symbols disposition (How the grid will be displayed)
def fill_grid(grid_id, x_axis, y_axis):
    grid = []
    for y in range(y_axis):
        grid_line = []
        for x in range(x_axis): 
            grid_line.append(grid_id[y][x].symbol)
            # grid_line.append("-  ")
            
            # Sobreposition of tiles (Borders must be walls)
            if x == 0 or y == 0 or y == y_axis - 1 or x == x_axis - 1:
                if y == 0 and x < x_axis - 1 or y == y_axis - 1 and x < x_axis - 1:
                    grid_line[x] = "███" # Wall
                else:
                    grid_line[x] = "█  " # Wall
        
        grid.append(grid_line)
    return grid 

class Map(Grid):
    
    def __init__(self, x_axis:int, y_axis:int, biome:str="dungeon"):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.biome = biomes[biome]
        self.grid = create_grid_id(x_axis, y_axis)
        self.map = None

    def generate_map(self):
        self.map = fill_grid(self.grid, self.x_axis, self.y_axis)    
    
    # generate terrain from top-left to bottom-right from a random point inside the map
    def generate_terrain(self, width:int, height:int, num_areas:int, tile:Tile, irregular:bool=True):
        
        border_symbol = limpar_ultimo_caractere(tile.symbol)
        for _ in range(num_areas):
            # Mapeamento de inícios para evitar sobreposição
            pass
        for n in range(num_areas):
            
            start_x = randint(1, max(1, self.x_axis - width - 1))
            final_x = start_x + width
            start_y = randint(1, max(1, self.y_axis - height - 1))           
        
            for i in range(height):
                if irregular:
                    vv = randint(-1, 1)
                    # width = randint(width//2, width)  
                for j in range(width):
                    if irregular:
                        if 1 < start_x + j + vv < self.x_axis - 1 and start_y + i < self.y_axis - 1:
                            self.map[start_y + i][start_x + j + vv] = tile.symbol
                        if j == width:
                            self.grid[start_y + i][start_x + j] = border_symbol
                    else:
                        if 1 < start_x + j < self.x_axis - 1 and 1 < start_y + i < self.y_axis - 1:
                            self.map[start_y + i][start_x + j] = tile.symbol
                        if j == width:
                            self.grid[start_y + i][start_x + j] = border_symbol
        

    def print_map(self):
        if not self.map == None:
            x = self.x_axis
            y = self.y_axis
            print(f"[{x}, {y}]\n")
            centralizer = "                    " # 6 'tabs' to the right
            for i in range(y):
                line = centralizer
                for j in range(x):
                    line += self.map[i][j]
                print(line)
        else:
            print("Map not generated")

            

