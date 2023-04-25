from baseclasses.enemy import Enemy


class FirstEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.attacks = 0

    def attack(self):
        return ("damage", self.attacks+1)
        self.attacks += 1
