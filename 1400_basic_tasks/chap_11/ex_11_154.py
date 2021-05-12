# a
def replace_els(nums:list) -> list:
    new_list = []
    new_list += nums[:2]
    new_list += nums[9:2:-1]
    new_list += nums[10:]
    return(new_list)


# b
def get_els(msg:str) -> tuple:
    while 1:
        try:
            k, s = (int(x) for x in input(msg).split())
            return(k, s)
        except ValueError:
            print('Используйте целые числа!')


def users_shift(nums:list) -> list:
    k,s = get_els('Укажите начало и конец среза (через пробел): ')
    new_list = []
    new_list += nums[:k]
    new_list += nums[s:k:-1]
    new_list += nums[s+1:]
    return(new_list)


# c
def min_max_shift(nums:list) -> list:
    i = nums.index(min(nums)) # min
    j = nums.index(max(nums)) # max
    new_list = []
    new_list += nums[:i]
    new_list += nums[j:i:-1]
    new_list += nums[j+1:]
    return(new_list)
    