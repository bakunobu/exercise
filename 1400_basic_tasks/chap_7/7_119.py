from main_funcs import get_input


def last_gtehund(n:int) -> int:
    last_ind = 0
    for i in range(n):
        b = get_input('Введите число: ', False)
        if b > 100:
            last_ind = i
    return(i)