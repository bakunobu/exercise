import doctest

def is_divisor(a:int, n:int) -> bool:
    """
    >>> is_divisor(1,3)
    True
    >>> is_divisor(3, 1)
    False
    """
    return(not n%a)


if __name__ == '__main':
    doctest.testmod()