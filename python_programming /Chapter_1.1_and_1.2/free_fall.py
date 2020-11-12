"""
Составьте программу, получающую в агрументах командной строки три значения:
x_0, v_0, t типа float и выводящую результат вычиселния выражения
x_0 + v_0*t - Gt^2 / 2
"""

import sys
import scipy.constants as const

def count_speed(x: float, v: float, t:float) -> float:
    """
    Calculates free fall motion of a body
    Args:
    =====
    x: float
    starting position
    v: float
    starting speed
    t: float
    time step
    
    Return:
    =======
    distance: float
    a difference between x_0 and x_1 positions of a body with respect to time (in meters)
    """
    return(x + v * t - (const.g * t ** 2) / 2)

print(count_speed(sys.argv[1], sys.argv[2], sys.argv[3]))