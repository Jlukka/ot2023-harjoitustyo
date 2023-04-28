from baseclasses.card import Card
from action import Action


class Slash(Card):
    def __init__(self):
        super().__init__("slash", 1, [Action("damage", 1, "enemy")])


class Defend(Card):
    def __init__(self):
        super().__init__("defend", 1, [Action("block", 1, "player")])


class DrawDiscard(Card):
    def __init__(self):
        super().__init__("Draw&Discard", 1, [Action("discard", 1, ""), Action("draw", 1, "")])
