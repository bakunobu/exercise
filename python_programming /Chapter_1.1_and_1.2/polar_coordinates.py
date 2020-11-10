"""
Составьте программу, осуществляющую преобразование координат из Декартовых в полярные.
"""

import math

def polar_coord_conv(x: float, y:float) -> tuple:
    """
    Transforms Carthesian coordinates to polar coordinates
    
    Args:
    =====
    x: float
    the x coordinate
    y: float
    the y coordinate
    
    Returns:
    ========
    r, t: tuple
    polar coodinates
    x->r
    y->t
    
    """
    r = (x ** 2 + y ** 2) ** 0.5
    t = math.atan2(x, y)
    return(r, t)


# test
print(polar_coord_conv(1, 2))