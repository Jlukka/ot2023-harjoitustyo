from random import shuffle

from baseclasses.cardcontainer import CardContainer


class DrawPile(CardContainer):
    def __init__(self, playerdeck, playerhand, discardpile):
        super().__init__()
        self.cards = playerdeck.get_cards()
        shuffle(self.cards)
        self._playerhand = playerhand
        self._discardpile = discardpile

    def reshuffle_discard(self):
        cards = self._discardpile.take_cards()
        for card in cards:
            self.cards.append(card)
        shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) < 1:
            self.reshuffle_discard()
        return self.cards.pop(0)

    def draw_cards(self, n):
        for i in range(0, n):
            card = self.draw_card()
            self._playerhand.add_card(card)
