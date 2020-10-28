"""
Составьте программу, пре­образующую значения RGB в СМYК.
"""

def rgb_to_cmyk(r: int, g: int, b: int) -> tuple:
    """
    Converts RGB to SMYK color notation
    
    Args:
    =====
    r: int
    red
    g: int
    green
    b: int
    black
    
    Return:
    =======
    result: tuple
    returns values for C, M, Y, K
    """
    w = max(r / 255, g / 255, b / 255)
    c = (w - (r / 255)) / w
    m = (w - (g / 255)) / w
    y = (w - (b / 255)) / w
    k = 1 - w
    return(c, m, y, k)

rgb_to_cmyk(255, 255, 0)