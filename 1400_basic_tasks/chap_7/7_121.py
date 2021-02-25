from main_funcs import get_input


def last_neg(k:int) -> int:
    last_ind = ''
    for i in range(k):
        b = get_input('Введите число: ', False)
        if b < 0:
            last_ind = i
    return(last_ind)