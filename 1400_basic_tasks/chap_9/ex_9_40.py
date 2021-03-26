def calc_seq(n:int) -> int:
    if n == 1:
        return(1)
    else:
        return(n ** n + calc_seq(n-1))
    
