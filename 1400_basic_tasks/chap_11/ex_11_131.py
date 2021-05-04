def min_max_diff(nums:list) -> bool:
    return(max(nums) / min(nums) > 2)


def heigth_diff(nums:list) -> bool:
    return(min_max_diff(nums))