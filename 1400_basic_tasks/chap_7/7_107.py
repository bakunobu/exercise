from main_funcs import get_input
from typing import Union


def calc_mean(x:int, n:Union[int, float]) -> float:
    i = 0
    my_sum = 0
    for _ in range(x):
        a = get_input('Введите число: ', False)
        if a > n:
            i += 1
            my_sum += a
    return(my_sum / i)
        