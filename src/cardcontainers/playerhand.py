from baseclasses.cardcontainer import CardContainer


class PlayerHand(CardContainer):
    def __init__(self):
        super().__init__(10)

    def pop_card(self, index):
        return self.cards.pop(index)
