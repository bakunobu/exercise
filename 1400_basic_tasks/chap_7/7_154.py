from main_funcs import get_input


def max_num_seq(n:int) -> int:
    max_seq = 1
    cur_seq = 1
    prev_a = get_input('Введите число: ')
    for _ in range(1, n):
        a = get_input('Введите число: ')
        if a == prev_a:
            cur_seq += 1
        else:
            prev_a = a
            max_seq = max(max_seq, cur_seq)
            cur_seq = 1
    return(max_seq)
    