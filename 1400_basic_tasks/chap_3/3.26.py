import doctest


def complete_permut(x) -> tuple:
    """
    >>> complete_permut(123)
    (123, 132, 213, 231, 312, 321)
    >>> complete_permut(743)
    (743, 734, 473, 437, 374, 347)
    """
    h = x // 100
    d = (x % 100) // 10
    n = x % 10
    return(h * 100 + d * 10 + n,
           h * 100 + n * 10 + d,
           d * 100 + h * 10 + n,
           d * 100 + n * 10 + h,
           n * 100 + h * 10 + d,
           n * 100 + d * 10 + h)


if __name__ == "__main__":
    doctest.testmod()