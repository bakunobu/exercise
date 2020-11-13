import math


def circle_square(r:float) -> float:
    return(math.pi * r ** 2)


def find_s_ring(r_1:float, r_2:float) -> float:
    s_1 = circle_square(r_1)
    s_2 = circle_square(r_2)
    return(abs(s_1 - s_2))

print(find_s_ring(2, 5))