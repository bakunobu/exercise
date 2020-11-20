import doctest


def fancy_permut(x) -> tuple:
    """
    >>> fancy_permut(123)
    312
    >>> fancy_permut(743)
    374
    """
    h = x // 100
    d = (x % 100) // 10
    n = x % 10
    return(n * 100 + h * 10 + d)


if __name__ == "__main__":
    doctest.testmod()