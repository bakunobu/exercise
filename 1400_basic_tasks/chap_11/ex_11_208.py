def odd_el(nums:list) -> None:
    pairs = [1 if not nums[i] % 2 and not nums[i + 1] % 2 else 0 for i in range(len(nums) - 1)]
    if 1 in pairs:
        i = pairs.index(1)
        print(* nums[:i], sep=', ')
    else:
        print('Таких чисел в массиве нет!')
        