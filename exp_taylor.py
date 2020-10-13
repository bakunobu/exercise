'''
Составьте фрагмент кода, использующий разложение в ряд тейлора для присвоения переменной total
результата выражения e^x = 1 + x  + {x^2}/2! + {x^3}/3! + ...
'''

import math

def exp_taylor(x: float, n: int) -> int:
    total = 1 + x
    for i in range(2, n+1):
        total += x ** i / math.factorial(i)
    return(total)


def taylor_ser_rec(x: float, n: int) -> float:
    if n == 0:
        return(1)
    while n > 0:
        return(math.pow(x, n) / math.factorial(n) + taylor_ser_rec(x, n-1))


# testing
eps = 10e-6 # epsilon
print(abs(exp_tailor(3, 100) - math.exp(3)) <= eps)


