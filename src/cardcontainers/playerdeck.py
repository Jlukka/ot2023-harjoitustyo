from baseclasses.cardcontainer import CardContainer


class PlayerDeck(CardContainer):
    def __init__(self):
        super().__init__(50)
