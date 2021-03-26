def calc_seq(n:int, m:int) -> int:
    if m == 1:
        return(1)
    else:
        return(m ** n + calc_seq(n, m-1))
    
