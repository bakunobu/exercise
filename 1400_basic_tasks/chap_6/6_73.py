import doctest


def is_geom_prog(m:float, g:float, z:float) -> bool:
    '''
    >>> is_geom_prog(10.0, 2.0, 5.0)
    True
    >>> is_geom_prog(11.0, 2.0, 5.0)
    False
    >>> is_geom_prog(10.0, 2.5, -2.0)
    True
    >>> is_geom_prog(0.5, 8, 0.5)
    True    
    '''
    diff = abs(m - g)
    while diff > abs(m - g):
        g *= z
        if m == g:
            return(True)
        diff = abs(m - g)
    return(False)