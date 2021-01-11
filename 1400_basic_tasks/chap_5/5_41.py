def calc_prod(x:int, n:int):
    total = 1
    for x in range(n):
        total *= x % 10
        x = x // 10
    return(total)