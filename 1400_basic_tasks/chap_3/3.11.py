import doctest


def which_month(n:int) -> int:
    """
    >>> which_month(1)
    2
    >>> which_month(2)
    3
    >>> which_month(13)
    2
    """
    n %= 12
    return(n+1)


if __name__ == "__main__":
    doctest.testmod()