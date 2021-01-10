def count_series(n:int) -> int:
    total = 0
    for x in range(1, n + 1):
        total += x ** 2
    return(total)