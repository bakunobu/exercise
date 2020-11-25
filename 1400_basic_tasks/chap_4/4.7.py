import math


def define_k(x:float) -> float:
    if mat.sin(x) < 0:
        return(x ** 2)
    else:
        return(abs(x))
    
def my_func(x:float) -> float:
    k = define_k(x):
    if x > k:
        return(k * x)
    else:
        return(k + x)
        