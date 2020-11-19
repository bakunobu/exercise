import doctest


def which_floor(n:int) -> int:
    """
    >>> which_floor(1)
    1
    >>> which_floor(5)
    2
    >>> which_floor(8)
    2
    >>> which_floor(20)
    5
    """
    return(n // 4 + min(1, n % 4))


def which_num(n:int) -> int:
    """
    >>> which_num(1)
    1
    >>> which_num(20)
    4
    >>> which_num(2)
    2
    >>> which_num(5)
    1
    """
    floor = which_floor(n)
    return(n - (floor - 1) * 4)


if __name__ == "__main__":
    doctest.testmod()