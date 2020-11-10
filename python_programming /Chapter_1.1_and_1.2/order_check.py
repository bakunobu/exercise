"""
Составьте программу, получающую в аргументах ко­мандной строки три значения,
х, у и z типа float, а выводящую True, если значения расположены в порядке
возрастания или убывания (х < у < z или х >у> z), и False в  противном случае.
"""
 
def in_a_raw(x:float, y:float, z:float) -> bool:
    """
    An order checker
    
    Args:
    =====
    x: float
    the first element of a series
    y: float
    the second element of a series
    z: float
    the third element of a series
    
    Return:
    =======
    result: bool
    True if a < b < c or a > b > c
    """
    return((x < y < z) or (x > y > z))