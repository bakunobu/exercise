from typing import Union


# a
def add_hundr(nums:list) -> list:
    new_list = list(100,)
    new_list += nums
    return(new_list)


# b
def add_any(nums:list, n:Union[int, float]) -> list:
    new_list = list(n)
    new_list += nums
    return(new_list)


# c
def add_any_to_any_place(nums:list,
                         n:Union[int, float],
                         i:int) -> int:
    new_list = nums[:i]
    new_list.append(n)
    new_list += nums[i:]
    return(new_list)