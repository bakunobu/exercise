"""
Программа, получающая широту и долготу точки и выводящая ее проекцию
"""

import math

def gd(x:float) -> float:
    """
    Args:
    =====
    x: float
    coordinate
    
    Return:
    =======
    gd: float
    modified coordinate
    """
    return(2 * math.atan(math.exp(x) - (math.pi / 2)))

def merc_poj(lambda_0:float, x: float, y: float) -> tuple:
    """
    Args:
    =====
    lambda_0: float
    longitude in a central point of a map
    x: float
    x coordinate
    y: float
    y coordinate
    
    Return:
    result: tuple
    lambda_real - modified x coordinate
    theta - modified y coordinate    
    """
    lambda_real = x + lambda_0
    theta = math.atan(math.tan(gd(y)))
    return(lambda_real, theta)