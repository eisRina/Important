from deck import Deck

class Player:
    def __init__(self,name,deck = None):
        self.name = name
        self.deck = Deck() or deck
    def __str__(self):
        return f'Игрок - {self.name} , Колода {self.deck}'