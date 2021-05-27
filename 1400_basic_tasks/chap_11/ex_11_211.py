from typing import Union


def find_last_triplet(nums:list) -> Union[int, None]:
    i = len(nums) - 2
    j = None
    while i > 1:
        if nums[i-1] < nums[i] > nums[i + 1]:
            j = i
            break
        i -= 1
    return(j)


def print_result(nums:list) -> None:
    i = find_last_triplet(nums)
    if i is not None:
        print(* nums[:i-1], sep=', ')
    else:
        print("Таких чисел в массиве нет")