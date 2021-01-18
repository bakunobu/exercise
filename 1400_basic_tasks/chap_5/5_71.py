import math

def strange_sum(n:int=50) -> float:
    if n == 50:
        return(math.sqrt(50))
    else:
        return(math.sqrt(n + strange_sum(n+1)))
    
    
print(strange_sum())