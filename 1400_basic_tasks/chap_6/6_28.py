nums = []
i = 500
while len(nums) < 20:
    i += 1
    if i % 13 == 0 or i % 17 == 0:
        nums.append(i)

print(* nums, sep =', ')