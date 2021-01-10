def count_sum(n:int) -> float:
    total = 0
    for x in range(1, n+1):
        total += 1 / x
    return(total)