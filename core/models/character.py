from dataclasses import dataclass

@dataclass
class Character:
    name: str
    hp: int
    hp_max: int
    attack: int
    # wounds: int
    mana: int
    def attack(self):
        pass
    def defend(self):
        pass
    def heal(self):
        pass
    def cast_spell(self):
        pass
    def use_item(self):
        pass
    def flee(self):
        pass
    def die(self):
        pass
    def __str__(self):
        return f"Character: {self.name}, HP: {self.hp}/{self.hp_max}, Attack: {self.attack}"

class Hero(Character):
    super().__init__(name, hp, hp_max, attack, mana)
    weapon: str
    armor: str
    
    
    pass

class Monster(Character):
    pass

class Companion(Character):
    pass