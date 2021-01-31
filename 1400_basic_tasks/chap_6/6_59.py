def min_num_count(n:int) -> int:
    counter = 0
    min_num = 9
    while n:
        num = n % 10
        if num == min_num:
            counter += 1
        if num < min_num:
            min_num = num
            counter = 1
        n //= 10
    return(counter)