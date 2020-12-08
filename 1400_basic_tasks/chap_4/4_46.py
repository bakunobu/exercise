import math

def my_func(x:float) -> float:
    if 0.2 <= x <= 0.9:
        return(math.sin(x))
    else:
        return(1)