import doctest

def calc_dig_sum(x:int) -> int:
    """
    >>> calc_dig_sum(111_111_111)
    9
    >>> calc_dig_sum(111_111_112)
    10
    """
    total = 0
    for i in range(9):
        total += x % 10
        x //= 10
    return(total)


if __name__ == '__main__':
    doctest.testmod()