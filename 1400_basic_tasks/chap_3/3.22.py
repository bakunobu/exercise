import doctest


def fancy_permut(x) -> tuple:
    """
    >>> fancy_permut(123)
    231
    >>> fancy_permut(743)
    437
    """
    h = x // 100
    d = (x % 100) // 10
    n = x % 10
    return(d * 100 + n * 10 + h)


if __name__ == "__main__":
    doctest.testmod()