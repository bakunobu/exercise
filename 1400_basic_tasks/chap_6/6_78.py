import doctest


def is_sorted(n:int) -> bool:
    '''
    >>> is_sorted(5431)
    True
    >>> is_sorted(5441)
    True
    >>> is_sorted(1234)
    False
    '''

    prev_num = n % 10 
    while n > 10:
        n //= 10
        num = n % 10
        if num < prev_num:
            return(False)
        else:
            prev_num = num
    return(True)

if __name__ == '__main__':
    doctest.testmod()