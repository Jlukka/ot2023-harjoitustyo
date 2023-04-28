class Creature:
    def __init__(self, health):
        self.maxhealth = health
        self.health = health
        self.dead = False

    def modify_health(self, amount):
        self.health = max(min(amount, self.maxhealth),0)

    def die(self):
        self.dead = True