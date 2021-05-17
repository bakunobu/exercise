from typing import Any


def insert_el(nums:list, ind:int, el:Any=100) -> list:
    nums.insert(ind, el)
    return(nums)


# a
def find_first_neg_ind(nums:list) -> int:
    for i in range(len(nums)):
        if nums[i] < 0:
            return(i)
    

def insert_first_neg(nums:list, el:Any) -> list:
    i = find_first_neg_ind(nums)
    new_nums = insert_el(nums, i, el)
    return(new_nums)


# b
def find_last_even(nums:list) -> int:
    i = len(nums)-1
    while i > 0:
        if not nums[i] % 2:
            return(i)
        i -= 1
    return(i)


def insert_last_even(nums:list, el:Any) -> list:
    i = find_last_even(nums)
    new_nums = insert_el(nums, i, el)
    return(new_nums)