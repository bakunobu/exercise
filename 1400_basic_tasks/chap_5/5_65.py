def calc_power_alt(n:int) -> int:
    if n == 1:
        return(1)
    else:
        return((2 * n - 1) + calc_power_alt(n-1))
    
