import random

class CharacterCard:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def ability(self):
        return f"{self.name}'s ability"

    def use_ability(self, player, other_players, target_player=None):
        pass

class Assassin(CharacterCard):
    def __init__(self):
        super().__init__("Assassin", 1)

    def use_ability(self, player, other_players, target_player=None):
        print(f"{player.name} uses ability: {self.ability()} on {target_player.name}")
        target_player.skipped = True

class Thief(CharacterCard):
    def __init__(self):
        super().__init__("Thief", 2)

    def use_ability(self, player, other_players, target_player=None):
        stolen_gold = target_player.gold
        player.gold += stolen_gold
        target_player.gold = 0
        print(f"{player.name} uses ability: {self.ability()} on {target_player.name}. Stole {stolen_gold} gold.")

class Magician(CharacterCard):
    def __init__(self):
        super().__init__("Magician", 3)

    def use_ability(self, player, other_players, target_player=None):
        player.city, target_player.city = target_player.city, player.city
        print(f"{player.name} uses ability: {self.ability()} with {target_player.name}. Swapped district cards.")

class King(CharacterCard):
    def __init__(self):
        super().__init__("King", 4)

    def use_ability(self, player, other_players, target_player=None):
        num_yellow_noble = sum(1 for card in player.city if card.color in ["Yellow", "Green"])
        player.gold += num_yellow_noble
        print(f"{player.name} uses ability: {self.ability()}. Gained {num_yellow_noble} gold.")

class Bishop(CharacterCard):
    def __init__(self):
        super().__init__("Bishop", 5)

    def use_ability(self, player, other_players, target_player=None):
        num_blue_religious = sum(1 for card in player.city if card.color in ["Blue", "Religious"])
        player.gold += num_blue_religious
        print(f"{player.name} uses ability: {self.ability()}. Gained {num_blue_religious} gold.")

class Merchant(CharacterCard):
    def __init__(self):
        super().__init__("Merchant", 6)

    def use_ability(self, player, other_players, target_player=None):
        num_green_trade = sum(1 for card in player.city if card.color in ["Green", "Trade"])
        player.gold += 1 + num_green_trade
        print(f"{player.name} uses ability: {self.ability()}. Gained {1 + num_green_trade} gold.")

class Architect(CharacterCard):
    def __init__(self):
        super().__init__("Architect", 7)

    def use_ability(self, player, other_players, target_player=None):
        player.draw_district_cards(deck, num_cards=2)
        print(f"{player.name} uses ability: {self.ability()}. Drew 2 district cards.")

class Warlord(CharacterCard):
    def __init__(self):
        super().__init__("Warlord", 8)

    def use_ability(self, player, other_players, target_player):
        if target_player:
            if target_player.city:
                district_to_destroy = random.choice(target_player.city)
                cost_to_destroy = max(0, district_to_destroy.cost - 1)
                if player.gold >= cost_to_destroy:
                    player.gold -= cost_to_destroy
                    target_player.city.remove(district_to_destroy)
                    print(f"{player.name} uses ability: {self.ability()} to destroy {district_to_destroy} from {target_player.name}")
                else:
                    print(f"{player.name} doesn't have enough gold to destroy a district.")
            else:
                print(f"{target_player.name} has no district cards to destroy.")

# List of characters
CHARACTERS = [
    Assassin(),
    Thief(),
    Magician(),
    King(),
    Bishop(),
    Merchant(),
    Architect(),
    Warlord()
]

def shuffle_and_deal(players):
    random.shuffle(CHARACTERS)
    num_players = len(players)
    dealt_cards = {}

    for i in range(num_players):
        dealt_cards[players[i]] = CHARACTERS[i]

    return dealt_cards

if __name__ == "__main__":
    # Example players
    players = ["Player 1", "Player 2", "Player 3", "Player 4"]

    # Shuffle and deal cards to players
    dealt_cards = shuffle_and_deal(players)

    # Display the dealt cards and their abilities
    for player, card in dealt_cards.items():
        print(f"{player} has {card}: {card.ability()}")
