def greater_than_sum(nums:list) -> None:
    d = sum(nums)
    for i in range(len(nums)):
        if nums[i] > d:
            print(i)