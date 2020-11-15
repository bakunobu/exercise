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


def count_rect_param(a:tuple, b:tuple, c:tuple, d:tuple) -> None:
    A = eucl_dist(a, b)
    B = eucl_dist(b, c)
    C = eucl_dist(c, d)
    D = eucl_dist(d, a)
    print('Perimeter: %.3f' % (A+B+C+D))
    S_1 = triangle_area(A, B, C)
    S_2 = triangle_area(A, C, D)
    S = S_1 + S_2
    print('Area: %.3f' % S)
    

