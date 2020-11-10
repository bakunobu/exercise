def is_triangle(a: float, b: float, c: float) -> bool:
    """
    Checks is a given configuration of trinagle possible
    
    Args:
    =====
    a: float
    side a
    b: float
    side b
    c:float
    cide c
    
    Return:
    =======
    is possible: bool
    True if it is else False
    """
    
    triangle = a + b > c
    triangle = triangle and a + c > b
    triangle = triangle and b + c > a
    return (triangle)

is_triangle(sys.argv[1], sys.argv[2], sys.argv[3])