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
    n_copy = n
    i = 0
    while n_copy:
        n_copy //= 10
        i += 1
    prev_num = n // 10 ** (i - 1)
    while n > 10:
        n %= 10 ** (i - 1)
        i -= 1
        num = n // 10 ** (i - 1)
        if allow_eq:
            if num > prev_num:
                return(False)
        else:
            if num >= prev_num:
                return(False)
        prev_num = num
    return(True)


if __name__ == '__main__':
    doctest.testmod()