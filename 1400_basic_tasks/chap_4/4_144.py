ord_year = {1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31}

leap_year = {1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31}


def how_many_days(x:int, leap:bool=False) -> int:
    if leap:
        return(leap_year.get(x))
    else:
        return(ord_year.get(x))
    

# a
def prev_day(y:int, m:int, d:int, leap:bool=False) -> tuple:
    if m == 1 and d == 1:
        return(y-1, 12, 31)
    elif d == 1:
        d = how_many_days(m-1, leap)
        return(y, m-1, d)
    else:
        return(y, m, d-1)
    

# b
def next_day(y:int, m:int, d:int, leap:bool=False) -> tuple:
    if m == 12 and d == 31:
        return(y+1, 1, 1)
    lim = how_many_days(m, leap)
    if d == lim:
        return(y, m+1, 1)
    else:
        return(y, m, d + 1)