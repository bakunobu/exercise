# a
def drop_two_studs(nums:list, i:int, j:int) -> list:
    i, j = min(i, j), max(i,j)
    nums.pop(j)
    nums.pop(i)
    return(nums)


# b
def drops_two_studs_b(nums:list, h_1:float,
                      h_2:float) -> list:
    nums.remove(h_1)
    nums.remove(h_2)
    return(nums)
