import random

from typing import List

from district_card_base import DistrictCard, Color
from player import Player

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
DECK: List[DistrictCard] = [
    # Blue (Religious)
    DistrictCard("Temple", 1, Color.BLUE),
    DistrictCard("Church", 2, Color.BLUE),
    DistrictCard("Monastery", 3, Color.BLUE),
    DistrictCard("Cathedral", 5, Color.BLUE),

    # Yellow (Trade)
    DistrictCard("Tavern", 1, Color.YELLOW),
    DistrictCard("Market", 2, Color.YELLOW),
    DistrictCard("Trading Post", 2, Color.YELLOW),
    DistrictCard("Docks", 3, Color.YELLOW),
    DistrictCard("Harbor", 4, Color.YELLOW),
    DistrictCard("Town Hall", 5, Color.YELLOW),

    # Red (Military)
    DistrictCard("Watchtower", 1, Color.RED),
    DistrictCard("Prison", 2, Color.RED),
    DistrictCard("Barracks", 3, Color.RED),
    DistrictCard("Fortress", 5, Color.RED),

    # Green (Noble)
    DistrictCard("Manor", 3, Color.GREEN),
    DistrictCard("Castle", 4, Color.GREEN),
    DistrictCard("Palace", 5, Color.GREEN),

    # Purple (Unique)
    DistrictCard("Haunted City", 2, Color.PURPLE, haunted_city_ability),
    DistrictCard("Keep", 3, Color.PURPLE, keep_ability),
    DistrictCard("Laboratory", 5, Color.PURPLE, laboratory_ability),
    DistrictCard("Smithy", 5, Color.PURPLE, smithy_ability),
    DistrictCard("Observatory", 5, Color.PURPLE, observatory_ability),
    DistrictCard("Graveyard", 5, Color.PURPLE, graveyard_ability),
    DistrictCard("Library", 6, Color.PURPLE, library_ability),
    DistrictCard("School of Magic", 6, Color.PURPLE, school_of_magic_ability),
    DistrictCard("University", 6, Color.PURPLE, university_ability),
    DistrictCard("Dragon Gate", 6, Color.PURPLE, dragon_gate_ability)
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
