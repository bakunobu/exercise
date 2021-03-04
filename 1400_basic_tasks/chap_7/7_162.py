from main_funcs import get_input


def last_max_fall(n:int=30) -> int:
    ind = 0
    max_num = get_input('Укажите количество осадков: ', False)
    for i in range(1, n):
        a = get_input('Укажите количество осадков: ', False)
        if a >= max_num:
            ind = i
    return(ind+1)