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


def cards(k:int) -> str:
    return(cards.get(k))

