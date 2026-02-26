class Character():
    def __init__(self, name:str, symbol:str, x_y:list):
        self.name = name
        self.symbol = symbol
        self.x_y = x_y
    def __str__(self):
        return f"{self.name} {self.symbol} {self.x_y}"

class Hero(Character):
    pass
class Monster(Character):
    pass

class Item(Character):
    def coletar(self):
        print(f"Você coletou {self.name}!")
    pass
