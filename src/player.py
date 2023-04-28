from baseclasses.creature import Creature

class Player(Creature):
    def __init__(self, health, starter_deck):
        super().__init__(health)
        self._deck = starter_deck

    def get_deck(self):
        return self._deck