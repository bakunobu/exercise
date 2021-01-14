def calc_factorial(x:int) -> int:
    if x == 0:
        return(1)
    while x > 0:
        return(x * calc_factorial(x-1))
    
    
