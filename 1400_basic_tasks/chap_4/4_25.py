import doctest


def next_even(a: int) -> int:
    """
    >>> next_even(2)
    4
    >>> next_even(3)
    4
    """
    return(a + 2 - a % 2)

if __name__ == '__main__':
    doctest.testmod()