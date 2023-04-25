class CardContainer:
    def __init__(self, cardlimit=-1, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards
        self._cardlimit = cardlimit

    def get_cards(self):
        return self.cards.copy()

    def add_card(self, card):
        if self._cardlimit != -1:
            if len(self.cards) >= self._cardlimit:
                return
            else:
                self.cards.append(card)
        return True

    def add_cards(self, cards):
        for card in cards:
            if not self.add_card(card):
                return False
        return True

    def delete_card(self, cardindex):
        if cardindex < 0 or cardindex >= len(self.cards):
            return False
        self.cards.remove(cardindex)
        return True
