import doctest

# a
def ends_with_even(a:int) -> bool:
    """
    >>> ends_with_even(23)
    False
    >>> ends_with_even(18)
    True
    """
    x = a % 10
    return(not x % 2)

# b
def ends_with_odd(a:int) -> bool:
    """
    >>> ends_with_odd(23)
    True
    >>> ends_with_odd(18)
    False
    """
    x = a % 10
    return(bool(x % 2))


if __name__ == '__main__':
    doctest.testmod()