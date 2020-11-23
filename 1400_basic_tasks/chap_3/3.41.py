import doctest


def restore_dig(n:int) -> int:
    """
    >>> restore_dig(654)
    546
    """
    
    last_dig = 654 // 100
    n = 654 % 100
    mid_dig = n % 10
    first_dig = n // 10

    n = last_dig + mid_dig * 10 + first_dig * 100
    return(n)


def rest_dig_input() -> int:
    n = int(input())
    return(restore_dig(n))
    

if __name__ == "__main__":
    doctest.testmod()