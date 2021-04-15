import random

unique_nums = []
while len(unique_nums) < 20:
    num = random.randint(1, 1000)
    if num not in unique_nums:
        unique_nums.append(num)
        
print(unique_nums)