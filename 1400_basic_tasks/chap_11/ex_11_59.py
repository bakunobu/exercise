from typing import Union


# a
def sum_lim_els(nums:list, d:Union[int, float]=20) -> Union[int, float]:
    cond_list = [x for x in nums if x <= d]
    return(sum(cond_list))


# b
def sum_lim_els(nums:list, a:Union[int, float]) -> Union[int, float]:
    cond_list = [x for x in nums if x > a]
    return(sum(cond_list)) 