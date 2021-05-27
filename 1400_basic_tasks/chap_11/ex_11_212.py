from typing import Union


def is_accending(nums:list) -> Union(None, int):
    i = None
    for j in range(len(nums) - 1):
        if nums[j] > nums[j+1]:
            i = j
            break
    return(i)



def print_is_ccending(nums:list) -> None:
    i = is_accending(nums)
    if i is not None:
        print(i)
    else:
        print('Таких числе в масиве нет!')