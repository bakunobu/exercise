import doctest

def is_all_eq(a: int) -> bool:
    """
    >>> is_all_eq(111)
    True
    >>> is_all_eq(132)
    False
    >>> is_all_eq(999)
    True
    """
    a = abs(a)
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    return(hund == tens == units)


def is_some_eq(a: int) -> bool:
    """
    >>> is_some_eq(123)
    False
    >>> is_some_eq(122)
    True
    >>> is_some_eq(333)
    True
    """
    a = abs(a)
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    my_set = set((hund, tens, units)) 
    return(len(my_set) < 3)


if __name__ == '__main__':
    doctest.testmod()