class Card:
    def __init__(self, title, cost, actions=None):
        self.title = title
        self.cost = cost
        self.actions = actions or []
