from typing import Union


# a
def mult_two(nums:list) -> list:
    double_nums = [x * 2 for x in nums]
    return(double_nums)


# b
def diff_a(nums:list, a:Union[int, float]) -> list:
    diff_list = [x - a for x in nums]
    return(diff_list)


# c
def div_by_first(nums:list) -> list:
    try:
        div_list = [x / nums[0] for x in nums]
    except ZeroDivisionError:
        print('Division by zero, eps added')
        eps = 1e-8
        div_list = [x / eps for x in nums]
    return(div_list)