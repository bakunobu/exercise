# a
def drop_by_index(nums:list, i:int) -> list:
    nums.pop(i)
    return(nums)


# b
def drop_by_value(nums:list, h:float) -> list:
    nums.remove(h)
    return(nums)