def trd_digit(n:int) -> int:
    while n > 1000:
        n //= 10
    return(n % 10)


