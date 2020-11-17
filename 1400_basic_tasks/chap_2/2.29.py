import math


def eucl_dist(a:tuple, b:tuple) -> float:
    d_1 = (a[0] - b[0]) ** 2
    d_2 = (a[1] - b[1]) ** 2
    d = math.sqrt(d_1 + d_2)
    return(d)


def triangle_area(a:float, b:float, c:float) -> float:
    p = a + b + c
    P = p * (p - a) * (p - b) * (p - c)
    A = math.sqrt(P)


def count_triangle_param(a:tuple, b:tuple, c:tuple) -> None:
    A = eucl_dist(a, b)
    B = eucl_dist(a, c)
    C = eucl_dist(b, c)
    print('Perimeter: %.3f' % (A+B+C))
    S = triangle_area(A, B, C)
    print('Area: %.3f' % S)