import random

class creature:

    def __init__(self):

        self.level = 1
        self.HPDice = 8
        
        self.AC = 10
        
        self.STR = 0
        self.CHA = 0
        self.DEX = 0
        self.INT = 0
        self.CON = 0
        self.WIS = 0

        self.weapon = [6]

        self.HP = self.HPDice + self.CON*self.level + roll(self.level-1, self.HPDice)
    
    def attack(self):
        return [roll(1, 20)+self.STR, roll(1, self.weap)+self.dambns]

def roll(count, die):
    return sum([random.randint(1, die) for i in range(count)])
