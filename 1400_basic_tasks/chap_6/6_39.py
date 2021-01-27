def print_num(n:int) -> None:
    power = 10
    while power < n:
        power *= 10
    power /= 10
    while n:
        num = n // power
        print(int(num))
        n -= num * power
        power /= 10
        
        
