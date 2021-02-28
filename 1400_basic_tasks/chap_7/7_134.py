from main_funcs import get_input


def num_seq_els() -> int:
    nums = []
    prev_a = get_input('Введите число: ')
    while prev_a != 0:
        a = get_input('Введите число: ')
        if prev_a != a:
            nums.append(a)
        prev_a = a
    return(len(nums))