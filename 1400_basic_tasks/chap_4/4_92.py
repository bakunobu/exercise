def which_signal(t:int) -> str:
    t %= 7
    if t <= 3:
        return('Green')
    elif 3 < t <= 4:
        return('Yellow')
    else:
        return('Red')