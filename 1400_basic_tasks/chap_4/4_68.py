import doctest


def is_loop(y:int) -> bool:
    '''
    >>> is_loop(1943)
    False
    >>> is_loop(2000)
    True
    >>> is_loop(1986)
    False
    >>> is_loop(1800)
    False
    >>> is_loop(2004)
    True
    '''
    res = y % 4 == 0
    res = res and (y % 400 == 0 or y % 100 != 0)
    return(res)



if __name__ == "__main__":
    doctest.testmod()
    