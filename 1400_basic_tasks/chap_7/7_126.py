from main_funcs import get_input
from typing import Union


def first_neg_ind() -> Union[int, bool]:
    i = 0
    a = get_input('Введите число: ')
    while a <= 100:
        i += 1
        a = get_input('Введите число: ')
    if i == n:
        return(False)
    else:
        return(i) 
        