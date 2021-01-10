def calc_sum(x:int) -> float:
    total = 1
    for x in range(1, 11):
        el = ((-1) ** x) * ((x+1) / (x+2)) * x
        total += el
    return(total)
