def max_num_count(n:int) -> int:
    counter = 0
    max_num = 0
    while n:
        num = n % 10
        if num == max_num:
            counter += 1
        if num > max_num:
            max_num = num
            counter = 1
        n //= 10
    return(counter)