def transform_list(nums:list) -> list:
    cond_list = [int(x == 0) for x in nums]
    return(cond_list)



# a
def find_first_a(nums:list, a:int=1) -> int:
    nums = transform_list(nums)
    return(nums.index(a))

def print_all_except_first_zero(input_list:list) -> None:
    temp_list = input_list[:]
    i = find_first_a(temp_list)
    input_list.pop(i)
    print(* input_list)



# b
def find_last_a(nums:list, a:int=1) -> int:
    nums = transform_list(nums)
    rev_list = nums[::-1]
    j = rev_list.index(a)
    i = len(nums) - j
    return(i)


def print_all_except_last_zero(input_list:list) -> None:
    temp_list = input_list[:]
    i = find_last_a(temp_list)
    input_list.pop(i)
    print(* input_list)