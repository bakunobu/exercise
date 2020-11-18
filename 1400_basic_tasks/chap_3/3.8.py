import doctest


def find_seat(n: int) -> int:
    '''
    >>> find_seat(1994)
    Out of range
    >>> find_seat(1644)
    1
    >>> find_seat(1660)
    2
    >>> find_seat(1676)
    3
    >>> find_seat(1943)
    20
    
    '''
    if n > 1943 or 1643 < 0:
        print('Out of range')
        return(None)
    else:
        n -= 1643
        if n % 15 == 0:
            return(n // 15)
        else:
            return(1 + n // 15)
        


if __name__ == "__main__":
    doctest.testmod()
