from main_funcs import get_input


def count_pos_neg(n:int) -> tuple:
    pos_nums = 0
    neg_nums = 0
    for _ in range(n):
        a = get_input('Введите число: ')
        if a > 0:
            pos_nums += 1
        elif a < 0:
            neg_nums += 1
        else:
            pass
    return(pos_nums, neg_nums)