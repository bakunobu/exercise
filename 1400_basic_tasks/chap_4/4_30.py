import doctest


def num_palindrome(a: int) -> bool:
    """
    >>> num_palindrome(121)
    True
    >>> num_palindrome(131)
    True
    >>> num_palindrome(321)
    False
    """
    hund = a // 100
    units = a % 10
    return(hund == units)


if __name__ == '__main__':
    doctest.testmod()