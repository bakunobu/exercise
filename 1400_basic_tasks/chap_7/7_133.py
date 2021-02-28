from main_funcs import get_input


def num_els() -> int:
    num_seq = 1
    prev_a = get_input('Введите число: ')
    while prev_a != 1000:
        a = get_input('Введите число: ')
        if a == prev_a:
            num_seq += 1
        prev_a = a
    return(num_seq)