def calc_series(n:int) -> int:
    total = 0
    for x in range(1, n+1):
        total += (x * (x + 1))
    return(total)