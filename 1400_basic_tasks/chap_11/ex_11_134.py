def which_earlier(nums:list) -> str:
    if nums.index(max(nums)) > nums.index(min(nums)):
        return('Oldes')
    else:
        return('Yongest')