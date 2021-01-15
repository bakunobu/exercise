def return_mirror_num(x:int) -> int:
    num = 0
    for i in range(7):
        num *= 10
        num += x % 10
        x //= 10
    return(num)


