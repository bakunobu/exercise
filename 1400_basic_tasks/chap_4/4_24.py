import doctest


# a
def is_even(a:int) -> bool:
    """
    >>> is_even(2)
    True
    >>> is_even(5)
    False
    """
    return(not a % 2)

# b
def ends_with_seven(a:int) -> bool:
    """
    >>> ends_wiht_seven(23)
    False
    >>> ends_wiht_seven(-27)
    True
    """
    return(not a % 10 == 7 )

if __name__ == '__main__':
    doctest.testmod()