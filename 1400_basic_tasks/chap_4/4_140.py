suits = {1: 'Spades',
         2: 'Clubs',
         3: 'Diamonds',
         4: 'Hearts'}


cards = {2: 'двойка',
         3: 'тройка',
         4: 'четверка',
         5: 'пятерка',
         6: 'шестерка',
         7: 'семерка',
         8: 'восьмерка',
         9: 'девятка',
         10: 'десятка',
         11: 'валет',
         12: 'дама',
         13: 'король',
         17: 'туз',}


def which_suit(m:int) -> str:
    return(suits.get(m))


def which_card(k:int) -> str:
    return(cards.get(k))


def generate_card(m:int, k:int) -> str:
    suit = which_suit(m)
    card = which_card(k)
    return(f'{suit} {card}')


