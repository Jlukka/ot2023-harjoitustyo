from baseclasses.creature import Creature

class Enemy(Creature):
    def __init__(self, health=10):
        super().__init__(health)
