from main_funcs import get_iput
from typing import Union


def seq_num_ind(n:int) -> Union[int, bool]:
    i = 0
    a_0 = get_input('Введите число: ', False)
    for _ in range(n-1):
        a = get_input('введите число: ', False)
        if a_0 == a:
            return(i)
        a_0 = a
        i += 1
    return(False)