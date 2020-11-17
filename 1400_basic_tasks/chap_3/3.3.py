import doctest


def weeks_in_period(d:int=324) -> int:
    """
    >>> weeks_in_period(14)
    2
    >>> weeks_in_period(15)
    2
    >>> weeks_in_period(5)
    0
    """
    return(d//7)


if __name__ == "__main__":
    doctest.testmod()
    print(weeks_in_period())
    