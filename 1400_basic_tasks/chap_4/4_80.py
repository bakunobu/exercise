import math


def check_sides(a:float, b:float, c:float) -> bool:
    return(a + b > c)


def check_triangle(a:float, b:float, c:float) -> bool:
    for x in [(a, b, c), (b, c, a), (a, c, b)]:
        if not check_sides(* x):
            return(False)
    return(True)


def check_angle(a:float, b:float, c:float) -> bool:
    a, b, c = sorted([a, b, c])
    return(check_triangle(a, b, c) and (a ** 2 + b ** 2 == c ** 2))


