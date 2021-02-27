from main_funcs import get_input
from typing import Union


def first_demonia() -> Union[int, bool]:
    i = 0
    a = get_input('Введите число: ', False)
    while a <= 100:
        i += 1
        a = get_input('Введите число: ', False)
        if a == 666:
            return(i)
    return(False)
       