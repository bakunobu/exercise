from main_funcs import get_input


def first_duplicate(n:int=20) -> int:
    num_dupl = 1
    a_prev = get_input('Введите число: ')
    for _ in range(1, n):
        a = get_input('Введите число: ')
        if a_prev == a:
            num_dupl += 1
            a_prev = a
    return(num_dupl)
       