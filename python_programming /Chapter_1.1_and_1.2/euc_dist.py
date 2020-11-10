"""
Предположим, что x и y имеют тип float и представляют координаты (x, y) точки на Декартовой плоскости.
Составьте выражениые для вычисления расстояния от этой точки до исходной
"""

import math


def eucl_dist(p:tuple, q:tuple=(0,0)) -> float:
    """
    The equasion for Euclidian distance
    """
    return(math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2))


# test
print(eucl_dist((1, 1,)))