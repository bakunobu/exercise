symbols = ['крыса',
           'бык',
           'тигр',
           'кролик',
           'дракон',
           'змея',
           'лошадь',
           'овца',
           'обезьна',
           'петух',
           'coбака',
           'свинья',]


colors = ['зеленый',
          'красный',
          'желтый',
          'белый',
          'синий',]


def year_of_cycle(y:int) -> tuple:
    base_year = 1984
    while y < base_year:
        base_year -= 60
    remainer = y - base_year
    sym = symbols[remainer % 12]
    col = remainer % 10
    col //= 2
    color = colors[col]
    return(sym, color)


