def snd_digit(n:int) -> int:
    while n > 100:
        n //= 10
    return(n % 10)