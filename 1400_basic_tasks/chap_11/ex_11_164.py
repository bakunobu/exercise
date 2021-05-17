# a
def even_in_odd_pos(nums:list) -> list:
    odd_ind = list(range(1, len(nums), 2))
    for i in odd_ind[::-1]:
        if not nums[i] % 2:
            nums.pop(i)
    return(nums)


# b
def drop_div_by_tree_five(nums:list) -> list:
    cond_nums = [x for x in nums if x % 3 and x % 5]
    return(cond_nums)