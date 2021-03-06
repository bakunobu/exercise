from main_funcs import get_input


# a
def count_max_inhab(n:int) -> int:
    msg = 'Укажите количество жильцов: '
    nums = [get_input(msg, False) for _ in range(n)]
    max_num = max(nums)
    return(nums.count(max_num))
