import math


def define_k(x: float) -> float:
    if math.sin(x) < 0:
        return(abs(x))
    else:
        return(x ** 2)
    

def define_func(x:) -> float:
    k = define_k(x)
    if x < k:
        return(abs(x))
    else:
        return(k * x)