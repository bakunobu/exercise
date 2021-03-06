import doctest


def is_sorted(n:int, allow_eq=True) -> bool:
    '''
    >>> is_sorted(5321)
    True
    >>> is_sorted(44321)
    True
    >>> is_sorted(1234)
    False
    '''
    prev_num = n % 10 
    while n > 10:
        n //= 10
        num = n % 10
        if allow_eq:
            if num < prev_num:
                return(False)
        else:
            if num <= prev_num:
                return(False)
        prev_num = num
    return(True)


if __name__ == '__main__':
    doctest.testmod()