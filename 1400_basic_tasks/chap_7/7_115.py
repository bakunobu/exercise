from main_funcs import get_input
from typing import Union


def mean_series(m:int, n:int) -> float:
    tot_sum = 0
    tot_num = 0
    for _ in range(m):
        a = get_input('Введите число: ', False)
        if not a % n:
            tot_num += 1
            tot_sum += a 
    
    
    if tot_num == 0:
        return(0)
    else:
        return(tot_sum / tot_num)