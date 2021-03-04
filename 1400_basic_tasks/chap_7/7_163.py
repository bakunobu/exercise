import numpy as np
from main_funcs import get_input


def collect_time(n:int) -> list:
    msg = 'Укажите время обслуживания покупателя: '
    wait_list = [get_input(msg) for _ in range(n)]
    return(wait_list)


def calc_cum_sum(my_list:list) -> np.ndarray:
    my_array = np.array(my_list)
    cum_sum = np.cumsum(my_array)
    return(cum_sum)


def find_least_time(my_array:np.ndarray) -> int:
    min_el = min(my_array)
    min_index = my_array[::-1].index(min_el)
    return(len(my_array) - min_index)
