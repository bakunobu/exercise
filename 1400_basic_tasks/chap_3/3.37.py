import doctest


def rest_dig(n:int) -> int:
    """
    >>> rest_dig(546)
    456
    """
    mid_dig = n // 100
    n %= 100
    first_dig = n // 10
    last_dig = n % 10
    n = last_dig + mid_dig * 10 + first_dig * 100
    return(n)

def rest_dig_input() -> int:
    n = int(input())
    return(rest_dig(n))
    

if __name__ == "__main__":
    doctest.testmod()