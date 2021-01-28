def min_max_indices(n:int) -> str:
    i = 0
    min_dig = 9
    max_dig = 0
    min_i = 0
    max_i = 0
    while n:
        num = n % 10
        if num > max_dig:
            max_dig = num
            max_i = i
        if num < min_dig:
            min_dig = num
            min_i = i
    if max_i > min_i:
        print('Greater')
    else:
        print('Lesser')
