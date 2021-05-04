# a 
def max_els_ind(nums:list) -> list:
    ind = [i for i in range(nums) if nums[i] == max(nums)]
    return(ind)


# b
def min_els_ind(nums:list) -> list:
    ind = [i for i in range(nums) if nums[i] == min(nums)]
    return(ind)