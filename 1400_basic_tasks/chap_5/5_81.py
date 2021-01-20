def find_nums(a: int) -> list:
    nums = []
    for _ in range(3):
        num = a % 10
        a //= 10
        nums.append(num)
    return(nums)

# a
for x in range(100, 1000):
    if x ** 2 % 1000 == x:
        print(x, x ** 2)


# b
for x in range(100, 1000):
    sum_num = sum(find_nums(x))
    if x % 7 == 0 and sum_num % 7 == 0:
        print(x)