from main_funcs import get_input
from typing import Union


def first_div_seven() -> Union[int, bool]:
    i = 0
    a = get_input('Введите число: ', False)
    while a != -1:
        i += 1
        a = get_input('Введите число: ', False)
        if not a % 7:
            return(i)
    return(False)
       