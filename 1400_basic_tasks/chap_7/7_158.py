from main_funcs import get_input


def last_min_max_index(m:int) -> tuple:
    d = get_input('Введите число: ', False)
    min_ind = 0
    max_ind = 0
    min_num = d
    max_num = d
    for i in range(1, m):
        d = get_input('Введите число: ', False)
        if d >= max_num:
            max_num = d
            max_ind = i
        elif d <= min_num:
            min_num = d
            min_ind = i
    return(max_ind, min_ind)