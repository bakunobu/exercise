"""
Один способ создания случайного числа в со­ответствии с распределением Гаусса подразумевает использование фор­мулы Бокса-Мюллера.
Составьте программу, выводящую значение согласно стандарт­ному Гауссову распределению. 
"""


import math
import random

import random


def box_muller_trans(v:float, u: float) -> float:
    """
    A Box-Muller transformation for random number generation
    
    Args:
    =====
    v: float
    a random number
    u: float
    a random number
    
    Return:
    ========
    w: float
    a result of Box-Muller transformation
    """
    expr_1 = math.sin(2 * math.pi * v)
    expr_2 = (-2 * math.log(u)) ** 0.5
    return(expr_1 * expr_2)

def gaussian_random_digits() -> float:
    """
    Generates a Normal Distributed random number using
    Box-Muller transformation
    
    Args:
    None
    
    Return:
    w: float
    a random number
    """
    v = random.random()
    u = random.random()
    w = box_muller_trans(v, u)
    return(w)

# test
gaussian_random_digits()