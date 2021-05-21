def find_same(nums:list) -> list:
    is_same = [int(x == nums[0]) for x in nums]
    return(is_same)


def get_index(indices:list, ind:int=0) -> int:
    return(indices.index(ind))


def print_other_els(nums:list) -> None:
    indices = find_same(nums)
    i = get_index(indices) + 1
    print(* nums[i:])