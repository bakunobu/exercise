from main_funcs import get_input
from typing import Union


def last_tf(n:int) -> Union[int, bool]:
    last_ind = False
    for i in range(n):
        c = get_input('Введите число: ', False)
        if c == 25:
            last_ind = i
    
    return(last_ind)