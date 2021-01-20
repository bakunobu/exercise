def find_nums(n:int) -> int:
    nums = []
    while n:
        u = n % 10
        nums.append(u)
        n //= 10
    return(nums)

# a
for x in range(10, 100):
    t, u = find_nums(x)
    if (t ** 2 + u ** 2) % 13 == 0:
        print(x)
        

# b
for x in range(10, 100):
    num_sum = sum(find_nums(x))
    if num_sum + num_sum ** 2 == x:
        print(x)