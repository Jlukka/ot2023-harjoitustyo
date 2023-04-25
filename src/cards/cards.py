from baseclasses.card import Card


class Slash(Card):
    def __init__(self):
        super().__init__("slash", 1, [("damage", 1)])


class Defend(Card):
    def __init__(self):
        super().__init__("defend", 1, [("block", 1)])


class Test(Card):
    def __init__(self):
        super().__init__("test", 1, [("draw", 1), ("discard", 1)])
