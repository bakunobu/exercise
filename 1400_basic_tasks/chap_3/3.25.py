import doctest


def fancy_permut(x) -> tuple:
    """
    >>> fancy_permut(123)
    132
    >>> fancy_permut(743)
    734
    """
    h = x // 100
    d = (x % 100) // 10
    n = x % 10
    return(h * 100 + n * 10 + d)


if __name__ == "__main__":
    doctest.testmod()