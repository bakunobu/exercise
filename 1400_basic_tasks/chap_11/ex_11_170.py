import random
from typing import Union

def find_all_max_nums(nums:list) -> list:
    max_el = max(nums)
    max_ind = [i for i in range(nums) if nums[i] == max_el]
    return(max_ind)


def add_two_nums(nums:list, n_1:Union[int, float],
                 n_2:Union[int, float]) -> list:
    indices = find_all_max_nums(nums)
    i = random.choice(indices)
    nums.insert(i, n_2)
    i += 2
    nums.inser(i, n_1)
    return(nums)