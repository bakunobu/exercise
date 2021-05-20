from typing import Union


# a
def return_all_less_a(nums:list, a:Union[int, float]) -> list:
    indices = list(set([i * int(nums[i] < a) for i in range(len(nums))]))
    indices.sort()
    indices.pop(0)
    return(indices)

def print_els(nums:list, indices:list) -> None:
    for i in indices:
        print(nums[i], end=', ')
        

# b
def all_ind_to_bin(nums:list, a:Union[int, float]) -> tuple:
    indices = [i * int(nums[i] < a) for i in range(len(nums))]
    i = indices.index(0)
    return(i-1, i)


# c
def find_closest_el(nums:list, a:Union[int, float]) -> tuple:
    i, j = all_ind_to_bin(nums, a)
    abs_i = abs(nums[i] - a)
    abs_j = abs(nums[j] - a)
    if abs_i > abs_j:
        return(j, nums[j])
    else:
        return(i, nums[i])