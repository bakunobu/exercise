def odd_el(nums:list) -> None:
    pairs = [1 if nums[i] % 2 and nums[i + 1] % 2 else 0 for i in range(len(nums) - 1)]
    if 1 in pairs:
        i = pairs.index(1)
        print(i, i+1)
    else:
        print('Таких чисел в массиве нет!')
