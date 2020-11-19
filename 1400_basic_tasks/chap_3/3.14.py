import doctest


def find_block(n: int) -> int:
    """
    >>> find_block(1)
    1
    >>> find_block(54)
    1
    >>> find_block(55)
    2
    """
    return(n // 55 + 1)


def find_floor(n: int) -> int:
    """
    >>> find_floor(1)
    1
    >>> find_floor(54)
    9
    >>> find_floor(55)
    1
    """
    block = find_block(n)
    n = n - 54 * (block - 1)
    return(n // 6 + min(1, n % 6))

def find_num(n: int) -> int:
    """
    >>> find_num(1)
    1
    >>> find_num(54)
    6
    >>> find_num(55)
    1
    """
    n = n - 54 * (n // 54)
    n = n - 6 * (n // 6)
    flat_nums = {1:1,
                 2:2,
                 3:3,
                 4:4,
                 5:5,
                 0:6}
    return(flat_nums[n%6])            


if __name__ == "__main__":
    doctest.testmod()