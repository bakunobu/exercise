def calc_mercator_series(n:int) -> float:
    total = 1
    x = 1
    for a in range(2, n+1):
        sign = -x / x
        x = sign * (1 / n)
        total += x
    return(total)