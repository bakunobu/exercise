def num_to_digit(a:int) -> list:
    nums = []
    nums.append(a % 10)
    a -= nums[-1]
    while a > 0:
        a /= 10
        nums.append(int(a % 10))
        a -= nums[-1]
    return(nums[::-1])


# a
def a_eq_b(a:int) -> bool:
    nums = num_to_digit(a)
    return(sum(nums[:2]) == sum(nums[2:]))


# b
def div_three(a:int) -> bool:
    nums = num_to_digit(a)
    return(not sum(nums) % 3)


# c
def div_four(a:int) -> bool:
    nums = num_to_digit(a)
    return(not sum(nums) % 4)


# d
def div_a(num:int, a:int) -> bool:
    nums = num_to_digit(num)
    return(not sum(nums) % a)