nums = []
i = 107
while len(nums) < 10:
    if i % 9 == 0:
        nums.append(i)
    i += 10
    
print(* nums, sep=', ')