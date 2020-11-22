import doctest


def num_hundr(n:int) -> int:
    """
    >>> num_hundr(100)
    1
    >>> num_hundr(1300)
    3
    >>> num_hundr(9037)
    0
    """
    n //= 100
    return(n % 10)


def num_ths(n:int) -> int:
    """
    >>> num_ths(1000)
    1
    >>> num_ths(13000)
    3
    >>> num_ths(90370)
    0
    """
    n //= 1000
    return(n % 10)


if __name__ == "__main__":
    doctest.testmod()