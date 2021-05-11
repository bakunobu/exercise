from typing import Union

# a
def substr(nums:list) -> list:
    substr_list = [ x - 20 for x in nums]
    return(substr_list)


# b
def prod_last(nums:list) -> list:
    prod_list = [x * nums[-1] for x in nums]
    return(prod_list)


# c
def sum_b(nums:list, b:Union[int, float]) -> list:
    sum_list = [x + b for x in nums]
    return(sum_list)