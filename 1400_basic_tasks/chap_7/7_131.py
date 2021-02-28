from main_funcs import get_input


def num_duplicates(n:int=20) -> int:
    num_seq = 1
    prev_a = get_input('Введите число: ')
    for _ in range(1, n):
        a = get_input('Введите число: ')
        if a == prev_a:
            num_seq += 1
        prev_a == a
    
    return(num_seq)