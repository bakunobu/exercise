import doctest


def is_two_digit(x: int) -> bool:
    """
    >>> is_two_digit(9)
    False
    >>> is_two_digit(18)
    True
    >>> is_two_digit(101)
    False
    """
    return(9 < abs(x) < 100)

if __name__ == "__main__":
    doctest.testmod()