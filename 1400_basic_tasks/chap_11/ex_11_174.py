from typing import Union


def is_five_init(x:int) -> bool:
    while x:
        if not x % 5 and x % 10:
            return(True)
        x //= 10
    return(False)


def cont_five_ind(nums:list, a:Union[int, float]) -> list:
    ind_five = [i for i in range(len(nums)) if is_five_init(nums[i])]
    i = 1
    for j in range(len(nums)):
        ind_five[j] += i
        i += 1
    for i in ind_five:
        nums.insert(i, a)
    return(nums)
    