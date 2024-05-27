import random

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

# Define abilities as functions
def haunted_city_ability():
    return "Counts as any color for abilities."

def keep_ability():
    return "Cannot be destroyed."

def laboratory_ability():
    return "Once per turn, discard a card for 2 gold."

def smithy_ability():
    return "Once per turn, pay 2 gold to draw 3 cards."

def observatory_ability():
    return "When drawing cards, draw 3 and keep 2."

def graveyard_ability():
    return "Pay 1 gold to keep a destroyed district."

def library_ability():
    return "When drawing cards, keep all."

def school_of_magic_ability():
    return "Counts as any color for income."

def university_ability():
    return "Worth 8 points."

def dragon_gate_ability():
    return "Worth 8 points."

# List of all district cards in the game
DECK = [
    # Blue (Religious)
    DistrictCard("Temple", 1, "Blue"),
    DistrictCard("Church", 2, "Blue"),
    DistrictCard("Monastery", 3, "Blue"),
    DistrictCard("Cathedral", 5, "Blue"),

    # Yellow (Trade)
    DistrictCard("Tavern", 1, "Yellow"),
    DistrictCard("Market", 2, "Yellow"),
    DistrictCard("Trading Post", 2, "Yellow"),
    DistrictCard("Docks", 3, "Yellow"),
    DistrictCard("Harbor", 4, "Yellow"),
    DistrictCard("Town Hall", 5, "Yellow"),

    # Red (Military)
    DistrictCard("Watchtower", 1, "Red"),
    DistrictCard("Prison", 2, "Red"),
    DistrictCard("Barracks", 3, "Red"),
    DistrictCard("Fortress", 5, "Red"),

    # Green (Noble)
    DistrictCard("Manor", 3, "Green"),
    DistrictCard("Castle", 4, "Green"),
    DistrictCard("Palace", 5, "Green"),

    # Purple (Unique)
    DistrictCard("Haunted City", 2, "Purple", haunted_city_ability),
    DistrictCard("Keep", 3, "Purple", keep_ability),
    DistrictCard("Laboratory", 5, "Purple", laboratory_ability),
    DistrictCard("Smithy", 5, "Purple", smithy_ability),
    DistrictCard("Observatory", 5, "Purple", observatory_ability),
    DistrictCard("Graveyard", 5, "Purple", graveyard_ability),
    DistrictCard("Library", 6, "Purple", library_ability),
    DistrictCard("School of Magic", 6, "Purple", school_of_magic_ability),
    DistrictCard("University", 6, "Purple", university_ability),
    DistrictCard("Dragon Gate", 6, "Purple", dragon_gate_ability)
]

# Function to shuffle and draw district cards
def draw_district_cards(deck, num_cards):
    random.shuffle(deck)
    drawn_cards = deck[:num_cards]
    return drawn_cards

if __name__ == "__main__":
    # Draw 4 district cards as an example
    drawn_cards = draw_district_cards(DECK, 4)

    # Display the drawn cards and their abilities
    for card in drawn_cards:
        print(f"{card}: {card.use_ability()}")
