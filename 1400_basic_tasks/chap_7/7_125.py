from main_funcs import get_input


def get_seq(n:int=15) -> list:
    msg = 'Введите число: '
    nums = [get_input(msg) for _ in range(n)]
    return(nums)


# a
def calc_sum(my_list:list) -> float:
    total = 0
    new_num = get_input('Введите число: ')
    i = 0
    while new_num > my_list[i]:
        total += my_list[i]
        i += 1
    return(total)

# b
def find_ind(my_list:list) -> tuple:
    new_num = get_input('Введите число: ')
    i = 0
    while new_num > my_list[i]:
        i += 1
    return(i, i+1)