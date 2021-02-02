import doctest

def fib_seq(n:int) -> bool:
    '''
    >>> fib_seq(5)
    True
    >>> fib_seq(8)
    True
    >>> fib_seq(11)
    False
    >>> fib_seq(13)
    True
    '''
    fib_seq = [1,]
    a, b = 1, 1
    while fib_seq[-1] < n:
        a, b = b, a + b
        fib_seq.append(b)
    return(fib_seq[-1] == n)


if __name__ == '__main__':
    doctest.testmod()
