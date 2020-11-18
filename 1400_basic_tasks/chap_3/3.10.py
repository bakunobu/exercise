import doctest


def which_day(given_day:int,
              year_start:int) -> int:
    """
    >>> which_day(400, 1)
    Out of range
    >>> which_day(14, 1)
    0
    >>> which_day(8, 1)
    1
    >>> which_day(25, 3)
    6
    """
    
    if given_day < 1 or given_day > 365:
        print('Out of range')
        return(None)
    else:
        return(year_start+given_day % 7 - 1)



if __name__ == "__main__":
    doctest.testmod()