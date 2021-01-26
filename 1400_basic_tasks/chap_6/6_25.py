import doctest

def find_least_div(n:int) -> int:
    """
    >>> find_least_div(4)
    2
    >>> find_least_div(5)
    5
    >>> find_least_div(9)
    3
    """
    div = 1
    while div < n:
        div += 1
        if n % div == 0:
            return(div)
        
        
if __name__ == '__main__':
    doctest.testmod()