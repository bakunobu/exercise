from main_funcs import get_input


def calc_no_moist(d:int=31, lim:int=10):
    num_no_moist = 0
    i = 0
    while num_no_moist < lim and i < d:
        f = get_input('Укажите число осадков за день: ')
        i += 1
        if f == 0:
            num_no_moist += 1
    return(num_no_moist >= lim)