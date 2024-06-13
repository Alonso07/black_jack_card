from src.blackjack.constants import values

class Card():
    suits = ""
    ranks = ""
    value = 0
    
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.lower()]
        
    def __str__(self):
        return self.rank + " of " + self.suit