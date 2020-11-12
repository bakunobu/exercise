"""
Программа, определяющую температуру воздуха с учетом влияния ветра
"""
from typing import Optional

def wind_temp(t: float, v: float) -> Optional[float]:
    """
    Evaluates winds influence to temperature
    
    Args:
    =====
    t: float
    temperature
    v: float
    wind speed
    
    Returns:
    ========
    adj_temp: float or None
    an adjusted temperature (non if bad conditions)
    
    """
    if t > 50 or not (3 < v < 120):
        return(None)
    else:
        return(35.74 + 0.6215 * t + (0.425 * t - 35.75) * v ** 0.16)
    

# test
print(wind_temp(51, 20))
print(wind_temp(35, 20))
print(wind_temp(40, 2))



