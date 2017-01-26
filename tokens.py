import random

class creature:

    def __init__(self):
        self.ac = random.randint(12, 17)
        self.att = 0
        self.hp = roll(3, 8) + 5
        self.weap = 6
        self.dambns = 3
    
    def attack(self):
        return [roll(1, 20)+self.att, roll(1, self.weap)+self.dambns]

def roll(count, die):
    return sum([random.randint(1, die) for i in range(count)])
