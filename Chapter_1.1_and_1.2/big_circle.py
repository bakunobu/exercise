"""
Составьте программу, получающую в командной строке четыре аргумента, х1,  у1, х2 и у2 типа float
(широта и долгота в градусах двух точек на глобусе), и  выводящую длину большой окруж­ности между ними. 
"""

import math
def big_circle(x_1: float, y_1: float, x_2: float, y_2: float) -> float:
    """
    calculates the distance (curve) betwwen the two points on a surface of a sphere
    
    Args:
    =====
    x_1: float
    point 1 x coordinate
    y_1: float
    point 1 y coordinate
    x_2: float
    point 2 x coordinate
    y_2: float
    point 2 y coordinate
    
    Return:
    =======
    d: float
    distance (cuve) between two points
    """
    X_1 = math.radians(x_1)
    Y_1 = math.radians(y_1)
    X_2 = math.radians(x_2)
    Y_2 = math.radians(y_2)
    d = 60 * math.acos(math.sin(X_1) * math.sin(X_2) + math.cos(X_1) * math.cos(X_2) * math.cos(Y_1 - Y_2))
    return(d)


# test
big_circle(48.87, -2.33, 37.8, 122.4)