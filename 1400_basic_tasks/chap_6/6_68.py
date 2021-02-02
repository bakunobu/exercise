import doctest


def eucl_gcd(a:int, b:int) -> int:
    while a > 0 and b > 0:
        a, b = min(a, b), max(a, b) % min(a, b)
    return(a)


def decr_part(a:int, b:int) -> tuple:
    """
    >>> decr_part(2, 4)
    (1, 2)
    >>> decr_part(3, 7)
    (3, 7)
    """
    denom = eucl_gcd(a, b)
    return(a // denom, b // denom)


if __name__ == "__main__":
    doctest.testmod()