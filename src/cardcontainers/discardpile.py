from baseclasses.cardcontainer import CardContainer


class DiscardPile(CardContainer):
    def __init__(self):
        super().__init__()

    def take_cards(self):
        taken_cards = self.cards.copy()
        self.cards = []
        return taken_cards

    def discard_hand(self, playerhand):
        while len(playerhand.get_cards() > 0):
            card = playerhand.pop_card(0)
            self.cards.append(card)
