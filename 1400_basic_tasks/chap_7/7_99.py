from main_funcs import get_iput
from typing import Union


def seq_even_num_ind() -> Union[int, bool]:
    i = 0
    a_0 = get_input('Введите число: ', False)
    a = ''
    while a != 9999:
        a = get_input('введите число: ', False)
        if not a_0 % 2 and not a % 2:
            return(i)
        a_0 = a
        i += 1
    return(False)