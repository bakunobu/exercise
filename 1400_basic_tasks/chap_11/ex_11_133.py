def which_earlier(nums:list) -> str:
    if nums.index(max(nums)) > nums.index(min(nums)):
        return('max')
    else:
        return('min')