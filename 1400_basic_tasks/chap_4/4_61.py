import math
from typing import Union

def solve_quad_eq(a:float, b:float, c:float) -> Union[tuple, None]:
    D = b ** 2 - 4 * a * c
    if D < 0:
        return(None)
    elif D == 0:
        return(tuple(-b / (2 * a)))
    else:
        x_1 = (-b + math.sqrt(D)) / (2 * a)
        x_2 = (-b - math.sqrt(D)) / (2 * a)
        return(x_1, x_2)
    

