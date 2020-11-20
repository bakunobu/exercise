import doctest


def num_decomposition(x) -> tuple:
    """
    >>> num_decomposition(123)
    (3, 2, 6, 6)
    >>> num_decomposition(743)
    (3, 4, 14, 84)
    """
    h = x // 100
    d = (x % 100) // 10
    n = x % 10
    return(n, d, h + d + n, h * d * n)


if __name__ == "__main__":
    doctest.testmod()