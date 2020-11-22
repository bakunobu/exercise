import doctest


def num_units(n:int) -> int:
    """
    >>> num_units(7)
    7
    >>> num_units(10)
    0
    >>> num_units(101)
    1
    """
    return(n % 10)

def num_tens(n:int) -> int:
    """
    >>> num_tens(7)
    0
    >>> num_tens(10)
    1
    >>> num_tens(101)
    0
    """
    n //= 10
    return(num_units(n))


if __name__ == "__main__":
    doctest.testmod()