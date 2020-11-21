import doctest


def four_digits_num(n: int) -> int:
    """
    >>> four_digits_num(9000)
    9
    >>> four_digits_num(1234)
    10
    >>> four_digits_num(1925)
    17
    """
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    
    return(total)


def sum_dig_input():
    n = int(input('Введите четырехзначное число: '))
    return(four_digits_num(n))
        
    


if __name__ == "__main__":
    doctest.testmod()