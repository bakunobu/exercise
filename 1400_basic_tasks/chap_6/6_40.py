def count_first_digin(n:int) -> int:
    counter = 0
    power = 10
    while power < n:
        power *= 10
    power /= 10
    
    fd = int(n // power)
    
    while n:
        num = int(n // power)
        if num == fd:
            counter += 1
        n -= num * power
        power /= 10
    
    return(counter)