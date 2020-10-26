"""
Составьте программу, получающую в аргументах командной строки два целых числа, 
m и d, и выводящую True, если день d месяца m приходится на на 20 марта или 20 июня
и False в противном случае
"""

def stupid_date_checker(m: int, d: int) -> bool:
    """
    Checks wether date is 3/20 or 6/20
    Args:
    =====
    m: int
    month
    d: int
    day
    
    Returns:
    result: True
    True if the date is 3/20 or 6/20   
    """
    return((m == 3 or m == 6) and d == 20)

stupid_date_checker(sys.argv[1], sys.argv[2])