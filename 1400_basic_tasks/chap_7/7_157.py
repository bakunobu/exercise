from main_funcs import get_input

# a
def last_max(n:int) -> int:
    ind = 0
    max_num = get_input('Введите число: ', False)
    for i in range(1, n):
        a = get_input('Введите число: ', False)
        if a >= max_num:
            ind = i
    return(ind)


# b
def last_min(n:int) -> int:
    ind = 0
    min_num = get_input('Введите число: ', False)
    for i in range(1, n):
        a = get_input('Введите число: ', False)
        if a <= min_num:
            ind = i
    return(ind)