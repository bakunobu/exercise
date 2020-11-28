import doctest

# a
def base_index(k:int) -> int:
    """
    >>> base_index(3)
    0
    >>> base_index(6)
    1
    >>> base_index(9)
    2
    >>> base_index(150)
    49
    """
    return(int(k / 3) - 1)

# b
def odd_index(k:int) -> int:
    """
    >>> odd_index(1)
    0
    >>> odd_index(4)
    1
    >>> odd_index(7)
    2
    >>> odd_index(148)
    49
    """
    return((k-1) // 3)


# c
def even_index(k:int) -> int:
    """
    >>> even_index(2)
    0
    >>> even_index(5)
    1
    >>> even_index(8)
    2
    >>> even_index(149)
    49
    """
    return((k - 2) // 3)



if __name__ == "__main__":
    doctest.testmod()