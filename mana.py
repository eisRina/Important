from card import Card
from Player import Player

class Land(Card):
    def __init__(self, mana_produce):
        super().__init__()
        self.mana_produce = mana_produce 
    def tap(self,player):
        if not self.isTaped:
            super().tap()
            player.mana_pool.append(self.mana_produce)
    
    def manaMANA(self,player,card):
        pool_mana = player.mana_pool[:]
        cost_mana = card.mana_cost()
        for a in cost_mana():
            if a.isdigit():
                
                
                
        
        
        