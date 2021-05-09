def abs_el(nums:list) -> list:
    abs_nums = [abs(x) for x in nums]
    return(abs_nums)


def  find_abs_max_ind(abs_nums:list) -> list:
    abs_max = max(abs_nums)
    ind = [i for i in range(len(abs_nums)) if abs_nums[i] == abs_max]
    return(ind)


def change_abs_max_sign(nums:list) -> list:
    abs_nums = abs_el(nums)
    ind = find_abs_max_ind(abs_nums)
    for i in ind:
        nums[i] *= -1
    return(nums)


"""
nums = [1, 2, 3, 4, -5, 4, 5]

print(* change_abs_max_sign(nums))
"""
