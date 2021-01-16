def calc_power_alt(n:int) -> int:
    if n == 1:
        return(1)
    else:
        return((2 * n - 1) + calc_power_alt(n-1))


total = 0
for x in range(1, 13):
    total += calc_power_alt(x)
    
    
