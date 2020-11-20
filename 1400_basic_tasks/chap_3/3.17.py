import doctest

def num_sum(x:int) -> int:
    """
    >>> num_sum(20)
    2
    >>> num_sum(19)
    10
    >>> num_sum(23)
    5
    """
    return(x // 10 + x % 10)


num = int(input())
print(num_sum(num))
    

if __name__ == "__main__":
    doctest.testmod()