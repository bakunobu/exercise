import random

SUITS = ['Clubs', 'Diamonds', "Hearts", 'Spades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Queen', 'King']


DECK = ['{} of {}'.format(rank, suit) for suit in SUITS for rank in RANKS]

def cast_five(my_deck: list) -> None:
    print(* random.sample(my_deck, 5), sep='; ')


def repeat_cast(n:int, my_deck:list) -> None:
    for _ in range(n):
        cast_five(my_deck)
        print()


repeat_cast(5, DECK)
    