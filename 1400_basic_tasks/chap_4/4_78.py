def which_field(a:int, b:int) -> str:
    if a % 2 == 0:
        if b % 2 == 0:
            return('black')
        else:
            return('white')
    else:
        if b % 2 == 0:
            return('white')
        else:
            return('black ')