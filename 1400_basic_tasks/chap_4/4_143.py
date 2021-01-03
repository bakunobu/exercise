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


# a
def prev_day(m:int, n:int) -> tuple:
    if n == 1:
        prev_m -= 1
        d = ord_year.get(prev_m)
        return(prev_m, d)
    else:
        return(m, n-1)

    
# b
def next_day(m:int, n:int) -> tuple:
    if n >= 27:
        lim = ord_year.get(m)
        if m == lim:
            return(m+1, 1)
    else:
        return(m, n + 1)