import doctest

def secs_in_day(s: int) -> int:
    """
    >>> secs_in_day(3600)
    1
    >>> secs_in_day(7205)
    2
    """
    return(s // 3600)

def mins_gone(s: int) -> int:
    """
    >>> mins_gone(3660)
    1
    >>> mins_gone(3665)
    1
    """
    s_i = secs_in_day(s)
    s -= (s_i * 3600)
    return(s // 60)

def secs_gone(s: int) -> int:
    """
    >>> secs_gone(3665)
    5
    >>> secs_gone(3660)
    0
    """
    s_i = secs_in_day(s)
    s -= (s_i) * 3600
    return(s % 60)

if __name__ == "__main__":
    doctest.testmod()