 


def has_solution(a:float,
                 b:float,
                 c:float) -> str:
    
    D = b ** 2 - 4 * a * c
    
    if D < 0:
        return('No')
    else:
        return('Yes')