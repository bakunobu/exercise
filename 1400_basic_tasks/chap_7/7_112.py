from main_funcs import get_input
from typing import Union


def mean_series(n:int, cond:Union[int, float]=10) -> float:
    tot_sum = 0
    tot_num = 0
    for _ in range(n):
        b = get_input('Введите число: ')
        if a > 10:
            tot_num += 1
            tot_sum += b 
    
    
    if tot_num == 0:
        return(0)
    else:
        return(tot_sum / tot_num)