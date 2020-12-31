suits = {1: 'Spades',
         2: 'Clubs',
         3: 'Diamonds',
         4: 'Hearts'}

def which_suit(i:int) -> str:
    return(suits.get(i))