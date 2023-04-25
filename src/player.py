class Player:
    def __init__(self, health, starter_deck):
        self.max_health = health
        self.health = health
        self.dead = False
        self._deck = starter_deck

    def take_damage(self, amount):
        if self.health - amount <= 0:
            self.die()
        else:
            self.health -= amount

    def heal_damage(self, amount):
        if self.health + amount >= self.max_health:
            self.health = self.max_health
        else:
            self.health += amount

    def get_deck(self):
        return self._deck

    def die(self):
        self.dead = True
