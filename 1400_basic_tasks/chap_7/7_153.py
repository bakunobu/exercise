from main_funcs import get_input
from typing import Union


# a
def max_even(n:int=14) -> Union[int, bool]:
    max_even_num = False
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if not a % 2:
            if not max_even_num:
                max_even_num = a
            else:
                max_even_num = max(a, max_even_num)
    
    return(max_even_num)


# b
def adj_max_even(n:int=14) -> Union[int, bool]:
    msg = 'Введите число: '
    nums = [get_input(msg, False) for x in range(n)]
    even_nums = [x for x in nums if not x % 2]
    if even_nums:
        return(max(even_nums))
    else:
        return(False)