import doctest


def dec_nums(x:int) -> tuple:
    """
    >>> dec_nums(9)
    (0, 9)
    >>> dec_nums(19)
    (1, 9)
    >>> dec_nums(23)
    (2, 3)
    """
    return(x // 10, x % 10)
    


if __name__ == "__main__":
    doctest.testmod()