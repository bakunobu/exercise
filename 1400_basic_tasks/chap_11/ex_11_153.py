def shift_three_els(nums:list) -> list:
    nums[0], nums[1], nums[2],\
    nums[-3], nums[-2], nums[-1] = nums[-3],\
    nums[-2], nums[-1], nums[0], nums[1], nums[2]
    return(nums)


# num_list = [1, 2, 3, 4, 5, 6, 7]
# print(shift_three_els(num_list))