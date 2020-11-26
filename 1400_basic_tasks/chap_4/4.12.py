import math


def square_area(a: float) -> float:
    return(a ** 2)


def circle_area(r: float) -> float:
    return(math.pi * r ** 2)


def compare_areas(a:float, r:float) -> str:
    sq_a = square_area(a)
    cir_a = circle_area(r)
    if sq_a > cir_a:
        return('Square')
    else:
        return('Circle')