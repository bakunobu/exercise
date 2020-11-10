"""
Составьте прогрмму, получающую в аргументах командной строки переменну t
тапа float и выводящую результат вычисления выражения sin(2t)+sin(3t)
"""

import math
import sys

def calc_sin_expr(x: float) -> float:
    """
    Accepts t and returns a result of the expr sin(2t)+sin(3t)
    """
    return(math.sin(x * 2) + math.sin(x * 3))

calc_sin_expr(sys.argv[1])
