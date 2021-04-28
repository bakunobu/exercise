def find_same_els(nums:list) -> tuple:
    el = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == el:
            return(el, nums.index(el), i)
        else:
            el = nums[i]
    return(0,0)