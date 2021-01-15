def calc_power(a:float, n:int) -> float:
    tot = 1
    for i in range(n):
        tot *= i
    return(tot)