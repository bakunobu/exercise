import doctest


def num_permut(x:int) -> int:
    """
    >>> num_permut(23)
    32
    >>> num_permut(45)
    54
    >>> num_permut(9)
    90
    """
    return((x % 10) * 10 + (x // 10))

if __name__ == "__main__":
    doctest.testmod()