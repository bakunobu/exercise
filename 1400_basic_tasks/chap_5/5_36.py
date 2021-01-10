def count_long_way() -> float:
    total = 1
    for i in range(1, 9):
        num = 1
        for j in range(i):
            num *= 1 / 3
        total += num
    return(total)