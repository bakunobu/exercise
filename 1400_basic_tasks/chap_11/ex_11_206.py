def eq_el(nums:list) -> None:
    pairs = [1 if nums[i] == nums[i + 1] else 0 for i in range(len(nums) - 1)]
    print(pairs)
    if 1 in pairs:
        i = pairs.index(1) + 2
        print(* nums[i:], sep=', ')
    else:
        print('Таких чисел в массиве нет!')
        
        
        
        
