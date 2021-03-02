from main_funcs import get_input


def max_seq_len(n:int) -> int:
    max_seq_len = 1
    seq_len = 1
    prev_num = 0
    for _ in range(n):
        d = get_input('Введите число: ', False)
        if d == prev_num:
            seq_len += 1
        else:
            seq_len = 1
        if max_seq_len < seq_len:
            max_seq_len = seq_len
    return(max_seq_len)