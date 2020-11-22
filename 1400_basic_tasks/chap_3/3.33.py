import doctest


def find_num(n:int) -> int:
    """
    >>> find_num(237)
    372
    """
    unit = 237 // 100
    n -= unit * 100
    n *= 10
    n += unit
    return(n)


if __name__ == "__main__":
    doctest.testmod()