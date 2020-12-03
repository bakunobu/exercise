import doctest


# a
def first_last(a: int) -> str:
    """
    >>> first_last(123)
    'last'
    >>> first_last(321)
    'first'
    >>> first_last(121)
    'equal'
    """
    hund = a // 100
    units = a % 10
    if hund > units:
        return('first')
    elif hund < units:
        return('last')
    else:
        return('equal')


# b
def first_second(a: int) -> str:
    """
    >>> first_second(123)
    'second'
    >>> first_second(321)
    'first'
    >>> first_second(221)
    'equal'
    """
    hund = a // 100
    a -= hund  * 100 
    tens = a // 10
    if hund > tens:
        return('first')
    elif hund < tens:
        return('second')
    else:
        return('equal')

# c
def second_last(a: int) -> str:
    """
    >>> second_last(123)
    'last'
    >>> second_last(321)
    'second'
    >>> second_last(122)
    'equal'
    """
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    if tens > units:
        return('second')
    elif tens < units:
        return('last')
    else:
        return('equal')

if __name__ == '__main__':
    doctest.testmod()