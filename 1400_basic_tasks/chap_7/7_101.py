from main_funcs import get_iput
from typing import Union


def seq_accend() -> Union[int, bool]:
    i = 0
    a_0 = get_input('Введите число: ')
    a = get_input('Введите число: ')
    while a_0 < a and a != 10_000:
        a = get_input('Введите число: ')
        a_0 = a
        i += 1
    if a == 10_000:
        return(True)
    else:
        return(i)