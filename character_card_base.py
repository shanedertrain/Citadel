class CharacterCard:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def ability(self):
        return f"{self.name}'s ability"

    def use_ability(self, player, other_players, target_player=None):
        pass