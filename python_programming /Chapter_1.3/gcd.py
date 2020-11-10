"""
Программа, которая находит наибольший общей делитель на основе алгоритма Евклида и рекурсии
"""


def gcd(a: int, b: int) -> int:
    if a == b:
        return(b)
    else:
        return(gcd(min(a, b), abs(a - b)))