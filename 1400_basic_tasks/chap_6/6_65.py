import doctest


def eucl_gcd(a:int, b:int) -> int:
    """
    >>> eucl_gcd(12, 18)
    6
    >>> eucl_gcd(1071, 462)
    21
    >>> eucl_gcd(9, 11)
    1
    """
    while a > 0 and b > 0:
        a, b = min(a, b), max(a, b) % min(a, b)
    return(a)


if __name__ == '__main__':
    doctest.testmod()