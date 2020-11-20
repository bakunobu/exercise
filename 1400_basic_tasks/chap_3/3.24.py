import doctest


def fancy_permut(x) -> tuple:
    """
    >>> fancy_permut(123)
    213
    >>> fancy_permut(743)
    473
    """
    h = x // 100
    d = (x % 100) // 10
    n = x % 10
    return(d * 100 + h * 10 + n)


if __name__ == "__main__":
    doctest.testmod()