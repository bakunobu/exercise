def greater_than_mean(nums:list) -> None:
    d = (max(nums) + min(nums)) / 2
    for i in range(len(nums)):
        if nums[i] > d:
            print(i)