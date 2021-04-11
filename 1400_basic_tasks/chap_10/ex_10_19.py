import random

ranks = ['6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']

suits = ['diamonds',
         'hearts',
         'spades',
         'clubs']

def show_card() -> None:
    r = random.sample(ranks, 1)
    s = random.sample(suits, 1)
    print(f'{r[0]} of {s[0]}')
    
    
show_card()