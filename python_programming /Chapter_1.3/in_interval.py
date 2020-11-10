""" 
Составьте фрагмент кода, получающий два аргумента командной стро­ки типа float
и выводящую True, если оба находятся в диапазоне от О.О до 1.О, и False в противном случае.  
"""

def is_in_int(a: float, b: float) -> bool:
    """
    Return the statement if a and b are both belong to (0, 1) interval
    
    Args:
    =====
    a: float
    number one
    
    b: float
    number two
    
    Return:
    =======
    result: bool
    True if the statement is correct, else - False
    
    """
    
    return(0 < a < 1 and 0 < b < 1)