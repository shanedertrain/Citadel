import random

from typing import List

from character_cards import CHARACTERS, King
from district_cards import DistrictCard, DECK
from player import Player

def initialize_game(player_names):
    players = [Player(name) for name in player_names]
    deck = DECK.copy()
    random.shuffle(deck)
    return players, deck

def evaluate_player_scores(players: List[Player]):
    # Calculate points for each player based on the specified conditions
    for player in players:
        total_gold_cost = sum(card.cost for card in player.city)  # Total gold cost of all district cards
        num_colors = len(set(card.color for card in player.city))  # Number of unique colors in the player's city
        num_districts = len(player.city)  # Number of districts built by the player

        # Points for total gold cost of district cards
        player.points = total_gold_cost

        # Points for having at least one district in each of the five colors
        if num_colors == 5:
            player.points += 3

        # Points for being the first player to build eight districts
        if num_districts >= 8:
            if not any(p.points > 0 for p in players if p != player):
                player.points += 4
            else:
                player.points += 2  # All other players who have managed to build eight districts

    # Print scoreboard
    print("Scoreboard:")
    for player in players:
        print(f"{player.name}: Points - {player.points}, Gold - {player.gold}")

    # Determine the winner based on points
    winner = max(players, key=lambda player: (player.points, player.gold))
    print(f"The winner is {winner.name} with {winner.points} points and {winner.gold} gold.")

def check_game_over_condition(players):
    # Check if any player has built eight or more districts
    for player in players:
        if len(player.city) >= 8:
            return True  # Set game_over flag to True
    return False  # Game is not over if no player has built eight or more districts

def main():
    player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
    players, deck = initialize_game(player_names)
    game_over = False  # Initialize game over condition

    while not game_over:
        characters_deck = CHARACTERS.copy()

        # Part 1: Randomly remove a character card from available characters
        random_character = random.choice(characters_deck)
        characters_deck.remove(random_character)
        print(f"Randomly removed character: {random_character.name}")

        # Calculate the number of characters to discard
        num_players = len(players)
        num_remaining_characters = len(characters_deck)
        num_to_discard = num_players + 1 - num_remaining_characters

        # Part 2: Discard characters and show them to players
        discarded_characters = characters_deck[:num_to_discard]
        print("Discarded characters:")
        for character in discarded_characters:
            print(character.name)
        characters_deck = characters_deck[num_to_discard:]

        # Determine the order of character selection starting from the player who last had the King
        king_index = None
        for i, player in enumerate(players):
            if player.character and isinstance(player.character, King):
                king_index = i
                break
        if king_index is None:
            king_index = random.randint(0, num_players - 1)

        # Iterate through players in order starting from the player who last had the King
        for i in range(num_players):
            current_player_index = (king_index + i) % num_players
            current_player = players[current_player_index]
            available_characters_names = [character.name for character in characters_deck]
            print(f"{current_player.name} can choose from: {available_characters_names}")
            
            chosen_character_name = random.choice(available_characters_names)
            chosen_character = next(character for character in characters_deck if character.name == chosen_character_name)
            current_player.character = chosen_character
            print(f"{current_player.name} chose: {chosen_character_name}")
            
            characters_deck.remove(chosen_character)

        # Discard the remaining character without showing it to players
        remaining_character = characters_deck[0]
        print(f"Discarded remaining character: {remaining_character.name}")

        # Sort players based on the value of their character cards
        players.sort(key=lambda player: player.character.value)

        # Simulate turns
        for player in players:
            if not player.skipped:
                other_players = [p for p in players if p != player]
                player.take_turn(other_players, deck)
            else:
                print(f"{player.name} is dead and their turn will be skipped.")

        # Check if game over condition is met
        # For example, if there's only one player left or a specific condition is met
        if check_game_over_condition(players):
            game_over = True

        # Reset any skipped players
        for player in players:
            player.skipped = False

    # Evaluate win conditions
    evaluate_player_scores(players)

if __name__ == "__main__":
    main()