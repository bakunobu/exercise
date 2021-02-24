from main_funcs import get_iput
from typing import Union


def seq_accend(n:int) -> Union[int, bool]:
    i = 0
    a_0 = get_input('Введите число: ')
    a = get_input('Введите число: ')
    while a_0 < a and i < n-1:
        a = get_input('Введите число: ')
        a_0 = a
        i += 1
    if i == n:
        return(True)
    else:
        return(i)