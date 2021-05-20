# a
def find_first_a(nums:list, a:int=5) -> int:
    return(nums.index(a))


# b
def find_last_a(nums:list, a:int=5) -> int:
    rev_list = nums[::-1]
    j = rev_list.index(a)
    i = len(nums) - j
    return(i)
