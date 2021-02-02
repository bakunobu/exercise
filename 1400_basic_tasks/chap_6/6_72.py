import doctest


def is_ar_prog_el(n:int, f:int, s:int) -> bool:
    """
    >>> is_ar_prog_el(9, 1, 1)
    True
    >>> is_ar_prog_el(10, 0, 5)
    True
    >>> is_ar_prog_el(-10, 0, -5)
    True
    >>> is_ar_prog_el(9, 1, 3)
    False
    """
    while abs(n) > abs(f):
        f += s
        if n == f:
            return(True)
    return(False)




if __name__ == '__main__':
    doctest.testmod()