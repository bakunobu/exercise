"""
Ул учшите решение упражнения 1.2.22, добавив код проверки аргументов командной строки на принадлежность к диапазону
допустимых для фор­мулы температуры воздуха
с учетом влияния ветра и код вывода сообще­ния об ошибке, если они не в диапазоне
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
    an adjusted temperature
    If bad conditions returns None and print a message (respectively)
    
    """
    if t > 50:
        print('emperature is out of range')
        return(None)
    if not (3 < v < 120):
        print('Wind speed is out of range')
        return(None)
    else:
        return(35.74 + 0.6215 * t + (0.425 * t - 35.75) * v ** 0.16)
    