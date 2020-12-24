# a
def which_day(k:int) -> str:
    k %= 7
    if k <= 5:
        return('Working day')
    elif k == 6:
        return('Saturday')
    else:
        return('Sunday')
    
# b
def which_d_day(k:int, d:int) -> str:
    k %= 7
    k += d - 1
    if k > 7:
        k %= 7
    if k <= 5:
        return('Working day')
    elif k == 6:
        return('Saturday')
    else:
        return('Sunday')
    
    