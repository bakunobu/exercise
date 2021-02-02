import doctest


def eucl_gcd(a:int, b:int) -> int:
    while a > 0 and b > 0:
        a, b = min(a, b), max(a, b) % min(a, b)
    return(a)


def lcm(a:int, b:int) -> int:
    """
    >>> lcm(16, 20)
    80
    """
    return((a * b) // eucl_gcd(a, b))


if __name__ == '__main__':
    doctest.testmod()