import doctest

def m_sum_dig(n:int, m:int) -> int:
    """
    >>> m_sum_dig(1234, 5)
    10
    >>> m_sum_dig(1234, 4)
    10
    >>> m_sum_dig(1234, 3)
    9
    """
    i = 1
    num_sum = 0
    while True:
        if n:
            num_sum += n % 10
            n //= 10
        else:
            break
        if i == m:
            break
        i += 1
    return(num_sum)


if __name__ == '__main__':
    doctest.testmod()