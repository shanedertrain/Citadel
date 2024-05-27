import random

from typing import Optional, List

from character_cards import CharacterCard
from district_cards import DistrictCard

class Player:
    def __init__(self, name):
        self.name = name
        self.character: Optional[CharacterCard] = None
        self.hand: List[DistrictCard] = []  # District cards in hand
        self.city: List[DistrictCard] = []  # District cards played into the city
        self.gold = 2
        self.skipped = False

    def draw_district_cards(self, deck, num_cards=2) -> List[DistrictCard]:
        drawn_cards = [deck.pop() for _ in range(num_cards)]
        self.hand.extend(drawn_cards)  # Add drawn cards to hand
        return drawn_cards

    def discard_card(self, card):
        self.hand.remove(card)
        print(f"{self.name} discarded: {card}")

    def choose_gold_or_cards(self, deck):
        choice = random.choice(["gold", "cards"])
        if choice == "gold":
            self.gold += 2
            print(f"{self.name} chose to take 2 gold. Total gold: {self.gold}")
        else:
            drawn_cards = self.draw_district_cards(deck)
            print(f"{self.name} drew: {[str(card) for card in drawn_cards]}")

            card_to_keep = random.choice(drawn_cards)
            
            drawn_cards.remove(card_to_keep)
            card_to_discard = drawn_cards[0]
            
            print(f"{self.name} kept: {card_to_keep} and discarded: {card_to_discard}")

    def play_card(self, card):
        if card in self.hand:
            if self.gold >= card.cost:  # Check if player has enough gold
                self.hand.remove(card)
                self.city.append(card)
                self.gold -= card.cost  # Deduct card cost from player's gold
                print(f"{self.name} played district card: {card}. Gold remaining: {self.gold}")
            else:
                print(f"{self.name} does not have enough gold to play {card}.")
        else:
            print(f"{self.name} does not have {card} in hand.")

    def take_turn(self, other_players, deck):
        print(f"{self.name}'s turn with {self.character}")
        self.choose_gold_or_cards(deck)
        self.play_card(random.choice(self.hand))  # Simulate playing a random card
        if self.character:
            self.character.use_ability(self, other_players)