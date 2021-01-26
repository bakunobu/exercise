nums = []
i = 100
while True:
    i += 1
    if i % 19 == 0:
        nums.append(i)
        while len(nums) < 15:
            i += 19
            nums.append(i)
        break

print(* nums, sep =', ')