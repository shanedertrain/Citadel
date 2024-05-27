from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    PURPLE = 5

class DistrictCard:
    def __init__(self, name, cost, color, ability=None):
        self.name = name
        self.cost = cost
        self.color = color
        self.ability = ability

    def use_ability(self):
        if self.ability:
            return self.ability()
        else:
            return "No ability."

    def __repr__(self):
        return f"{self.name} (Cost: {self.cost}, Color: {self.color})"