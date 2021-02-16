from main_funcs import get_input


def neg_seq(n:int) -> int:
    seq_len = 0
    msg = 'Введите число: '
    a = get_input(msg)
    i = 1
    while a < 0 and i < n:
        seq_len += 1
        a = get_input(msg)
        i += 1
    return(seq_len)

print(neg_seq(5))