from typing import Union

# a
def del_all_neg(nums:list) -> list:
    pos_nums = [num for num in nums if num > 0]
    return(pos_nums)


# b
def greater_n(nums:list, n:Union[int, float]) -> list:
    cond_nums = [num for num in nums if num <= n]
    return(cond_nums)


# c
def drop_slice(nums:list, n_1:int, n_2:int) -> list:
    drop_nums = nums[:n_1]
    drop_nums += nums[n_2:]
    return(drop_nums)