from main_funcs import get_input
from typing import Union


def mean_series(n:int) -> float:
    tot_sum = 0
    tot_num = 0
    for _ in range(n):
        d = get_input('Введите число: ')
        if not d % 2:
            tot_num += 1
            tot_sum += d 
    
    
    if tot_num == 0:
        return(0)
    else:
        return(tot_sum / tot_num)