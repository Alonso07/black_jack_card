from src.blackjack.chips import Chips
from src.blackjack.deck import Deck
from src.blackjack.hand import Hand


class GameLogic():
    

    def take_bet(self, chips: Chips):
        while True:
            try:
                chips.bet = int(input("How many chips do you want to bet?"))
            except:
                print("Sorry please provide an integer!")
            else:
                if chips.bet > chips.total:
                    print(f"Sorry you dont have enough chips!. You have: {chips.total}")
                else:
                    break


    def hit(self, deck: Deck, hand: Hand):
        single_card = deck.deal_one()
        hand.add_card(single_card)
        hand.adjust_for_ace()
        

    def ask_hit_or_stand(self, deck: Deck, hand: Hand)-> bool:
        while True:
            x = input("Do you want to hit (h) or stand (s)")
            if x[0].lower() == "h":
                self.hit(deck, hand)
                return True
            elif x[0].lower() == "s":
                print("Player will stand, Dealer's turn")
                return False
            else:
                print("Sorry, I didn't understand that! only 'h' or 's'")


    def show_some_cards(self, player: Hand, dealer: Hand):
        print("\nDealer's Hand: ")
        print("1st card hidden!")
        print(f"{dealer.cards[1]}")

        print("\nPlayer's Hand: ")
        for card in player.cards:
            print(card)


    def show_all_cards(self, player: Hand, dealer: Hand):
        
        print("\nDealer's Hand: ")
        for card in dealer.cards:
            print(card)
        print(f"Value of Dealer's hand is : {dealer.value}")

        print("\nPlayer's Hand: ")
        for card in player.cards:
            print(card)            
        print(f"Value of Player's hand is : {player.value}")  


    def player_busts(self, player: Hand, dealer: Hand, chips: Chips):
        print("Player bust!") 
        chips.lose_bet()


    def player_wins(self, player: Hand, dealer: Hand, chips: Chips): 
        print("Player wins!")         
        chips.win_bet()     


    def dealer_busts(self, player: Hand, dealer: Hand, chips: Chips): 
        print("Dealer bust!")         
        chips.win_bet() 


    def dealer_wins(self, player: Hand, dealer: Hand, chips: Chips): 
        print("Dealer wins!")         
        chips.lose_bet()  


    def push(self, player: Hand, dealer: Hand): 
        print("Game Tie! Push")         
                      

    def main_logic(self):
        playing = True
        #print statement
        print("Welcome to black jack!")
        #create deck and shuffle it
        n_deck = Deck()
        n_deck.shuffle()
        ## deal 2 cards per player
        p_hand = Hand()
        p_hand.add_card(n_deck.deal_one())
        p_hand.add_card(n_deck.deal_one())

        d_hand = Hand()
        d_hand.add_card(n_deck.deal_one())
        d_hand.add_card(n_deck.deal_one())

        chips = Chips()
        self.take_bet(chips)

        self.show_some_cards(p_hand, d_hand)
        while playing:
            playing = self.ask_hit_or_stand(n_deck, p_hand)
            self.show_some_cards(p_hand, d_hand)

            if p_hand.value > 21:
                self.player_busts(p_hand,d_hand,chips)
                break
        if p_hand.value < 21:
            while d_hand.value < 17:
                self.hit(n_deck, d_hand)

        self.show_all_cards(p_hand, d_hand)

        if d_hand.value > 21:
            self.dealer_busts(p_hand, d_hand, chips)
        elif d_hand.value > p_hand.value:
            self.dealer_wins(p_hand, d_hand, chips)  
        elif p_hand.value > 21:
            self.player_busts(p_hand, d_hand, chips)   
        elif d_hand.value < p_hand.value:
            self.player_wins(p_hand, d_hand, chips)                            
        else:
            self.push(p_hand, d_hand)

        print(f"\nPlayer chips are at :{chips.total}")

