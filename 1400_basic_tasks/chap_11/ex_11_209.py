# a
def num_to_digits(num:int) -> tuple:
    if num < 10:
        return(0, num)
    else:
        return(num // 10, num % 10)
    
    
def compare_two_nums(x:int, y:int) -> bool:
    num_1 = num_to_digits(x)
    num_2 = num_to_digits(y)
    return(num_1[0] == num_2[1])


def seq_compare_a(nums:list) -> bool:
    for i in range(len(nums) - 1):
        if not compare_two_nums(nums[i], nums[i+1]):
            return(False)
    return(True)


# b
def has_same_nums(x:int, y:int) -> bool:
    num_1 = num_to_digits(x)
    num_2 = num_to_digits(y)
    return(num_1[0] in num_2 or num_1[1] in num_2)


def seq_compare_b(nums:list) -> bool:
    for i in range(len(nums) - 1):
        if not has_same_nums(nums[i], nums[i+1]):
            return(False)
    return(True)
