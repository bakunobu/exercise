"""
Составьте программу, вычисляющую и выводящую сумму денег,
выручаемую в результате инвестиции при заданной непрерывно
начисляемой процентной ставке по формуле Pe^{rt}, где
P - размер вклада
t - период (в годах)
r - процентная ставка
"""


import math

def comp_interest(p: float, t:int, r:float) -> float:
    """
    Calculates an continuous interest for given params
    
    Args:
    p: float
    Principal
    t: int
    Period (in years)
    r: float
    interest rate (annual)
    
    Returns:
    total: float
    an amount of money returned
    """
    return(p * math.exp(r * t))

comp_interest(1000, 1, 0.05)