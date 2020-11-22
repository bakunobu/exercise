import doctest


def num_tens(n:int) -> int:
    """
    >>> num_tens(10)
    1
    >>> num_tens(99)
    9
    >>> num_tens(123)
    2
    """
    n //= 10
    return(n % 10)


def num_hundr(n:int) -> int:
    """
    >>> num_hundr(100)
    1
    >>> num_hundr(1300)
    3
    >>> num_hundr(9037)
    0
    """
    n //= 100
    return(n % 10)


if __name__ == "__main__":
    doctest.testmod()