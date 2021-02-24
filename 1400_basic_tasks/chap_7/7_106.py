from main_funcs import get_input


def calc_mean(n:int) -> float:
    i = 0
    my_sum = 0
    for _ in range(n):
        c = get_input('Введите число: ')
        if c > 20:
            i += 1
            my_sum += c
    return(my_sum / i)
        