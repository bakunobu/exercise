import random
import time


points = {'6':60,
          '7':70,
          '8':80,
          '9':90,
          '10':100,
          'J':110,
          'Q':120,
          'K':130,
          'A':140,
          'spades':1,
          'clubs':2,
          'diamonds':3,
          'hearts':4}

class Card:
    def __init__(self, rank:str, suit:str) -> None:
        self.rank = rank
        self.suit = suit
        self.points = points[rank] + points[suit]
        
    
    def __repr__(self) -> str:
        return(f'{self.rank} of {self.suit}')
    
    
class Deck:
    def __init__(self, num_cards:int) -> None:
        self.num = num_cards
        if self.num == 32:
            self.ranks = ['6', '7', '8', '9',
                          '10', 'J', 'Q', 'K', 'A']
        else:
            pass
        self.suits = ['diamonds', 'hearts',
                       'spades', 'clubs']
  
    
    def new_deck(self):
        self.deck = [Card(r,s) for r in self.ranks for s in self.suits]
        
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    
    def cast_card(self):
        card = self.deck.pop(0)
        return(card)
        
        
def game(n:int = 3) -> None:
    wins = {1:0,
            2:0}
    playing_deck = Deck(32)
    playing_deck.new_deck()
    playing_deck.shuffle_deck()
    
    for i in range(n):
        if not playing_deck.deck:
            playing_deck.new_deck()
            playing_deck.shuffle_deck()                      
    
        card_1 = playing_deck.cast_card()
        card_2 = playing_deck.cast_card()
            
        print(f'Player 1 has {card_1};')
        print(f'player 2 has {card_2};')
            
        if card_1.points > card_2.points:
            print('Player 1 wins!')
            wins[1] += 1
        else:
            print('Player 2 wins!')
            wins[2] += 1
        time.sleep(0.5)
    
    if wins[1] > wins[2]:
        print('Player 1 wins the game!')
    elif wins[1] < wins[2]:
        print('Player 2 wins the game!')
    else:
        print('It\'s a tie!')
        


game()