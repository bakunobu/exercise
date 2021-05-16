# a
def del_first_neg(nums:list) -> list:
    for i in range(len(nums)):
        if nums[i] < 0:
            nums.pop(i)
            break
    return(nums)


# b
def del_last_even(nums:list) -> list:
    for i in range(len(nums),0,-1):
        i -= 1
        if nums[i] % 2 == 0:
            nums.pop(i)
            break
    return(nums)
        