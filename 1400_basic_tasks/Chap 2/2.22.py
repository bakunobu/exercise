import math


def mean(a:float, b:float) -> float:
    return((abs(a) + abs(b) / 2))


def mean_geom(a:float, b:float) -> float:
    expr = abs(a) ** 2 + abs(b) ** 2
    return(math.sqrt(expr))