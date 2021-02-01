def calc_bones(n) -> tuple:
    num_1 = 0
    num_2 = 0
    num_4 = 0
    num_8 = 0
    num_16 = 0
    num_32 = 0
    num_64 = 0
    while n:
        if n >= 64:
            num = n // 64
            num_64 += num
            n %= 64
        elif n >= 32:
            num = n // 32
            num_32 += num
            n %= 32
        elif n >= 16:
            num = n // 16
            num_16 += num
            n %= 16
        elif n >= 8:
            num = n // 8
            num_8 += num
            n %= 8
        elif n >= 4:
            num = n // 4
            num_4 += num
            n %= 4
        elif n >= 2:
            num = n // 2
            num_2 += num
            n %= 2
        else:
            n -= 1
            num_1 += 1
    return(num_1, num_2, num_4, num_8, num_16,
           num_32, num_64)

