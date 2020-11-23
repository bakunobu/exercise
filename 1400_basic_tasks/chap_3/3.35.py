import doctest


def construct_num(n:int) -> int:
    """
    >>> construct_num(564)
    456
    """
    first_digit = n % 10
    n //= 10
    n += first_digit * 100

    return(n)
    



if __name__ == "__main__":
    doctest.testmod()