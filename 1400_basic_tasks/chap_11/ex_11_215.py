def find_not_same(nums:list) -> None:
    diff = [int(nums[i] - nums[0] == 0) for i in range(len(nums))]
    try:
        i = diff.index(0)
        print(* nums[i:])
    except ValueError:
        print('Массив состоит из одинаковых чисел')
        
