# a
def two_max_num(n:int) -> tuple:
    max_one = 0
    max_two = 1
    while n:
        num = n % 10
        if num > max_two:
            max_one, max_two = max_two, num
        elif num > max_one:
            max_one = num
        n //= 10
    return(max_one, max_two)


# b
def two_min_num(n:int) -> tuple:
    min_one = 9
    min_two = 8
    while n:
        num = n % 10
        if num < min_two:
            min_one, min_two = min_two, num
        elif num < min_one:
            min_one = num
        n //= 10
    return(min_one, min_two)