import doctest


def funny_divs(a:int, b:int) -> int:
    """
    >>> funny_divs(2, 3)
    0
    >>> funny_divs(2, 6)
    1
    """
    state_1 = a % b == 0
    state_2 = b % a == 0
    return(int(state_1 or state_2))


if __name__ == "__main__":
    doctest.testmod()
