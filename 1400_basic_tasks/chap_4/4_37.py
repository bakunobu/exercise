import doctest

def is_divisor(a:int, b: int) -> bool:
    return(not a % b)

def a_divisor_b(a: int, b:int) -> tuple:
    """
    >>> a_divisor_b(1, 2)
    (False, True)
    >>> a_divisor_b(3, 5)
    (False, False)
    >>> a_divisor_b(2, 1)
    (True, False)
    """
    a_div_b = is_divisor(a, b)
    b_div_a = is_divisor(b, a)
    return(a_div_b, b_div_a)


if __name__ == '__main__':
    doctest.testmod()