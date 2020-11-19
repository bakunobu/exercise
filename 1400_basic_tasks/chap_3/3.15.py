import doctest


# a
def get_cell_address(n:int) -> tuple:
    """
    >>> get_cell_address(1)
    (1, 1)
    >>> get_cell_address(120)
    (1, 8)
    >>> get_cell_address(121)
    (2, 1)
    >>> get_cell_address(127)
    (2, 1)    
    """
    i = n // 120 + min(1, n % 120)
    n = n - 120 * (i - 1)
    j = n // 8 + min(1, n % 8)
    return(i, j)

# b
def get_cell_address_alt(n: int) -> tuple:
    """
    >>> get_cell_address_alt(1)
    (1, 1)
    >>> get_cell_address_alt(10)
    (10, 1)
    >>> get_cell_address_alt(151)
    (1, 2)
    """
    shell_dict = {0: 10,
                  1: 1,
                  2: 2,
                  3: 3,
                  4: 4,
                  5: 5,
                  6: 6,
                  7: 7,
                  8: 8,
                  9: 9}
    
    i = shell_dict[n % 10]
    j = n // 150 + min(1, n % 150)
    return(i, j)
    
     
     

if __name__ == "__main__":
    doctest.testmod()