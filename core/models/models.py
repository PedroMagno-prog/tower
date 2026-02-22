class Monster:

    def __init__(self, name, type, family, level, description=None):

        self.name = name
        self.type = type
        self.family = family
        self.level = level
        self.description = description

    def __str__(self):
        # This helps to identify the object in the Django admin
        return f"{self.name} (Level {self.level})"


class Loot:

    def __init__(self, name, rarity, value, description=None):

        self.name = name
        self.rarity = rarity
        self.value = value
        self.description = description

    def __str__(self):
        return f"Loot: {self.name}, Rarity: {self.rarity}, Value: {self.value}"