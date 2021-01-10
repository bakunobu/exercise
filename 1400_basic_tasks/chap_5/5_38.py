def calc_sum(x:int) -> float:
    total = 0
    for i in range(1, 12, 2):
        total += x ** i / i
    return(total)


print(calc_sum(2))