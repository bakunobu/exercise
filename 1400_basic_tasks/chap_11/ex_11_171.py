from typing import Union


# a
def get_indices(nums:list, a:Union[int, float]) -> list:
    indices = [i for i in range(len(nums)) if not nums[i] % 2]
    indices = [i + indices[i] for i in range(len(indices))]
    return(indices)


def add_num_nums(nums:list, a:Union[int, float],
                 n:Union[int, float]) -> list:
    indices = get_indices(nums, a)
    for i in indices:
        nums.insert(i, n)
    return(n)


# b
def get_neg_indices(nums:list) -> list:
    neg_ind = [i for i in range(len(nums)) if nums[i] < 0]
    return(neg_ind)


def preproc_ind(indices:list) -> list:
    i = 1
    for j in range(len(indices)):
        indices[j] += i
        i += 1
    return(indices)


def insert_after(nums:list, n:Union[int, float]) -> list:
    neg_ind = get_neg_indices(nums)
    prep_ind = preproc_ind(neg_ind)
    for i in prep_ind:
        nums.insert(i, n)
    return(nums)