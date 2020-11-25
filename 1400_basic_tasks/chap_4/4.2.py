import math


def my_func(x:float) -> float:
    if x > 0:
        return(math.sin(x) ** 2)
    else:
        return(1 - 2 * math.sin(x) ** 2)
    

