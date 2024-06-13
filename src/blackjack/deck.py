from src.blackjack.card import Card
from src.blackjack.constants import values
from src.blackjack.constants import suits
from src.blackjack.constants import ranks
import random


class Deck():
  
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self) -> Card:
        return self.all_cards.pop()
    
    def __str__(self)-> str:
        deck_info = ''
        for card in self.all_cards:
            deck_info = '\n' + card.__str__()
        return "The Deck has : " + deck_info 
    