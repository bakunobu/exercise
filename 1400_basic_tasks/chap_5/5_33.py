def count_partial() -> float:
    total = 0
    for x in range(2, 11):
        total += x / (x + 1)
    return(total)