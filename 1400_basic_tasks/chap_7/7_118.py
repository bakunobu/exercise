from main_funcs import get_input


# a
def first_ten_appear(n:int) -> int:
    i = -1
    a = ''
    while a >= 10:
        a = get_input('Введите число: ', False)
        i += 1
    return(i)


# b
def last_ten_appear(n:int) -> int:
    i = 0
    a = ''
    last_a = 0
    while i < n:
        a = get_input('Введите число: ', False)
        if a == 10:
            last_a = i
        i += 1
    return(last_a)
        