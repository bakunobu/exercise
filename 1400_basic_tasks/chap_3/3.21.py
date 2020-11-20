import doctest


def num_permut(x) -> tuple:
    """
    >>> num_permut(123)
    321
    >>> num_permut(743)
    347
    """
    h = x // 100
    d = (x % 100) // 10
    n = x % 10
    return(n * 100 + d * 10 + h)


if __name__ == "__main__":
    doctest.testmod()