import doctest


def reverse_num(n:int) -> int:
    """
    >>> reverse_num(1234)
    4321
    >>> reverse_num(1915)
    5191
    """
    i = 3
    rev_num = 0
    while n > 10:
        rev_num += (n % 10 * 10 ** i)
        i -= 1
        n //= 10
    rev_num += n
    return(rev_num)


def pair_shuffle(n:int) -> int:
    """
    >>> pair_shuffle(5434)
    4543
    >>> pair_shuffle(7048)
    784
    """
    t = n // 1000
    n %= 1000
    h = n // 100
    n %= 100
    d = n // 10
    n %= 10
    n = n % 10
    return(h * 1000 + t * 100 + n * 10 + d)


def middle_shuffle(n:int) -> int:
    """
    >>> middle_shuffle(5084)
    5804
    """
    t = n // 1000
    n %= 1000
    h = n // 100
    n %= 100
    d = n // 10
    n %= 10
    n = n % 10
    return(t * 1000 + d * 100 + h * 10 + n)


def two_two_shuffle(n:int) -> int:
    """
    >>> two_two_shuffle(4566)
    6645
    >>> two_two_shuffle(7304)
    473
    """
    t = n // 1000
    n %= 1000
    h = n // 100
    n %= 100
    d = n // 10
    n %= 10
    n = n % 10
    return(d * 1000 + n * 100 + t * 10 + h)


def two_two_shuffle_b(n:int) -> int:
    """
    >>> two_two_shuffle_b(4566)
    6645
    >>> two_two_shuffle_b(7304)
    473
    """
    num = (n % 100) * 100 + n // 100
    return(num)
        


if __name__ == '__main__':
    doctest.testmod()