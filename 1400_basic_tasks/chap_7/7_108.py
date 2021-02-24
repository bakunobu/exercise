from main_funcs import get_input


def calc_mean(m:int, n:int) -> float:
    i = 0
    my_sum = 0
    for _ in range(m):
        b = get_input('Введите число: ', False)
        if not b % n:
            i += 1
            my_sum += b
    return(my_sum / i)
        