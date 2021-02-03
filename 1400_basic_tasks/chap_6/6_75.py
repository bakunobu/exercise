import numpy as np


# a
def my_func_a(x:float) -> float:
    return(x ** 4 + 2 * x ** 3 - x - 1)


# b
def my_func_b(x:float) -> float:
    return(x ** 3 - 0.2 * x ** 2 - 0.2 * x - 1.2)


def bisec(my_func, a:float, b:float, eps:float=0.001) -> float:
    if my_func(a) == 0:
        return(a)
    if my_func(b) == 0:
        return(b)
    while True:
        if (b - a) <= eps:
            break
        delta = (b - a) / 2
        x_m = a + delta
        if np.sign(my_func(a)) != np.sign(my_func(x_m)):
            b = x_m
        else:
            a = x_m
        
    return(x_m)

print(bisec(my_func_a, 0, 1))
print(bisec(my_func_b, 1, 1.5))
            
