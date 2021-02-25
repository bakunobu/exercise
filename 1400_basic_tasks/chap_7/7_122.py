from main_funcs import get_input
from typing import Union


def last_eds_with_tw(m:int) -> Union[int, bool]:
    last_ind = False
    for i in range(m):
        x = get_input('Введите число: ', False)
        if x % 100 == 12:
            last_ind = i
    return(last_ind)