from typing import Union


def find_triplets(nums:list) ->Union[int, None]:
    for i in range(1, len(nums) - 1):
        if nums[i-1] < nums[i] > nums[i+1]:
            return(i)
    return(None)


def print_triplet_res(nums:list) -> None:
    i = find_triplets(nums)
    if i is not None:
        print(i-1, i, i+1)
    else:
        print('Таких чисел в массиве нет!')