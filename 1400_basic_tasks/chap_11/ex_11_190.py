def transform_list(nums:list) -> list:
    cond_list = [int(x > 65530) for x in nums]
    return(cond_list)



# a
def find_first_a(nums:list, a:int=1) -> int:
    nums = transform_list(nums)
    return(nums.index(a))



# b
def find_last_a(nums:list, a:int=1) -> int:
    nums = transform_list(nums)
    rev_list = nums[::-1]
    j = rev_list.index(a)
    i = len(nums) - j
    return(i)


